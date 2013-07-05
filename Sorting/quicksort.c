#include <stdio.h>
#include <stdlib.h>

#include "common.h"

#define LENGTH (10)

int main(int argc, char **argv) {
    int *data = generate_test_data(LENGTH, 10);
    if (data) {
	print_test_data(data, LENGTH);
    }
    else {
	printf("Error generating test data.\n");
	exit(1);
    }
    exit(0);
}
