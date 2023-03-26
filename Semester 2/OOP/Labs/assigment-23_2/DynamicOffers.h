//
// Created by User on 3/12/2023. Repo like stuff
//
#pragma once
#ifndef A23_PORTOKY_DYNAMICOFFERS_H
#define A23_PORTOKY_DYNAMICOFFERS_H

#endif //A23_PORTOKY_DYNAMICOFFERS_H
#include "Offers.h"


typedef struct
{
    int capacity;
    int nm_of_elems;
    Offer* elems;
}DynamicOffers;

//creates a the DynamicOffers structure dinamically
//pre: param - capacity:int -> the number of Offer structure that it can hold
//post: return a pointer to the created structure
DynamicOffers* CreateDynamicOffers(int capacity);

//destroys the structure
void destroyOffers(DynamicOffers* offers);
int getCapacity(DynamicOffers* offers);
int getLength(DynamicOffers* offers);
Offer* getOffer(DynamicOffers* offers, int pos);

//increases the capacity to be two time as large an reallocates the structure's elements in the memory
//post: 0 if succesfull
//      -1 otherwise
int resize(DynamicOffers* offers);

//adds an offer to the elems dynamic list + increases the nm_of_elems
int addOffer(DynamicOffers* offers, Offer* o);

//removes an offer from the list found by destination or departure date +  decreases the nm_of_elems
void removeOffer(DynamicOffers* offers, char* dest, int dep_date); //we remove by this
//updates an Offer in the list, identified by dest and departure date
int updateOffer(DynamicOffers* offers, Offer* o);

//returns a pointer to DynamicOffers structure which contains element whose destination equal with the given destination
DynamicOffers* listByDestination(DynamicOffers* offers, char* dest);

//returns a pointer to a DynamicOffers structure which contains only those elements where the given type is a substring
//of the element type and the element's date is after the given date
DynamicOffers* listByTypeAndDate(DynamicOffers* offers, char* type, int date);

//returns a pointer to our offers structure, containing all the offers(elements)
Offer* getAll(DynamicOffers* offers);

//check if given offer is unique (based on destination and dep_date)
//0 if so
//-1 otherwise
int checkUnique(DynamicOffers* offers, Offer* o);