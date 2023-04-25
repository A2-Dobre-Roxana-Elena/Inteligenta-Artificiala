#include "Transfer.h"
#include <iostream>

bool Transfer::transferare(Recipient sursa, Recipient destinatie, int nrLitri)
{
	bool ok1,ok2 = true;
	ok1 = sursa.extragereApa(nrLitri);
	if (!ok1)
	{
		std::cout << "Nu puteti extrage din vasul sursa litrii solicitati!!!";
		return false;
	}
	ok2 = destinatie.adaugareApa(nrLitri);
	if (!ok2)
	{
		std::cout << "Nu puteti adauga atat de multi litri in vasul solicitat";
		return false;
	}
	return true;
}