/*
 * inet udp socket server
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
	struct sockaddr_in addr; //sockaddr type for inet
	struct sockaddr_in remote; //client remote address
	socklen_t raddrlen = sizeof(remote);
	char sa[] = "127.0.0.1"; //inet socket path
	int portnum = 8051;
	unsigned char buf[128]; //buffer
	char aux[64]; int aup;

	// create a inet UDP socket using default (0) protocol
	// use SOCK_DGRAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_INET, SOCK_DGRAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//initialize server address
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr(sa);
	addr.sin_port = htons(portnum);

	//bind socket to socket path
	rc = bind(sd, (struct sockaddr *)&addr, sizeof(addr));
	if(rc < 0){
		perror("bind");
		goto teardown;
	}

	// await receive
	printf("echo udp server on %s:%d\n", sa, portnum);
	// the 4th arg is the flag to this call
	// setting it to MSG_DONTWAIT can make it a non-blocking call
	// MSG_PEEK allows see what's in the receive buffer without causing
	// the pointer to advance (when we call recvfrom again, we get the same data)
	rc = recvfrom(sd, buf, 128, 0, (struct sockaddr *)&remote, &raddrlen);
	if( rc < 0){ perror("recv"); goto teardown; }

	inet_ntop(AF_INET, &(remote.sin_addr), aux, INET_ADDRSTRLEN );
	aup = ntohs(remote.sin_port);
	printf("recv'd %u from %s:%d\n", rc, aux, aup);

	rc = sendto(sd, buf, rc, 0, (struct sockaddr *)&remote, raddrlen); //echo back
	if( rc < 0 ){ perror("send"); goto teardown; }

	//final
	printf("echo. (%u):", rc);
	for(size_t i=0; i<rc;i++){ printf("%02x", buf[i]); }
	printf("\n");
	rc = 0;

teardown:
	close(sd); //close server socket
	return rc;
}
