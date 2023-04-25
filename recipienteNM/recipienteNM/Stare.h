#pragma once
#include "Recipient.h"
class Stare
{
public:
	int capDorita;
	Stare(int k);
	void eInitiala(Recipient *x, Recipient *y);
	bool eFinala(Recipient *x, Recipient *y);
	bool transferare(Recipient *sursa, Recipient *destinatie);
	void afisareStari(Recipient* x, Recipient* y);
};

