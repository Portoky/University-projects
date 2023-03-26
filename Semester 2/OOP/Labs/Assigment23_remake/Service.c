#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include "Service.h"


void save(Service* service)
{
	Repository* saveRepo = createRepository();
	for (int i = 0; i < getLength(getAllRepo(service->repo)); ++i)
	{
		addOfferRepo(saveRepo, get(getAllRepo(service->repo), i));
	}
	service->history->length = service->pos;
	add(service->history, saveRepo);
	++service->pos;
	service->maxpos = service->pos;
	
}
/*
void save2(Service* service, char* instruction, char* type1, char* type2, int price1, int price2, int dep_date, char* dest)
{
	Command* previous_command = createCommand(instruction, type1, type2, price1, price2, dep_date, dest);
	add(service->history, previous_command);
	++service->pos;
	if (service->pos > service->maxpos)
		service->maxpos = service->pos;
}*/


Service* createService()
{
	Service* newService = malloc(sizeof(Service));
	newService->repo = createRepository();
	newService->history = createDynamicArray(10, destroyRepository);
	newService->pos = 0;
	newService->maxpos = -1;
	return newService;
}

void destroyService(Service* service)
{
	free(service->history);
	destroyRepository(service->repo);
	free(service);
}

int addOfferService(Service* service, char* type, char* destination, int dep_date, int price)
{
	save(service);
	//save2(service, "add", type, NULL, price, -1, dep_date, destination);
	Offer* newOffer = createOffer(type, destination, dep_date, price);
	return addOfferRepo(service->repo, newOffer);
}

int removeOfferService(Service* service, char* dest, int dep_date)
{
	save(service);
	//save2(service, "remove", NULL, NULL, -1, -1, dep_date, dest);
	return removeOfferRepo(service->repo, dest, dep_date);
}

int updateOfferService(Service* service, char* type, char* destination, int dep_date, int price)
{
	save(service);
	/*int pos = findOfferRepo(service->repo, destination, dep_date);
	if(pos != -1)
		save2(service, "update", getType(get(getAllRepo(service->repo), pos)), type, getPrice(get(getAllRepo(service->repo), pos)), price ,getDepDate(get(getAllRepo(service->repo), pos)), getDestination(get(getAllRepo(service->repo), pos)));
	*/
	Offer* newOffer = createOffer(type, destination, dep_date, price);
	return updateOfferRepo(service->repo, newOffer);
}

DynamicArray* listByTypeService(Service* service, char* type)
{
	return listByTypeRepo(service->repo, type);
}

DynamicArray* listByDestinationService(Service* service, char* dest)
{
	return listByDestinationRepo(service->repo, dest);
}

DynamicArray* listByTypeAndDateService(Service* service, char* type, int date, int decision)
{
	return listByTypeAndDateRepo(service->repo, type, date, decision);
}

DynamicArray* getAllService(Service* service)
{
	return getAllRepo(service->repo);
}

Command* createCommand(char* instruction, char* type1, char* type2, int price1, int price2, int dep_date, char* dest)
{
	Command* command = malloc(sizeof(Command));
	command->command = malloc(sizeof(instruction));
	command->type1 = malloc(sizeof(type1));
	command->type2 = malloc(sizeof(type2));
	command->dest = malloc(sizeof(dest));
	strcpy(command->command, instruction);
	strcpy(command->type1, type1);
	strcpy(command->type2, type2);
	strcpy(command->dest, dest);
	command->dep_date = dep_date;
	command->price1 = price1;
	command->price2 = price2;

	return command;
}

int undo(Service* service)
{
	//printf("%d %d \n", service->pos, service->maxpos);
	if (service->pos == getLength(service->history)) //in case we undo first time we need to save the state to redo it later, otherwise its lost;
	{
		save(service);
		--service->pos;
		service->maxpos = service->pos;
	}
	--service->pos;
	if (service->pos < 0)
	{
		++service->pos;
		return 1;
	}
	DynamicArray* repo2 = get(service->history, service->pos);

	service->repo = get(service->history, service->pos);
	return 0;
}

int redo(Service* service)
{
	//printf("%d %d \n", service->pos, service->maxpos);
	if (service->pos >= service->maxpos)
		return 1;
	++service->pos;
	service->repo = get(service->history, service->pos);
	return 0;

}
/*
int undo2(Service* service)
{
	if (service->pos == service->maxpos) //in case we undo first time we need to save the state to redo it later, otherwise its lost;
	{
		save2(service,);
		--service->pos;
		service->maxpos = service->pos;
	}
	--service->pos;
	if (service->pos < 0)
	{
		++service->pos;
		return 1;
	}
	Command* operation = get(service->history, service->pos);
	if (strcmp(getCommand(operation), "remove") == 0)
	{
		addOfferService(service, operation->type1, operation->dest, operation->dep_date, operation->price1);
	}
	else if (strcmp(getCommand(operation), "add") == 0)
	{
		removeOfferService(service, operation->dest, operation->dep_date);
	}
	else if (strcmp(getCommand(operation), "update") == 0)
	{
		updateOfferService(service, operation->type1, operation->dest, operation->dep_date, operation->price1);
	}
	return 0;
}

int redo2(Service* service)
{
	if (service->pos >= service->maxpos)
		return 1;
	++service->pos;
	Command* operation = get(service->history, service->pos);
	if (strcmp(getCommand(operation), "remove") == 0)
	{
		//OfferService(service, operation->type1, operation->dest, operation->dep_date, operation->price1);
		removeOfferService(service, operation->dest, operation->dep_date);
	}
	else if (strcmp(getCommand(operation), "add") == 0)
	{
		addOfferService(service, operation->type1, operation->dest, operation->dep_date, operation->price1);
	}
	else if (strcmp(getCommand(operation), "update") == 0)
	{
		updateOfferService(service, operation->type2, operation->dest, operation->dep_date, operation->price2);
	}
	return 0;
}

char* getCommand(Command* operation)
{
	return operation->command;
}
*/