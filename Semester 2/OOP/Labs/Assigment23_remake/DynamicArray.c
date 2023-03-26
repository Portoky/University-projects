#include <stdlib.h>
#include "DynamicArray.h"



DynamicArray* createDynamicArray(int capacity, destroyer destroyFunction)
{
	DynamicArray* array = malloc(sizeof(DynamicArray));
	array->length = 0;
	array->capacity = capacity;
	array->elements = malloc(sizeof(TElem) * array->capacity);
	array->destroyFunction = destroyFunction;
	return array;
}

void destroyDynamicArray(DynamicArray* arr)
{
	for (int i = 0; i < arr->length; ++i)
		arr->destroyFunction(arr->elements[i]);
	free(arr->elements);
	free(arr);
}

int getLength(DynamicArray* arr)
{
	return arr->length;
}

TElem get(DynamicArray* arr, int pos)
{
	return arr->elements[pos];
}

void resize(DynamicArray* arr) {
	arr->capacity *= 2;
	TElem* aux = malloc(arr->capacity * sizeof(TElem));
	for (int i = 0; i < arr->length; i++) {
		aux[i] = arr->elements[i];
	}
	free(arr->elements);
	arr->elements = aux;
}

void add(DynamicArray* arr, TElem e)
{
	if (arr->capacity == arr->length) {
		resize(arr);
	}
	arr->elements[arr->length++] = e;
}

void removeElement(DynamicArray* arr, int poz) {
	int i;
	//free(arr->elements[poz]);
	//arr->destroyFunction(get(arr, poz));
	for (i = poz; i < arr->length - 1; i++)
		arr->elements[i] = arr->elements[i + 1];
	arr->length--;

}

void update(DynamicArray* arr, TElem e, int poz)
{
	arr->elements[poz] = e;
}
/*
void testDynamicArray() {
	DynamicArray* arr = createDynamicArray(2, destroyOffer);
	assert(arr->length == 0);
	assert(arr->capacity == 2);

	Offer* p1 = createOffer("mars", "red", 23.4);
	Offer* p2 = createOffer("venus", "blue", 223.4);
	add(arr, p1);
	add(arr, p2);
	assert(arr->length == 2);
	assert(arr->capacity == 2);

	Offer* p3 = createOffer("earth", "green", 123.7);
	add(arr, p3);
	assert(arr->capacity == 4);

	assert(strcmp(getName(get(arr, 0)), "mars") == 0);

	destroyDynamicArray(arr);
}*/