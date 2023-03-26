#pragma once
#include "Offers.h"

typedef void* TElem;

typedef void (*destroyer)(TElem);

typedef struct
{
	TElem* elements;
	int capacity;
	int length;
	destroyer destroyFunction;
}DynamicArray;

DynamicArray* createDynamicArray(int capacity, destroyer destroyFunction);
void destroyDynamicArray(DynamicArray* arr);
//returns the size of the dynamic array
int getLength(DynamicArray* arr);
//returns a pointer to the element at the given position
TElem get(DynamicArray* arr, int pos);
//add an element to the array (increases length)
void add(DynamicArray* arr, TElem e);
//removes an element to the array (decreases length)
void removeElement(DynamicArray* arr, int poz);
//updates the element at the given position poz to e
void update(DynamicArray* arr, TElem e, int poz);

