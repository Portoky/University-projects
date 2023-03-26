#include <stdio.h>

typedef struct {
    int  arr[50], len;
}vector;

vector readVector2()
{
    vector a;
    scanf("%d", &a.len);
    for(int i = 0; i < a.len; ++i)
    {
        int x;
        scanf("%d", &x);
        a.arr[i] = x;
    }

    return a;
}

vector readVector() {
    int x, l = 0, arr[50];
    vector a;
    a.len = 0;
    do
    {
        printf("Element: ");
        scanf("%d", &x);
        printf("%d", x);
        a.arr[a.len++] = x;
        printf("%d", a.len);
    }while(x != 0);

    --a.len;

    return a;
}

int sum(vector a)
{
    int sum = 0;
    printf("%d", a.len);
    for(int i = 0; i < a.len; ++i)
    {
        printf("%d", a.arr[i]);
        sum += a.arr[i];
    }
    return sum;
}

void longestSubSequence(vector a, int* start, int* end)
{
    int maxSize = 0;
    int currSize = 0;
    *start = 0;
    *end = 0;
    for(int i = 0; i < a.len - 1; ++i)
    {
        if (a.arr[i] != a.arr[i+1])
        {
            if(currSize > maxSize)
            {
                maxSize = currSize;
                *start = *end;
                *end = i;
                currSize = 0;
            }
        }
        else
        {
            ++currSize;
        }
    }
}

int main()
{
    int option;
    while(1)
    {
        printf("1. Read until 0 and print the sum of read numbers\n");
        printf("2. Given  a  vector  of  numbers,  finds  the  longest  contiguous  subsequence  such  that  all elements are equal.\n");
        printf("0. Exit\n");
        scanf("%d", &option);
        if(option == 0)
            break;
        switch(option){
            case 1:
            {
                vector a = readVector();
                int s = sum(a);
                printf("Sum: %d \n", s);
                break;
            }
            case 2:
            {
                vector a = readVector2();
                int start;
                int end;
                longestSubSequence(a, &start, &end);
                printf("%d %d", start, end);
            }
            default:
            {
                break;
            }

        }


    }
    return 0;
}