#include<stdio.h>
int print(int x){
	if(x == 0)
		return 0;
	else
		return print(x--);
}

int main(){
	int x = 5;
	print(x);
	return 0;
}

