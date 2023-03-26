#pragma once
#include "Repository.h"

typedef struct {
	Repository* repo;
}Service;

Service* createService(Repository*);

void destroyService(Service*);

Planet* sameTypePlanets(Service* service, char* type, int* size);

int addPlanetService(Service*, char*, char*, double);
