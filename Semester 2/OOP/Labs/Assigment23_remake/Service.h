#pragma once
#include "Repo.h"

typedef struct
{
	char* command;
	char* type1; //type before
	char* type2; //type after
	int price1; //price before
	int price2; //price after -> we nned this for update
	char* dest;
	int dep_date;
}Command;

typedef struct
{
	Repository* repo;
	DynamicArray* history;
	int pos;
	int maxpos;
}Service;

Service* createService();
void destroyService(Service* service);

//creates an offer from the given parameter(type, destination, dep_date, price) and add it to the list of offers
//returns 0 if succesful
//          -1 otherwise
int addOfferService(Service* service, char* type, char* destination, int dep_date, int price);
//removes an offer from the list identified by destination or departure date + decreases the nm_of_elems
int removeOfferService(Service* service, char* dest, int dep_date);
//updates an Offer in the list, identified by dest and departure date
int updateOfferService(Service* service, char* type, char* destination, int dep_date, int price);
//returns a pointer to DynamicOffers structure which contains element whose destination equal with the given destination
DynamicArray* listByDestinationService(Service* service, char* dest);
//returns a pointer to a DynamicOffers structure which contains only those elements where the given type is a substring
//of the element type and the element's date is after the given date
DynamicArray* listByTypeAndDateService(Service* service, char* type, int date, int decision);
//returns a pointer to a DynamicOffers structure which contains only those elements where the given type is a substring of the offers type
DynamicArray* listByTypeService(Service* service, char* type);
//returns a pointer to our offers structure, containing all the offers(elements)
DynamicArray* getAllService(Service* service);
Command* createCommand(char* instruction, char* type1, char* type2, int price1, int price2, int dep_date, char* dest);
int undo(Service* service);
int redo(Service* service);
//int undo2(Service* service);
//int redo2(Service* service);