#pragma once

typedef struct  {
	char* name;
	char* type;
	double distanceFromEarth;
}Planet;


Planet* createPlanet(char* name, char* type, double dist);

void destroyPlanet(Planet* planet);

char* getName(Planet*);

char* getType(Planet*);

double getDistanceFromEarth(Planet*);

char* toString(Planet*);

