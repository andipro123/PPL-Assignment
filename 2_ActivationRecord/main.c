#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char **argv){
    char buffer[256];
    strcpy(buffer, argv[1]);
    puts(buffer);
    return 0;
}
