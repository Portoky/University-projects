//problem 2
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <exception>

void print_options()
{
	printf("1. Read an array.\n");
	printf("2. Read solve problem a -> generates all primes below n.\n");
	printf("3. Solve b -> longest contiguos subsequence of s.t two consecutive elements are relative primes.\n");
	printf("4. Exit\n");
}

void read_n(int* n)
{
	printf("Please type int the number you want smaller primes: ");
	scanf_s("%d", n);
}

void read_arr(int* arr, int* n)
{
	printf("Please type int the number of elements in the array: ");
	scanf_s("%d", n);
	for (int i = 0; i < *n; ++i)
	{
		scanf_s("%d", &arr[i]);
	}
}

int gcd(int a, int b)
{
	
	//returns the largest common divisor of a and b
	//a, b - natural numbers
	
	while (b != 0)
	{
		int m = a % b;
		a = b;
		b = m;
	}
	return a;
}

bool relative_primes(int a, int b)
{
	
	//Returns if the two numbers are relative primes

	if(gcd(a, b) == 1)
		return true;
	return false;
}

void first_n_prime(int n)
{
	
	 //Generates and prints all the prime numbers smaller then n
	 //n : natural number
	 //error occure if n is smaller than 0, or not a natural number
	 
	for (int x = 2; x < n; ++x)
	{
		int i = 2;
		for (i = 2; i <= sqrt(x) && (x % i != 0); ++i);

		if(i > sqrt(x)) //prime
			printf("%d ", x);
	}
	printf("\n");
}

void longest_relative_prime_subsequence(int arr[], int n, int* start, int* end)
{
	//Finds the longest subsequence in an array
	//arr - the array
	//n - positive number, the number of elements in the array
	//start - starting index where we return the where subsequence starts
	//end - ending index where we return the where  subsequence ends
	//pre - the array shouldnt be empty, n != 0, start == end == 0

	int curr_start = *start;
	int curr_end = *end;
	for(int i = 0; i < n + 1; ++i)
	{
		if(relative_primes(arr[i], arr[i + 1]))
			curr_end += 1;
		else
		{
			if(curr_end - curr_start > *end - *start)
			{
				*end = curr_end;
				*start = curr_start;
			}
			curr_start = i;
			curr_end = i;
		}
	}

}

int main()
{
	int arr[100];
	int n = 0;
	int option;
	
	while (true)
	{
		print_options();
		scanf_s("%d", &option);
		if (option == 4) {
			return 0;
		}
		switch (option)
		{
		case 1:
			read_arr(arr, &n);
			break;
		case 2:
		{
			int n2;
			read_n(&n2);
			first_n_prime(n2);
			break;
		}
		case 3:
		{
			if (n == 0)
			{
				printf("Please read the array first! \n");
				break;
			}
			int start = 0;
			int end = 0;
			longest_relative_prime_subsequence(arr, n, &start, &end);
			printf("%d - %d \n", start, end);
			break;
		}
		default:
			printf("Wrong input! \n");
			break;
		}
	}
	return 0;

}