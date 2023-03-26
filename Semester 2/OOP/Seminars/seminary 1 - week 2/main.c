#include <stdio.h>
#include <stdlib.h>
#include <crtdbg.h>
#include "Repository.h"
#include "Service.h"
#include "ui.h"

int main()
{
	Repository* repo = createRepo();
	Service* ctrl = createService(repo);
	Ui* ui = createUi(ctrl);

	startMenu(ui);
	
	destroyUi(ui);

	_CrtDumpMemoryLeaks();
	return 0;
}


