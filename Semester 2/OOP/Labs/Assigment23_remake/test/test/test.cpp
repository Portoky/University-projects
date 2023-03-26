#include <string.h>
#include "pch.h"
#include "CppUnitTest.h"
#include "../../Service.h"
#include "../../DynamicArray.h"
#include "../../Repo.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace assigment23test
{
	TEST_CLASS(assigment23test)
	{
	public:

		TEST_METHOD(TestMethod1)
		{
			Service* service = createService();
			addOfferService(service, "seaside", "Norvegia", 1, 500);
			addOfferService(service, "seaside", "Korzika", 5, 1000);
			addOfferService(service, "mountain", "Slovenia", 23, 1250);
			addOfferService(service, "mountain", "Korzika", 25, 804);
			addOfferService(service, "citybreak", "Britain", 20, 600);
			//assert(getLength(getAllService(service)) == 5);
			Assert::AreEqual(getLength(getAllService(service)), 5);
			removeOfferService(service, "Slovenia", 23);
			//assert(getLength(getAllService(service)) == 4);
			Assert::AreEqual(getLength(getAllService(service)), 4);
			undo(service);
			Assert::AreEqual(getLength(getAllService(service)), 5);
			redo(service);
			//assert(getLength(getAllService(service)) == 4);
			Assert::AreEqual(getLength(getAllService(service)), 4);
			updateOfferService(service, "mountain", "Norvegia", 1, 1000);
			//assert(strcmp(getType(get(getAllService(service), 0)), "mountain") == 0);
			//Assert::AreEqual(strcmp(getType(get(getAllService(service), 0)), "mountain"), 0);
			undo(service);
			//assert(getPrice(get(getAllService(service), 0)) == 500);
			DynamicArray* list = listByDestinationService(service, "Korzika");
			//assert(getLength(list) == 2);
			list = listByTypeAndDateService(service, "mountain", 24, 1);
			//assert(getLength(list) == 1);

			destroyService(service);
		}
	};
}
