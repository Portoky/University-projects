#define _CRTDBG_MAP_ALLOC
#include <stdio.h>
#include <stdlib.h>
#include <crtdbg.h>
#include <assert.h>
#include <string.h>
#include "DynamicArray.h"
#include "Offers.h"
#include "Repo.h"
#include "Service.h"
#include "Ui.h"

void test()
{
	//test;
	Service* service = createService();
	addOfferService(service, "seaside", "Norvegia", 1, 500);
	addOfferService(service, "seaside", "Korzika", 5, 1000);
	addOfferService(service, "mountain", "Slovenia", 23, 1250);
	addOfferService(service, "mountain", "Korzika", 25, 804);
	addOfferService(service, "citybreak", "Britain", 20, 600);
	assert(getLength(getAllService(service)) == 5);
	removeOfferService(service, "Slovenia", 23);
	assert(getLength(getAllService(service)) == 4);
	undo(service);
	assert(getLength(getAllService(service)) == 5);
	redo(service);
	assert(getLength(getAllService(service)) == 4);
	updateOfferService(service, "mountain", "Norvegia", 1, 1000);
	assert(strcmp(getType(get(getAllService(service), 0)), "mountain") == 0);
	undo(service);
	assert(getPrice(get(getAllService(service), 0)) == 500);
	DynamicArray* list = listByDestinationService(service, "Korzika");
	assert(getLength(list) == 2);
	list = listByTypeAndDateService(service, "mountain", 24, 1);
	assert(getLength(list) == 1);

	destroyService(service);
}

int main()
{
	test();
	//printf("%d %d %s %s", getDepDate(get(res2, 0)), getPrice(get(res2, 0)), getType(get(res2, 0)), getDestination(get(res2, 0)));
	//testDynamicArray(); 
	//createRepository();
	//_CrtSetDbgFlag ( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF );
	Service* service = createService();
	Ui* ui = createUi(service);
	startMenu(ui);
	destroyUi(ui);
	//int* p = malloc(sizeof(int) * 100);
	_CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_DEBUG);
	_CrtDumpMemoryLeaks();

}