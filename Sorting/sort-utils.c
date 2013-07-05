#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "common.h"

int *generate_test_data(int length, int max) {
    int *data;
    if ( (data = malloc(sizeof(int)*length)) != NULL) {
	srand(time(NULL));
	for (int i = 0; i < length; i++) {
	    data[i] = rand() % max + 1;
	}
    }
    return data;
}

void print_test_data(int *data, int length) {
    for (int i = 0; i < length; i++) {
	printf("%d%s", data[i], i != length-1 ? ", " : "\n");
    }
}

int validate_data(int *data, int length) {
    int prev = length ? data[0] : 0;
    for (int i = 1; i < length; i++) {
	if (data[i] < prev) {
	    return FALSE;
	}
	prev = data[i];
    }
    return TRUE;
}

