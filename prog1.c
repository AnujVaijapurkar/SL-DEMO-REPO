#include<stdio.h>

int sum(int a, int b)
{
    return a+b;
}

int diff(int a, int b)
{
    return a-b;
}
void main()
{
    int s= sum(20,10);
    printf("Sum is %d",s);
}