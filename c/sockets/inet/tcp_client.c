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
#include <arpa/inet.h>
#include <unistd.h>

int main(){
	int rc; //result codes
	int sd; //socket descriptor
	struct sockaddr_in addr; //sockaddr type for inet (internet protocol)
	struct sockaddr_in remote;
	socklen_t raddrlen;
	char sa[] = "127.0.0.1"; //address to connect to
	int portnum = 8051;
	unsigned char buf[8] = {0xde, 0xad, 0xbe, 0xef, 0xca, 0xfe, 0xba, 0xbe};

	// create a unix TCP socket using default (0) protocol
	// use SOCK_STREAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_INET, SOCK_STREAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//initialize server address
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr(sa);
	addr.sin_port = htons(portnum);

	// connect to server
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
