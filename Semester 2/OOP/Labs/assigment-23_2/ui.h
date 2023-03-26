//
// Created by User on 3/12/2023.
//

#pragma once
#ifndef ASSIGMENT_23_2_UI_H
#define ASSIGMENT_23_2_UI_H

#endif //ASSIGMENT_23_2_UI_H
#include "Service.h"

typedef struct
{
    Service* service;
}Ui;

Ui* createUi(Service* service);

void destroyUi(Ui*);

void startMenu(Ui*);

void startUp(Ui*);
