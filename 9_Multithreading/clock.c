#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

int hour = 0, minute = 0, second = 0;

void* sec() {
	while(1) {
		printf("\r%02d : % 02d : %02d", hour, minute, second);
		sleep(1);
		second++;
	}
}

void* min() {
	while(1) {
		if(second == 60) {
			second = 0;
			minute++;
		}	
	}
}

void* hours() {
	while(1) {
		if(minute == 60) {
			minute = 0;
			hour++;
			if(hour == 24)
				hour = 0;
		}
		
	}
}

void* print_time() {
	while(1) {
		printf("\r%02d : % 02d : %02d", hour, minute, second);
	}
}

int main() {
	time_t now = time(0);
	struct tm *local = localtime(&now);
	
	hour = local -> tm_hour;
	minute = local -> tm_min;
	second = local -> tm_sec;
	
	pthread_t thr1, thr2, thr3, thr4;
	
	pthread_create(&thr1, NULL, sec, NULL);
	pthread_create(&thr2, NULL, min, NULL);
	pthread_create(&thr3, NULL, hours, NULL);
	pthread_create(&thr4, NULL, print_time, NULL);
	
	pthread_join(thr1, NULL);
	pthread_join(thr2, NULL);
	pthread_join(thr3, NULL);
	pthread_join(thr4, NULL);
	return 0;
}