#ifndef _COMMON_H_
#define _COMMON_H_

#define FALSE (0)
#define TRUE (!FALSE)

int *generate_test_data(int length, int max);
int *generate_median_data(int length, int position);
void print_test_data(int *data, int length);
int validate_data(int *data, int length);
int validate_median_data(int *data, int length, int position, int value);

#endif // _COMMON_H_

