//
// Created by User on 3/12/2023.
//
#define _CRT_SECURE_NO_WARNINGS
#include "DynamicOffers.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <malloc.h>

void sortOffersByPrice(DynamicOffers* offers)//insertion sort
{
    for(int i = 1; i < offers->nm_of_elems; ++i) {
        Offer o = offers->elems[i];

        for (int j = i - 1; j >= 0 && offers->elems[j].price > o.price; --j) {
            offers->elems[j + 1] = offers->elems[j];
            offers->elems[j] = o;
        }
    }
}

DynamicOffers* CreateDynamicOffers(int capacity)
{
    DynamicOffers* offers = malloc(sizeof(DynamicOffers));
    if(offers == NULL)
        return NULL;

    offers->capacity = capacity;
    offers->nm_of_elems = 0;
    offers->elems = malloc(capacity * sizeof(Offer));
    if(offers->elems == NULL)
        return NULL;

    return offers;
}

void destroyOffers(DynamicOffers* offers)
{
    if(offers != NULL) {
//        for(int i = 0; i < getLength(offers); ++i)
//            free(&offers->elems[i]);
        free(offers->elems);
        offers->elems = NULL;
        free(offers);
        offers = NULL;
    }
}

int resize(DynamicOffers* offers)
{
    offers->capacity =offers->capacity * 2;
    //printf("%d", offers->capacity);
    Offer* temp = realloc(offers->elems, offers->capacity * sizeof(Offer));
    if(temp == NULL)
        return -1;
    for(int i = 0; i < getLength(offers); ++i)
        temp[i] = offers->elems[i];
    offers->elems = temp;
    return 0;
}

//Offer* getAll(DynamicOffers* offers)
//{
//    return offers->elems;
//}

int getCapacity(DynamicOffers* offers)
{
    return offers->capacity;
}

int getLength(DynamicOffers* offers)
{
    return offers->nm_of_elems;
}

Offer* getOffer(DynamicOffers* offers, int pos)
{
    if(pos > getLength(offers))
        return NULL;
    return &offers->elems[pos];
}

int checkUnique(DynamicOffers* offers, Offer* o)
{
    for(int i = 0; i < offers->nm_of_elems; ++i) {

        //printf("%s %s \n", offers->elems[i].destination, o->destination);
        //printf("%d %d \n", offers->elems[i].dep_date, o->dep_date);
        if (strcmp(getDestination(&offers->elems[i]), getDestination(o)) == 0 &&
            getDepDate(&offers->elems[i]) == getDepDate(o)) {

            return -1; //not unique
        }
    }
    return 0;
}

int addOffer(DynamicOffers* offers, Offer* o)
{
    int res = checkUnique(offers, o);
    if(res == -1 || offers == NULL)
        return -1;
    if(getCapacity(offers) == getLength(offers))
        resize(offers);
    offers->elems[offers->nm_of_elems] = *o;
    offers->nm_of_elems++;
    return 0;
}

int updateOffer(DynamicOffers* offers, Offer* o)
{
    int res = checkUnique(offers, o);
    if(res == 0 || offers == NULL || offers->elems == NULL)
        return -1;

    for(int i = 0; i < offers->nm_of_elems; ++i)
        if(strcmp(offers->elems[i].destination, o->destination) == 0 && offers->elems[i].dep_date == o->dep_date) {
            offers->elems[i] = *o;
            return 0;
        }
}

void removeOffer(DynamicOffers* offers, char* dest, int dep_date)
{
    int i;
    for(i = 0; i < offers->nm_of_elems; ++i)
    {
        if(strcmp(offers->elems[i].destination, dest) == 0 && offers->elems[i].dep_date == dep_date)
            break;
    }
    if (i < offers->nm_of_elems) {
        for (; i < offers->nm_of_elems - 1; ++i)
            offers->elems[i] = offers->elems[i + 1];

        --offers->nm_of_elems;
    }
}

DynamicOffers* listByDestination(DynamicOffers* offers, char* dest)
{
    DynamicOffers* list = CreateDynamicOffers(offers->nm_of_elems + 1); //we contain the offers in a newly created Dynamic offers->we display this later on
    for(int i = 0; i < getLength(offers); ++i) {
        //printf("%s %s \n", offers->elems[i].destination, dest);
        if (strstr(offers->elems[i].destination, dest) != NULL) {
            addOffer(list, &offers->elems[i]);
        }
    }
    //sorting them by price
    sortOffersByPrice(list);

    return list;

}

DynamicOffers* listByTypeAndDate(DynamicOffers* offers, char* type, int date)
{
    DynamicOffers* list = CreateDynamicOffers(offers->nm_of_elems + 1);
    for(int i = 0; i < offers->nm_of_elems; ++i)
    {
        if(strstr(offers->elems[i].type, type) != NULL && offers->elems[i].dep_date > date)
            addOffer(list, &offers->elems[i]);
    }

    return list;
}

Offer* getAll(DynamicOffers* offers)
{
    return offers->elems;
}
