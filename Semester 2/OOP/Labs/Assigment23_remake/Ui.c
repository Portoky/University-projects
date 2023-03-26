#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include "Ui.h"

Ui* createUi(Service* service)
{
    Ui* newUi = malloc(sizeof(Ui));
    newUi->service = service;
    return newUi;
}

void destroyUi(Ui* ui) {
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
    printf("\t9. Search by type\n");
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
            char date_s[20];
            char price_s[20];
            printf("Please input - type, destination, departure date, price: ");
            scanf("%s %s %s %s", type, dest, date_s, price_s);
            int date = atoi(date_s);
            if (date == 0)
            {
                printf("Invalid date\n");
                break;
            }
            int price = atoi(price_s);
            if (price <= 0)
            {
                printf("Invalid price\n");
                break;
            }
            if (strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
            {
                printf("Wrong type!\n");
                break;
            }
            if (date < 1 || date > 31) {
                printf("Invalid date\n");
                break;
            }
            
            int result = addOfferService(ui->service, type, dest, date, price);
            if (result != 0)
                printf("Something is bad\n");

            break;
        }
        case 2:
        {
            char dest[20];
            char date_s[20];
            printf("Please input - destination, date: ");
            scanf("%s %s", dest, date_s);
            int date = atoi(date_s);
            if (date == 0) {
                printf("Invalid date\n");
                break;
            }
            if (date < 1 || date > 31) {
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
            char date_s[20];
            char price_s[20];
            printf("Please input - type, destination, departure date, price: ");
            scanf("%s %s %s %s", type, dest, date_s, price_s);
            int date = atoi(date_s);
            if (date == 0)
            {
                printf("Invalid date\n");
                break;
            }
            if (date < 1 || date > 31) {
                printf("Invalid date\n");
                break;
            }
            int price = atoi(price_s);
            if (price <= 0)
            {
                printf("Invalid price\n");
                break;
            }
            if (strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
            {
                printf("Wrong type!\n");
                break;
            }
            
            int res = updateOfferService(ui->service, type, dest, date, price);
            if (res != 0)
                printf("Offer not found\n");
            break;
        }
        case 4: {
            char dest[20];
            printf("Type in the destination: ");
            scanf("%s", dest);
            DynamicArray* list = listByDestinationService(ui->service, dest);
            if (getLength(list) == 0) {
                printf("No such offer found\n");
                break;
            }
            for (int i = 0; i < getLength(list); ++i)
            {
                printf("%s : %s : %d : %d \n", getType(get(list, i)), getDestination(get(list, i)), getDepDate(get(list, i)), getPrice(get(list, i)));
            }
            break;
        }
        case 5: {
            char type[20];
            char date_s[20];
            printf("Please type in the type and date: ");
            scanf("%s %s", type, date_s);
            char decision_s[20];
            printf("Ascending or descending order by price (1/2): ");
            scanf("%s", decision_s);

            int decision = atoi(decision_s);
            int date = atoi(date_s);
            if (date < 1 || date > 31) {
                printf("Invalid date\n");
                break;
            }
            if (decision < 1 || decision > 2)
            {
                printf("Invalid decision\n");
                break;
            }
            if (strcmp(type, "seaside") != 0 && strcmp(type, "mountain") != 0 && strcmp(type, "citybreak") != 0)
            {
                printf("Wrong type!\n");
                break;
            }
            
            else {
                DynamicArray* list = listByTypeAndDateService(ui->service, type, date, decision);
                if (getLength(list) == 0) {
                    printf("No such offer found\n");
                    break;
                }
                for (int i = 0; i < getLength(list); ++i)
                {
                    printf("%s : %s : %d : %d \n", getType(get(list, i)), getDestination(get(list, i)), getDepDate(get(list, i)), getPrice(get(list, i)));
                }
                break;
            }
        }
        case 6:
        {
            int res = undo(ui->service);
            if (res != 0)
                printf("Nothing to undo!\n");
            break;
        }
        case 7:
        {
            int res = redo(ui->service);
            if (res != 0)
                printf("Nothing to redo!\n");
            break;
        }
        case 8:
        {
            DynamicArray* list = getAllService(ui->service);
            for (int i = 0; i < getLength(list); ++i) {
                printf("%s : %s : %d : %d \n", getType(get(list, i)), getDestination(get(list, i)), getDepDate(get(list, i)), getPrice(get(list, i)));
            }
            break;
        }
        case 9:
        {
            char type[20];
            printf("Type in the type: ");
            scanf("%s", type);
            DynamicArray* list = listByTypeService(ui->service, type);
            for (int i = 0; i < getLength(list); ++i) {
                printf("%s : %s : %d : %d \n", getType(get(list, i)), getDestination(get(list, i)), getDepDate(get(list, i)), getPrice(get(list, i)));
            }
            break;
        }
        default:
            break;
        }

    }
}