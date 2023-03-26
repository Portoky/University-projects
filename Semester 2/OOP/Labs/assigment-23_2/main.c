#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include "Offers.h"
#include "DynamicOffers.h"
#include "Service.h"
#include "ui.h"
#include <assert.h>
#include <crtdbg.h>

void test()
{
    DynamicOffers* offers = CreateDynamicOffers(2);
    assert(getCapacity(offers) == 2);
    assert(getLength(offers) == 0);

    Offer* o = createOffer("seaside", "Korzika", 15, 1000);
    Offer* o2 = createOffer("seaside", "Korzika", 16, 500);
    Offer* o3 = createOffer("seaside", "Romania", 15, 100);
    Offer* o4 = createOffer("seaside", "Korzika", 15, 1200);
    assert(o->price == 1000);

    Service* service = createService(offers);
    int res;
    res = addOfferService(service, "seaside", "Korzika", 15, 1000);
    assert(res == 0);
    res = addOffer(offers, o);
    assert(res == -1);
    res = addOffer(offers, o4);
    assert(res == -1);
    res = addOffer(offers, o2);
    assert(res == 0);
    res = addOffer(offers, o3);
    assert(res == 0);
    printf("%s\n", offers->elems[0].destination);
    printf("%s\n", offers->elems[1].destination);
    printf("%s\n", offers->elems[2].destination);

    //printf("%d", getCapacity(offers));
    assert(getCapacity(offers) == 4);
    //addOffer(offers, o4);
    assert(getLength(offers) == 3);
    removeOffer(offers, "Romania", 15);
    assert(getLength(offers) == 2);
    DynamicOffers* list = listByDestination(offers, "Korzika");
    //assert(getOffer(list, 1) == o2);
    printf("%d\n", list->elems[0].price);
    printf("%d\n", list->elems[1].price);
    printf("%d\n", list->elems[2].price);
    destroyOffers(offers);
}

int main()
{

    test();
    DynamicOffers* offers = CreateDynamicOffers(2);
    Service* service = createService(offers);
    Ui* ui = createUi(service);
    startMenu(ui);
    destroyUi(ui);
    _CrtDumpMemoryLeaks();
}