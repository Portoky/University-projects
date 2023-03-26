#include <stdio.h>

void convert(int a, char res[]);

int main()
{
    int a = 0b01011111011100001100100010110001;
    char res[9] = "";
    convert(a, res);
    printf("%s", res);
}