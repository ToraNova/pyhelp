#include <stdio.h>
#include <time.h>

int main () {
	double sum = 0;
	double add = 1;

	// Start measuring time
	struct timespec begin, end;
	clock_gettime(CLOCK_REALTIME, &begin);
	//clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &begin);


	int iterations = 1000*1000*1000;
	for (int i=0; i<iterations; i++) {
		sum += add;
		add /= 2.0;
	}

	// Stop measuring time and calculate the elapsed time
	clock_gettime(CLOCK_REALTIME, &end);
	//clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end);
	long seconds = end.tv_sec - begin.tv_sec;
	long nanoseconds = end.tv_nsec - begin.tv_nsec;
	double elapsed = seconds + nanoseconds*1e-9;

	printf("res: %.20f\n", sum);

	printf("time measured: %.3f seconds.\n", elapsed);

	return 0;
}
