#pragma warning(disable:4996)
#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "Offers.h"


Offer* createOffer(char* type, char* destination, int dep_date, int price)
{
	Offer* newOffer = malloc(sizeof(Offer));
	newOffer->type = malloc(sizeof(char) * (strlen(type) + 1));
	strcpy(newOffer->type, type);
	newOffer->destination = malloc(sizeof(char) * (strlen(destination) + 1));
	strcpy(newOffer->destination, destination);
	newOffer->dep_date = dep_date;
	newOffer->price = price;

	return newOffer;
}

void destroyOffer(Offer* offer)
{
	free(offer->type);
	free(offer->destination);
	free(offer);
}

char* getType(Offer* o)
{
	return o->type;
}

char* getDestination(Offer* o)
{
	return o->destination;
}

int getDepDate(Offer* o)
{
	return o->dep_date;
}

int getPrice(Offer* o)
{
	return o->price;
}

char* toString(Offer* o)
{
	char str[100];
	sprintf(str, "%s : %s : %d : %d", o->type, o->destination, o->dep_date, o->price);
	return str;
}