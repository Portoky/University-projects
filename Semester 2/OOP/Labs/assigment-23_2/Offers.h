//
// Created by User on 3/12/2023.
//
#pragma once
#ifndef A23_PORTOKY_OFFER_H
#define A23_PORTOKY_OFFER_H

#endif //A23_PORTOKY_OFFER_H


typedef struct
{
    char* type;
    char* destination;
    int dep_date;
    int price;
}Offer;

Offer* createOffer(char* type, char* dest, int dep_date, int price);

void destroyOffer(Offer* o);

char* getType(Offer* o);

char* getDestination(Offer* o);

int getDepDate(Offer* o);

int getPrice(Offer* o);

char* toString(Offer* o);