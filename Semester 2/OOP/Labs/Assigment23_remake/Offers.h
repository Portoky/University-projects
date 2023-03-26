#pragma once

typedef struct
{
	char* type;
	char* destination;
	int dep_date;
	int price;
}Offer;

Offer* createOffer(char* type, char* destination, int dep_date, int price);
void destroyOffer(Offer* offer);
char* getType(Offer* o);
char* getDestination(Offer* o);
int getDepDate(Offer* o);
int getPrice(Offer* o);
char* toString(Offer* o);