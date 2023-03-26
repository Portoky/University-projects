//
// Created by User on 3/12/2023.
//
#define _CRT_SECURE_NO_WARNINGS
#include "Offers.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


Offer* createOffer(char* type, char* dest, int dep_date, int price)
{
//    if(strcmp(type, "seaside") == 0 || strcmp(type, "mountain") == 0 || strcmp(type, "city break") == 0) {
//        Offer o;
//        strcpy(o.type, type);
//        strcpy(o.destination, dest);
//        o.dep_date = dep_date;
//        o.price = price;
//        return o;
//    }
    Offer* o = malloc(sizeof(Offer));
    o->type = malloc((strlen(type)+1) * sizeof(char));
    o->destination = malloc((strlen(dest)+1) * sizeof(char));
    strcpy(o->type, type);
    strcpy(o->destination, dest);
    o->dep_date = dep_date;
    o->price = price;
    return o;
}

void destroyOffer(Offer* o)
{
    free(o->type);
    free(o->destination);
    free(o);
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
    char str[1000];
    sprintf(str, "%s %s %d %d", o->type, o->destination, o->dep_date, o->price);
    return str;
}
//int main()
//{
//    Offer o = createOffer("seaside", "Korzika", 15, 1000);
//}