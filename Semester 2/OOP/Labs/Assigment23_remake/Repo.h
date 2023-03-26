#pragma once
#include "DynamicArray.h"

typedef struct
{
	DynamicArray* arr;
}Repository;

Repository* createRepository();
void destroyRepository(Repository* repo);
//finds an offer on the repository based on destination and dep_date, returns a pointer to that offer 
int findOfferRepo(Repository* repo, char* dest, int dep_date);
//add the offer to the repo
int addOfferRepo(Repository* repo, Offer* offer);
int removeOfferRepo(Repository* repo, char* dest, int dep_date);
int updateOfferRepo(Repository* repo, Offer* offer);
DynamicArray* listByDestinationRepo(Repository* repo, char* dest);
DynamicArray* listByTypeAndDateRepo(Repository* repo, char* type, int date, int decision);
DynamicArray* listByTypeRepo(Repository* repo, char* type);
DynamicArray* getAllRepo(Repository* repo);