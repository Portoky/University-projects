#include "Repository.h"
#include <stdlib.h>

Repository* createRepo()
{
    Repository* newRepo = malloc(sizeof(Repository));
    newRepo->data = malloc(100 * sizeof(Planet));
    newRepo->size = 0;
    return newRepo;
}

void destroyRepository(Repository* repo) {
    free(repo->data);
    free(repo);
}

Planet* getAll(Repository* repo) {
    return repo->data;
}

int getSize(Repository* repo) {
    return repo->size;
}

int addPlanet(Repository* repo, Planet* newPlanet) {
    if (findPlanet(repo, newPlanet) == 1) {
        return 0;
    }

    repo->data[repo->size++] = *newPlanet;
    return 1;
}

int findPlanet(Repository* repo, Planet* planet) {
    for (int i = 0; i < repo->size; i++) {
        if (strcmp(getName(&repo->data[i]), getName(planet)) == 0) {
            return 1;
        }
    }
    return 0;
}
