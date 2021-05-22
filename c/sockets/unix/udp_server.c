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
	struct sockaddr_un addr; //sockaddr type for unix
	struct sockaddr_un remote; //client remote address
	socklen_t addrlen = sizeof(remote);
	char sp[] = "unix.sock"; //unix socket path
	unsigned char buf[128]; //buffer

	// create a unix UDP socket using default (0) protocol
	// use SOCK_DGRAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_UNIX, SOCK_DGRAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//initialize socket address
	memset(&addr, 0, sizeof(addr));
	addr.sun_family = AF_UNIX; //set address type
	memcpy(addr.sun_path, sp, strlen(sp)); //set socket path
	unlink(sp);

	//bind socket to socket path
	rc = bind(sd, (struct sockaddr *)&addr, sizeof(addr));
	if(rc < 0){
		perror("bind");
		goto teardown;
	}

	// await receive
	printf("echo udp server on socket file :%s\n", sp);
	// the 4th arg is the flag to this call
	// setting it to MSG_DONTWAIT can make it a non-blocking call
	// MSG_PEEK allows see what's in the receive buffer without causing
	// the pointer to advance (when we call recvfrom again, we get the same data)
	rc = recvfrom(sd, buf, 128, 0, (struct sockaddr *)&remote, &addrlen);
	if( rc < 0){ perror("recv"); goto teardown; }
	rc = sendto(sd, buf, rc, 0, (struct sockaddr *)&remote, addrlen); //echo back
	if( rc < 0 ){ perror("send"); goto teardown; }

	//final
	printf("echo. (%u):", rc);
	for(size_t i=0; i<rc;i++){ printf("%02x", buf[i]); }
	printf("\n");
	rc = 0;

teardown:
	close(sd); //close server socket
	unlink(sp);
	return rc;
}
