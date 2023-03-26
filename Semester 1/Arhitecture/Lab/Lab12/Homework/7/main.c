#include <stdio.h>

void longestPrefix(char sir1[], char sir2[], char sirRes[]);

int main()
{
    char s1[10] = "abcdefgh";
    char s2[10] = "abcdlmn";
    char s3[10] = "absd";
    char sirRes1[10] = "";
    char sirRes2[10] = "";
    char sirRes3[10] = "";
    longestPrefix(s1, s2, sirRes1);
    printf("%s\n", sirRes1);
    longestPrefix(s2, s3, sirRes2);
    printf("%s\n", sirRes2);
    longestPrefix(s3, s1, sirRes3);
    printf("%s\n", sirRes3);
}