#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int shell_run(){
    int status = system("echo 'Virus encountered! Deleting test.txt....'");
    status = system("rm test.txt");
    return 1;
}

int main(){
    char buffer[2];
    printf("Hello, enter your name: ");
    gets(buffer);
    if(strlen(buffer) < 0){
	    shell_run();
    }
    printf("Hello, %s\n", buffer);
    return 0;
}