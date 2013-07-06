#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "common.h"

void merge(int *data, int p, int q, int r) {
    int *tmp;
    int size = sizeof(int)*(r-p+1);
    if ( (tmp = malloc(size)) != NULL) {
	int i = p;
	int j = q+1;
	int k = 0;
	while (i <= q || j <= r) {
	    if (i <= q) {
		if (j > r || data[i] < data[j]) {
		    tmp[k++] = data[i++];
		}
		else {
		    tmp[k++] = data[j++];
		}
	    }
	    else {
		tmp[k++] = data[j++];
	    }
	}
	memcpy(&data[p], tmp, size);
	free(tmp);
    }
}

void merge_sort(int *data, int p, int r) {
    if (p < r) {
	int q = (p+r)/2;
	merge_sort(data, p, q);
	merge_sort(data, q+1, r);
	merge(data, p, q, r);
    }
}

void usage(void) {
    printf("usage: mergesort <length>\n");
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
	merge_sort(data, 0, length-1);
	if (validate_data(data, length)) {
	    printf("Merge Sort successful!\n");
	}
	else {
	    printf("Merge Sort FAILED.\n");
	    print_test_data(data, length);
	}
	free(data);
    }
    else {
	printf("Error generating test data.\n");
	exit(1);
    }
    exit(0);
}
