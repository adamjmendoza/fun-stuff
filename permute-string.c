#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void permute_string(char *string) {
    int n = strlen(string);
    int j = n;
    while (j >= 0) {
	printf("%s\n", string);
	
	j = n-2;
	while (j >= 0 && string[j] >= string[j+1]) j--;

	if (j >= 0) {
	    int l = n-1;
	    while (string[j] >= string[l]) l--;
	
	    char tmp = string[j];
	    string[j] = string[l];
	    string[l] = tmp;

	    int k = j+1;
	    l = n-1;
	    while (k < l) {
		tmp = string[k];
		string[k++] = string[l];
		string[l--] = tmp;
	    }
	}
    }
}

int main(int argc, char **argv) {
    char *string = argv[1];
    permute_string(string);
    exit(0);
}
