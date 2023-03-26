#include "ui.h"
#include <stdio.h>
#include <stdlib.h>

Ui* createUi(Service* service) {
	Ui* newUi = malloc(sizeof(Ui));
	newUi->service = service;
	return newUi;
}

void destroyUi(Ui* ui) {
	destroyService(ui->service);
	free(ui);
}

void printMenu() {
	printf("Menu:\n");
	printf("\t1. Add planet\n");
	printf("\t2. Show all planets\n");
	printf("\t0. Exit\n");
}

void startMenu(Ui* ui) {
	while (1) {
		printMenu();
		int option;
		scanf("%d", &option);
		if (option == 0) {
			break;
		}
		switch (option)
		{
		case 1:
		{
			char name[20];
			char type[20];
			double distance;
			scanf("%s %s %lf", name, type, &distance);

			int result = addPlanetService(ui->service, name, type, distance);
			if (result == 1)
				printf("it's fine\n");
			else
				printf("it's bad\n");

			break;
		}
		case 2:
		{
			char type[20];
			int size;
			printf("Give type or 'null' if you want to list all planets: ");
			scanf("%s", type);
			Planet* planets = sameTypePlanets(ui->service, type, &size);
			for (int i = 0; i < size; i++) {
				printf("%s\n", toString(&planets[i]));
			}
			break;
		}
		default:
			break;
		}

	}
}