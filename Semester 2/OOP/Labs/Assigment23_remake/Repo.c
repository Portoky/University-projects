#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "Repo.h"

void sortOffersByPrice(DynamicArray* offers)//insertion sort
{
	for (int i = 1; i < getLength(offers); ++i) {
		Offer* o = get(offers, i);

		for (int j = i - 1; j >= 0 && getPrice(get(offers, j)) > o->price; --j) {
			offers->elements[j + 1] = offers->elements[j];
			offers->elements[j] = o;
		}
	}
}

void sortOffersByPriceInverse(DynamicArray* offers)//insertion sort
{
	for (int i = 1; i < getLength(offers); ++i) {
		Offer* o = get(offers, i);

		for (int j = i - 1; j >= 0 && getPrice(get(offers, j)) < o->price; --j) {
			offers->elements[j + 1] = offers->elements[j];
			offers->elements[j] = o;
		}
	}
}

Repository* createRepository()
{
	Repository* repo = malloc(sizeof(Repository));
	repo->arr = createDynamicArray(5, destroyOffer);
	return repo;
}

void destroyRepository(Repository* repo)
{
	destroyDynamicArray(repo->arr);
	free(repo);
}


int findOfferRepo(Repository* repo, char* dest, int dep_date)
{
	for (int i = 0; i < getLength(repo->arr); ++i)
	{
		Offer* current = get(repo->arr, i);
		if (strcmp(getDestination(current), dest) == 0 && getDepDate(current) == dep_date)
			return i;
	}
	return -1;
}

int addOfferRepo(Repository* repo, Offer* offer)
{
	if (findOfferRepo(repo, getDestination(offer), getDepDate(offer)) != -1)
		return 1;
	add(repo->arr, offer);
	return 0;
}

int removeOfferRepo(Repository* repo, char* dest, int dep_date)
{
	int pos = findOfferRepo(repo, dest, dep_date);
	if (pos == -1)
		return 1;
	removeElement(repo->arr, pos);
	return 0;
}

int updateOfferRepo(Repository* repo, Offer* offer)
{
	int pos = findOfferRepo(repo, getDestination(offer), getDepDate(offer));
	if (pos == -1)
		return 1;
	update(repo->arr, offer, pos);
	return 0;

}

DynamicArray* listByTypeRepo(Repository* repo, char* type)
{
	DynamicArray* list = createDynamicArray(getLength(repo->arr), destroyOffer);
	for(int i = 0; i < getLength(repo->arr); ++i)
		if (strstr(getType(get(repo->arr, i)), type) != NULL)
		{
			add(list, get(repo->arr, i));
		}

	sortOffersByPrice(list);
	return list;
}

DynamicArray* listByDestinationRepo(Repository* repo, char* dest)
{
	DynamicArray* list = createDynamicArray(getLength(repo->arr), destroyOffer); //we contain the offers in a newly created Dynamic offers->we display this later on
	for (int i = 0; i < getLength(repo->arr); ++i) {
		//printf("%s %s \n", offers->elems[i].destination, dest);
		if (strstr(getDestination(get(repo->arr, i)), dest) != NULL) {
			add(list, get(repo->arr, i));
		}
	}
	//sorting them by price
	sortOffersByPrice(list);
	/*for (int i = 0; i < getLength(list); ++i)
		printf("%d ", getPrice(get(list, i)));*/
	return list;

}

DynamicArray* listByTypeAndDateRepo(Repository* repo, char* type, int date, int decision)
{
	
	DynamicArray* list = createDynamicArray(getLength(repo->arr), destroyOffer);
	for (int i = 0; i < getLength(repo->arr); ++i)
	{
		
		if (strcmp(getType(get(repo->arr, i)), type) == 0 && getDepDate(get(repo->arr, i)) >= date)
		{
			add(list, get(repo->arr, i));
			
		}
	}
	/*for (int i = 0; i < getLength(list); ++i)
		printf("%d ", getPrice(get(list, i)));*/
	if (decision == 1)
		sortOffersByPrice(list);
	else if (decision == 2)
		sortOffersByPriceInverse(list);
	return list;
}

DynamicArray* getAllRepo(Repository* repo)
{
	return repo->arr;
}
