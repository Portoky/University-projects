#include "planet.h"
#include <stdio.h>
#include <stdlib.h>

Planet* createPlanet(char* name, char* type, double dist)
{
	Planet* newPlanet = malloc(sizeof(Planet));
	newPlanet->name = malloc((strlen(name)+1)*sizeof(char));
	newPlanet->type = malloc((strlen(type) + 1) * sizeof(char));
	strcpy(newPlanet->name, name);
	strcpy(newPlanet->type, type);
	newPlanet->distanceFromEarth = dist;
	return newPlanet;
}

void destroyPlanet(Planet* planet)
{
	free(planet->name);
	free(planet->type);
	free(planet);
}


char* getName(Planet* planet) {
	return planet->name;
}

char* getType(Planet* planet) {
	return planet->type;
}

double getDistanceFromEarth(Planet* planet) {
	return planet->distanceFromEarth;
}

char* toString(Planet* planet) {
	char str[1000];
	sprintf(str, "%s %s %lf", planet->name, planet->type, planet->distanceFromEarth);
	return str;
}
