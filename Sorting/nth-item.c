#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "common.h"

void usage(void) {
    printf("usage: nth-item <length> [position]\n");
}

int find_item_at_position(int *data, int p, int r, int position) {
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
	    if (position <= j) {
		r = j;
		if (p == position && r == position) {
		    return data[position];
		}

		pivot = data[p];
		i = p-1;
		j = r+1;
	    }
	    else if (position > j) {
		p = j+1;
		if (p == position && r == position) {
		    return data[position];
		}

		pivot = data[p];
		i = p-1;
		j = r+1;
	    }
	}
    }
}

int main(int argc, char **argv) {
    if (argc < 2) {
	usage();
	exit(2);
    }

    int length;
    if ( (!(length = strtol(argv[1], NULL, 10)) && errno == EINVAL) || (length < 0)) {
	printf("Invalid length: %s\n", argv[1]);
	usage();
	exit(3);
    }

    int position;
    if (argc == 3) {
	if ( (!(position = strtol(argv[2], NULL, 10)) && errno == EINVAL) || (position < 0) || (position > length-1)) {
	    printf("Invalid position: %s\n", argv[2]);
	    usage();
	    exit(3);
	}
    }
    else {
	position = length/2;
    }

    int *data = generate_median_data(length, position);
    if (data) {
	printf("PRE:  ");
	print_test_data(data, length);
	int value = find_item_at_position(data, 0, length-1, position);
	printf("POST: ");
	print_test_data(data, length);

	if (validate_median_data(data, length, position, value)) {
	    printf("Nth-Item successful!\n");
	}
	else {
	    printf("Nth-Item FAILED.\n");
	    printf("Found: %d, Expected: %d\n", value, data[position]);
	    print_test_data(data, length);
	}
	free(data);
    }

    exit(0);
}
