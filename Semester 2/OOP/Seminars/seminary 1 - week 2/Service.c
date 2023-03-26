#include "Service.h"
#include <string.h>
#include <stdlib.h>

Service* createService(Repository* repo) {
	Service* newService = malloc(sizeof(Service));
	newService->repo = repo;
	return newService;
}

void destroyService(Service* service) {
	destroyRepository(service->repo);
	free(service);
}

Planet* sameTypePlanets(Service* service, char* type, int* size) {
	if (strcmp(type, "null") == 0) {
		*size = getSize(service->repo);
		return service->repo->data;
	}

	Planet* planets = malloc(sizeof(Planet) * 100);
	*size = 0;
	for (int i = 0; i < getSize(service->repo); i++) {
		if (strcmp(type, getType(&service->repo->data[i])) == 0) {
			planets[(*size)++] = service->repo->data[i];
		}
	}

	return planets;
}

int addPlanetService(Service* service, char* name, char* type, double distance) {
	Planet* newPlanet = createPlanet(name, type, distance);
	return addPlanet(service->repo, newPlanet);
}
