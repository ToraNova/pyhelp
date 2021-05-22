/*
 * tcpip socket server
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
	int sd, cd; //server and client socket descriptors
	struct sockaddr_in addr; //server address
	struct sockaddr_in remote; //client remote address
	socklen_t addrlen = sizeof(addr);
	char sa[] = "127.0.0.1"; // addrress to bind to local machine
	int portnum = 8051; // port to listen on
	unsigned char buf[128]; //buffer
	char aux[64]; int aup;

	// create a unix TCP socket using default (0) protocol
	// use SOCK_STREAM | SOCK_NONBLOCK to have non blocking mode
	sd = socket(AF_INET, SOCK_STREAM, 0);
	if(sd < 0){
		perror("socket");
		return -1;
	}

	//allow socket to be quicky reused
	int reuse = 1;
	rc = setsockopt(sd, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(int));
	if(rc < 0){
		perror("setsockopt");
		goto teardown;
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

	//listen with up to 1 incoming connection queue
	// accept incoming connections
	printf("echo tcp server on %s:%d\n", sa, portnum);
	listen(sd, 1);
	cd = accept(sd, (struct sockaddr *)&remote, &addrlen); //block until conn est.
	if(cd < 0){
		perror("remote");
		rc = -1;
		goto teardown;
	}

	inet_ntop(AF_INET, &(remote.sin_addr), aux, INET_ADDRSTRLEN );
	aup = ntohs(remote.sin_port);
	printf("conn'd from %s:%d\n", aux, aup);

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
	return rc;
}
