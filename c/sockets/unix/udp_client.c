/*
 * unix socket client
 * example program
 *
 * author: toranova
 * mailto: chia_jason96@live.com
 *
 * see this
 * https://stackoverflow.com/questions/3324619/unix-domain-socket-using-datagram-communication-between-one-server-process-and
 *
 * tldr; unix sockets on UDP needs to BIND to their own endpoint, then CONNECT to the
 * server's endpoint.
 * this is very different from how AF_INET UDP works (no binding/connection on client side)
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
	struct sockaddr_un remote; //sockaddr type for unix
	socklen_t addrlen = sizeof(addr);
	char sp[] = "unix.sock"; //unix socket path
	char cp[] = "udp_client.sock"; //client (this) endpoint path
	unsigned char buf[8] = {0xde, 0xad, 0xbe, 0xef, 0xca, 0xfe, 0xba, 0xbe};

	// create a unix UDP socket using default (0) protocol
	// use SOCK_DGRAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_UNIX, SOCK_DGRAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//initialize server socket address
	memset(&remote, 0, sizeof(remote));
	remote.sun_family = AF_UNIX;
	memcpy(remote.sun_path, sp, strlen(sp)); //alternate is strncpy

	rc = connect(sd, (struct sockaddr *)&remote, sizeof(remote)); //connect to server endpoint
	if(rc < 0){
		perror("connect");
		goto teardown;
	}

	//initialize client socket address
	memset(&addr, 0, sizeof(addr));
	addr.sun_family = AF_UNIX; //set address type
	memcpy(addr.sun_path, cp, strlen(cp)); //set socket path
	unlink(cp);

	rc = bind(sd, (struct sockaddr *)&addr, sizeof(addr)); //bind to own
	if(rc < 0){
		perror("bind");
		goto teardown;
	}

	// the 4th arg is the flag to this call
	// setting it to MSG_DONTWAIT can make it a non-blocking call
	// MSG_PEEK allows see what's in the receive buffer without causing
	// the pointer to advance (when we call recvfrom again, we get the same data)

	// either of the following lines work
	//rc = sendto(sd, buf, 8, 0, (struct sockaddr *)&remote, sizeof(remote));
	rc = send(sd, buf, 8, 0); //this work because 'connect' has set the remote addr
	if( rc < 0 ){ perror("send"); goto teardown; }

	// either of the following lines work
	//rc = recvfrom(sd, buf, rc, 0, (struct sockaddr *)&addr, &addrlen); //echo back
	rc = recv(sd, buf, rc, 0); //this work because 'bind' has set the recv addr
	if( rc < 0){ perror("recv"); goto teardown; }

	// final
	printf("resp. (%u):", rc);
	for(size_t i=0; i<rc;i++){ printf("%02x", buf[i]); }
	printf("\n");
	rc = 0;

teardown:
	close(sd); //close server socket
	unlink(cp);
	return rc;
}
