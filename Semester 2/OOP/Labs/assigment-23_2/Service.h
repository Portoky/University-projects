//
// Created by User on 3/12/2023.
//

#pragma once
#ifndef ASSIGMENT_23_2_SERVICE_H
#define ASSIGMENT_23_2_SERVICE_H

#endif //ASSIGMENT_23_2_SERVICE_H
#include "DynamicOffers.h"

typedef struct
{
    DynamicOffers* offers;
    DynamicOffers* history[100];
    int pos;
    int maxpos;
    int before_undo;
}Service;

Service* createService(DynamicOffers* offers);

void destroyService(Service* service);
//creates an offer from the given parameter(type, destination, dep_date, price) and add it to the list of offers
//returns 0 if succesful
//          -1 otherwise
int addOfferService(Service* service, char* type, char* destination, int dep_date, int price);
//removes an offer from the list identified by destination or departure date + decreases the nm_of_elems
void removeOfferService(Service * service, char* dest, int dep_date);
//updates an Offer in the list, identified by dest and departure date
int updateOfferService(Service* service, char* type, char* destination, int dep_date, int price);
//returns a pointer to DynamicOffers structure which contains element whose destination equal with the given destination
DynamicOffers* listByDestinationService(Service* service, char* dest);
//returns a pointer to a DynamicOffers structure which contains only those elements where the given type is a substring
//of the element type and the element's date is after the given date
DynamicOffers* listByTypeAndDateService(Service* service, char* type, int date);
//returns a pointer to our offers structure, containing all the offers(elements)
Offer* getAllService(Service* service);
//
void save(Service* service);
//
int undoService(Service* service);
//
int redoService(Service* service);