#include <stdio.h>

void SumAndProduct(int a, int b, int* p, int* s)
{
    *s = a + b;
    *p = a * b; 
}

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    int s, p;
    SumAndProduct(a, b, &p, &s);
    printf("The sum and the product of the two numbers: %d %d", s, p);
    return 0;
}