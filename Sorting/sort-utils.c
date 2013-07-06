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

void shuffle(int *data, int length) {
    srand(time(NULL));
    for (int i = length-1; i > 0; i--) {
	int j = rand() % (i+1);
	int tmp = data[i];
	data[i] = data[j];
	data[j] = tmp;
    }
}

int *generate_median_data(int length, int position) {
    int *data;
    if ( (data = malloc(sizeof(int)*length)) != NULL) {
	int n_below = position ? position-1 : 0;
	srand(time(NULL));
	for (int i = 0; i < length; i++) {
	    if (i < n_below) {
		data[i] = rand() % n_below;
	    }
	    else if (i == position) {
		data[i] = position;
	    }
	    else {
		data[i] = rand() % (length-position) + position + 1;
	    }
	}
    }
    shuffle(data, length);
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

int compare(const void *a, const void *b) {
    if (*(int*)a < *(int*)b) return -1;
    if (*(int*)a > *(int*)b) return 1;
    return 0;
}

int validate_median_data(int *data, int length, int position, int value) {
    qsort(data, length, sizeof(int), compare);
    if (data[position] == value) {
	return TRUE;
    }
    return FALSE;
}
