/*
 * unix socket client
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
	char sp[] = "unix.sock"; //unix socket path
	unsigned char buf[8] = {0xde, 0xad, 0xbe, 0xef, 0xca, 0xfe, 0xba, 0xbe};

	// create a unix TCP socket using default (0) protocol
	// use SOCK_STREAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_UNIX, SOCK_STREAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//initialize socket address
	memset(&addr, 0, sizeof(addr));
	addr.sun_family = AF_UNIX; //set address type
	memcpy(addr.sun_path, sp, strlen(sp)); //set socket path

	/* Now connect to the server */
	rc = connect(sd, (struct sockaddr *)&addr, sizeof(addr));
	if (rc < 0){
		perror("connect");
		goto teardown;
	}
	// recv (we ignore address since we are using TCP
	// the 4th arg is the flag to this call
	// setting it to MSG_DONTWAIT can make it a non-blocking call
	// MSG_PEEK allows see what's in the receive buffer without causing
	// the pointer to advance (when we call recvfrom again, we get the same data)
	rc = sendto(sd, buf, 8, 0, NULL, 0);
	if( rc < 0 ){ perror("send"); goto teardown; }
	rc = recvfrom(sd, buf, rc, 0, NULL, 0); //get response
	if( rc < 0){ perror("recv"); goto teardown; }

	printf("resp. (%u):", rc);
	for(size_t i=0; i<rc;i++){ printf("%02x", buf[i]); }
	printf("\n");
	rc = 0;
teardown:
	close(sd); //close server socket
	return rc;
}
