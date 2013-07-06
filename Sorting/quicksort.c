#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

#include "common.h"

int partition(int *data, int p, int r) {
    int pivot = data[p];
    int i = p-1;
    int j = r+1;

    while (1) {
	do {
	    j -= 1;
	} while (data[j] > pivot);
	do {
	    i += 1;
	} while (data[i] < pivot);
	if (i < j) {
	    int tmp = data[i];
	    data[i] = data[j];
	    data[j] = tmp;
	}
	else {
	    return j;
	}
    }
}

void quicksort(int *data, int p, int r) {
    if (p < r) {
	int q = partition(data, p, r);
	quicksort(data, p, q);
	quicksort(data, q+1, r);
    }
}

void usage(void) {
    printf("usage: quicksort <length>\n");
}

int main(int argc, char **argv) {
    if (argc != 2) {
	usage();
	exit(2);
    }
    
    int length;
    if ( !(length = strtol(argv[1], NULL, 10)) && errno == EINVAL) {
	printf("Invalid length: %s\n", argv[1]);
	usage();
	exit(3);
    }

    int *data = generate_test_data(length, length);
    if (data) {
	quicksort(data, 0, length-1);
	if (validate_data(data, length)) {
	    printf("Quicksort successful!\n");
	}
	else {
	    printf("Quicksort FAILED.\n");
	}
	free(data);
    }
    else {
	printf("Error generating test data.\n");
	exit(1);
    }
    exit(0);
}
