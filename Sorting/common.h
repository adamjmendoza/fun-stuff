#ifndef _COMMON_H_
#define _COMMON_H_

#define FALSE (0)
#define TRUE (!FALSE)

int *generate_test_data(int length, int max);
void print_test_data(int *data, int length);
int validate_data(int *data, int length);

#endif // _COMMON_H_

