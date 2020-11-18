/*
 * Example of timing code
 */

#include <stdio.h>
#include <time.h>
#include <unistd.h>

//linux
long long rdtsc(){
	unsigned int lo,hi;
	__asm__ __volatile__ ("rdtsc" : "=a" (lo), "=d" (hi));
	return ((long long)hi << 32) | lo;
}

int main(int argc, char *argv[]){

	clock_t start_clock, end_clock; 	//cpu time
	double cpu_time_ms;
	time_t start_time, end_time; 		//wall time
	time_t elapsed;
	unsigned long long start_cycle, end_cycle; 	//cycle count
	unsigned long long cycles;

	//cpu clock cycle timing
	start_clock = clock();
	sleep(0.5);
	end_clock = clock();

	//wall timing
	time(&start_time); //only measures SECONDS
	sleep(1);
	sleep(0.5); //won't be counted
	time(&end_time);

	//cycle count
	start_cycle = rdtsc();
	sleep(0.5);
	end_cycle = rdtsc();

	//record time in ms (cpu time)
	cpu_time_ms = (((double) (end_clock - start_clock))/CLOCKS_PER_SEC)*1000;
	printf("cpu runtime %fms\n", cpu_time_ms);

	elapsed = end_time - start_time;
	printf("wall time %lds\n", elapsed);

	cycles = end_cycle - start_cycle;
	printf("cpu cycles s:%llu, e:%llu, t:%llu\n",start_cycle, end_cycle, cycles);
}
