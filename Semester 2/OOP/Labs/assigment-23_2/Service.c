//
// Created by User on 3/12/2023.
//
#define _CRT_SECURE_NO_WARNINGS
#include "Service.h"
#include <stdlib.h>
#include "stdio.h"

Service* createService(DynamicOffers* offers){
    Service* newService = malloc(sizeof(Service));
    for(int i = 0; i < 100; ++i)
        newService->history[i] = NULL;
    newService->pos = 0;
    newService->maxpos = -1;
    newService->offers = offers;
    newService->before_undo = 0;
    return newService;
}

void destroyService(Service* service){
    destroyOffers(service->offers);
    for(int i = 0; i < 100; ++i)
        destroyOffers(service->history[i]);
    free(service);
}

int addOfferService(Service* service, char* type, char* destination, int dep_date, int price)
{
    save(service);
    Offer* newOffer = createOffer(type, destination, dep_date, price);
    //printf("%s", newOffer->destination);
    return addOffer(service->offers, newOffer);
}
int updateOfferService(Service* service, char* type, char* destination, int dep_date, int price)
{
    save(service);
    Offer* alt_offer = createOffer(type, destination, dep_date, price);
    return updateOffer(service->offers, alt_offer);
}
void removeOfferService(Service * service, char* dest, int dep_date)
{
    save(service);
    removeOffer(service->offers, dest, dep_date);
}

DynamicOffers* listByDestinationService(Service* service, char* dest)
{
    return listByDestination(service->offers, dest);
}

DynamicOffers* listByTypeAndDateService(Service* service, char* type, int date)
{
    return listByTypeAndDate(service->offers, type, date);
}

Offer* getAllService(Service* service)
{
    return getAll(service->offers);
}

void save(Service* service)
{

    //printf("%d ", service->pos);
    DynamicOffers* toSave = CreateDynamicOffers(service->offers->capacity);
    toSave->capacity = service->offers->capacity;
    toSave->nm_of_elems = 0;
    for(int i = 0; i < service->offers->nm_of_elems; ++i)
        addOffer(toSave, &service->offers->elems[i]);
    service->history[service->pos] = toSave;
    if(service->pos > service->maxpos)
        service->maxpos = service->pos;
    ++service->pos;
    service->before_undo = 0;
}

int undoService(Service* service)
{
    if(service->before_undo == 0) {
        save(service);
        --service->pos;
        service->before_undo = 1;
    }

    //printf("%d %d\n", service->pos, service->maxpos);

    if(service->pos > 0)
    {
        --service->pos;
        service->offers = service->history[service->pos];

        return 0;
    }
    return -1;
}

int redoService(Service* service) {
    //printf("%d %d \n", service->pos, service->maxpos);

    ++service->pos;
    if (service->history[service->pos] == NULL) {
        --service->pos;
        return -1;
    }
    service->offers = service->history[service->pos];

    //printf("%p", service->offers);
    return 0;
}