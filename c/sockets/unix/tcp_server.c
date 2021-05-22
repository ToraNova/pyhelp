/*
 * unix socket server
 * example program
 *
 * author: toranova
 * mailto: chia_jason96@live.com
 */

#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>

int main(){
	int rc; //result codes
	int sd; //socket descriptor
	int cd; //client descriptor (for client connections)
	struct sockaddr_un addr; //sockaddr type for unix
	struct sockaddr_un remote; //client remote address
	socklen_t raddrlen = sizeof(remote);
	char sp[] = "unix.sock"; //unix socket path
	unsigned char buf[128]; //buffer

	// create a unix TCP socket using default (0) protocol
	// use SOCK_STREAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_UNIX, SOCK_STREAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	memset(&addr, 0, sizeof(addr)); //initialize socket address
	addr.sun_family = AF_UNIX; //set address type
	memcpy(addr.sun_path, sp, strlen(sp)); //set socket path
	unlink(sp);

	//bind socket to socket path
	rc = bind(sd, (struct sockaddr *)&addr, sizeof(addr));
	if(rc < 0){
		perror("bind");
		goto teardown;
	}

	//listen with up to 1 incoming connection queue
	// accept incoming connections
	printf("echo tcp server on socket file :%s\n", sp);
	listen(sd, 1);
	cd = accept(sd, (struct sockaddr *)&remote, &raddrlen); //block until conn est.
	if(cd < 0){
		perror("remote");
		rc = -1;
		goto teardown;
	}

	// recv (we ignore address since we are using TCP
	// the 4th arg is the flag to this call
	// setting it to MSG_DONTWAIT can make it a non-blocking call
	// MSG_PEEK allows see what's in the receive buffer without causing
	// the pointer to advance (when we call recvfrom again, we get the same data)
	rc = recvfrom(cd, buf, 128, 0, NULL, 0);
	if( rc < 0){ perror("recv"); close(cd); goto teardown; }
	rc = sendto(cd, buf, rc, 0, NULL, 0); //echo back
	if( rc < 0 ){ perror("send"); close(cd); goto teardown; }

	//final
	printf("echo. (%u):", rc);
	for(size_t i=0; i<rc;i++){ printf("%02x", buf[i]); }
	printf("\n");
	rc = 0;

	close(cd); //close client socket
teardown:
	close(sd); //close server socket
	unlink(sp);
	return rc;
}
