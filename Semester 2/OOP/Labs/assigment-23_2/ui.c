//
// Created by User on 3/12/2023.
//
#define _CRT_SECURE_NO_WARNINGS
#include "ui.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

Ui* createUi(Service* service)
{
    Ui* newUi = malloc(sizeof(Ui));
    newUi->service = service;
    return newUi;
}

void destroyUi(Ui* ui){
    destroyService(ui->service);
    free(ui);
}

void printMenu()
{
    printf("Menu:\n");
    printf("\t1. Add offer\n");
    printf("\t2. Remove offer\n");
    printf("\t3. Update offer\n");
    printf("\t4. Search by destination\n");
    printf("\t5. Search by type and after a given date\n");
    printf("\t6. Undo last operation\n");
    printf("\t7. Redo last operation\n");
    printf("\t8. Get all offers\n");
    printf("\t0. Exit\n");
}

void startUp(Ui* ui)
{
    addOfferService(ui->service, "seaside", "Norvegia", 1, 500);
    addOfferService(ui->service, "seaside", "Romania", 1, 500);
    addOfferService(ui->service, "seaside", "Korzika", 5, 1000);
    addOfferService(ui->service, "mountain", "Slovenia", 23, 1250);
    addOfferService(ui->service, "mountain", "Korzika", 25, 804);
    addOfferService(ui->service, "citybreak", "Britain", 20, 600);
    addOfferService(ui->service, "citybreak", "Romania", 19, 7000);
    addOfferService(ui->service, "mountain", "France", 27, 900);
    addOfferService(ui->service, "mountain", "Romania", 30, 103);
    addOfferService(ui->service, "seaside", "Italy", 31, 999);
    addOfferService(ui->service, "seaside", "Spain", 15, 1423);
}

void startMenu(Ui* ui)
{
    startUp(ui);
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
                char type[20];
                char dest[20];
                int date;
                int price;
                printf("Please input - type, destination, departure date, price: ");
                scanf("%s %s %d %d", type, dest, &date, &price);
                if(strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
                {
                    printf("Wrong type!\n");
                    break;
                }
                if(date < 1 || date > 31) {
                    printf("Invalid date\n");
                    break;
                }
                if (price < 0)
                {
                    printf("Invalid price\n");
                    break;
                }
                int result = addOfferService(ui->service, type, dest, date, price);
                if(result != 0)
                    printf("Something is bad\n");

                break;
            }
            case 2:
            {
                char dest[20];
                int date;
                printf("Please input - destination, date: ");
                scanf("%s %d", dest, &date);
                if(date < 1 || date > 31) {
                    printf("Invalid date\n");
                    break;
                }
                removeOfferService(ui->service, dest, date);
                break;
            }
            case 3:
            {
                char type[20];
                char dest[20];
                int date;
                int price;
                printf("Please input - type, destination, departure date, price: ");
                scanf("%s %s %d %d", type, dest, &date, &price);
                if(strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
                {
                    printf("Wrong type!\n");
                    break;
                }
                if(date < 1 || date > 31) {
                    printf("Invalid date\n");
                    break;
                }
                if (price < 0)
                {
                    printf("Invalid price\n");
                    break;
                }
                int res = updateOfferService(ui->service, type, dest, date, price);
                if(res != 0)
                    printf("Something went wrong..");
                break;
            }
            case 4: {
                char dest[20];
                printf("Type in the destination: ");
                scanf("%s", dest);
                DynamicOffers *list = listByDestinationService(ui->service, dest);
                if (list->nm_of_elems == 0){
                    printf("No such offer found\n");
                    break;
                }
                for(int i = 0; i < list->nm_of_elems; ++i)
                {
                    printf("%s : %s : %d : %d \n", list->elems[i].type, list->elems[i].destination, list->elems[i].dep_date, list->elems[i].price);
                }
                break;
            }
            case 5:{
                char type[20];
                int date;
                printf("Please type in the type and date: ");
                scanf("%s %d", type, &date);
                if(strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
                {
                    printf("Wrong type!\n");
                }
                else if(date < 1 || date > 31) {
                    printf("Invalid date\n");
                }
                else {
                    DynamicOffers* list = listByTypeAndDateService(ui->service, type, date);
                    if (list->nm_of_elems == 0) {
                        printf("No such offer found\n");
                        break;
                    }
                    for (int i = 0; i < list->nm_of_elems; ++i)
                    {
                        printf("%s : %s : %d : %d \n", list->elems[i].type, list->elems[i].destination, list->elems[i].dep_date, list->elems[i].price);
                    }
                    break;
                }
            }
            case 6:
            {
                int res = undoService(ui->service);
                if(res != 0)
                    printf("Nothing to undo!\n");
                break;
            }
            case 7:
            {
                int res = redoService(ui->service);
                if(res != 0)
                    printf("Nothing to redo!\n");
                break;
            }
            case 8:
            {
                Offer* all = getAllService(ui->service);
                for (int i = 0; i < getLength(ui->service->offers); ++i){
                    printf("%s : %s : %d : %d \n", all[i].type, all[i].destination, all[i].dep_date, all[i].price);
                }
            }
            default:
                break;
        }

    }
}