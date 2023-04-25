#include "Stare.h"
#include <iostream>


Stare::Stare(int k)
{
	this->capDorita = k;
}

bool Stare::eFinala(Recipient *x, Recipient *y)
{
	if (x->stare_curenta == capDorita || y->stare_curenta == capDorita)
		return true;
	else
		return false;
}

void Stare::eInitiala(Recipient *x, Recipient *y)
{
	x->stare_curenta = 0;
	y->stare_curenta = 0;
}

bool Stare::transferare(Recipient *sursa, Recipient *destinatie)					/// returneaza 0 daca nu e stare finala, 1 daca e finala
																					////TREBUIE SA RETURNEZE DOAR STARILE
{
	int nrLitri;
	if (destinatie->capacitate - destinatie->stare_curenta < sursa->stare_curenta)
		nrLitri = destinatie->capacitate - destinatie->stare_curenta;
	else
		nrLitri = sursa->stare_curenta;
	sursa->extragereApa(nrLitri);
	destinatie->adaugareApa(nrLitri);
	if (eFinala(sursa, destinatie))
	{
		std::cout << "am ajuns in starea finala"<<std::endl;
		return true;
	}
	return false;
}

void Stare::afisareStari(Recipient* x, Recipient* y)
{
	std::cout << "(" <<x->stare_curenta<< "," << y->stare_curenta<< ")" << std::endl;
}



/*
in transferare::
bool ok1, ok2 = true;
	ok1 = sursa->extragereApa(nrLitri);
	if (!ok1)
	{
		std::cout << "Nu puteti extrage din vasul sursa litrii solicitati!!!";
		return false;
	}
	ok2 = destinatie->adaugareApa(nrLitri);
	if (!ok2)
	{
		std::cout << "Nu puteti adauga atat de multi litri in vasul solicitat";
		return false;
	}*/