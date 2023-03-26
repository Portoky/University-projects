#pragma once
#include "planet.h"

typedef struct  {
	Planet* data;
	int size;

} Repository;

Repository* createRepo();

void destroyRepo(Repository*);

Planet* getAll(const Repository*);

int getSize(const Repository*);

int addPlanet(Repository*, Planet*);

