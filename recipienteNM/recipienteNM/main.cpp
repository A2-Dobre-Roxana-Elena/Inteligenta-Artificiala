#include <iostream>
#include "Recipient.h"
#include "Stare.h"
using namespace std;

int main()
{
	int n, m,cantitateDorita;
	cout << "Introduceti capacitatile maxime ale celor doua vase, in ordine"<<endl;
	cin >> n >> m;
	cout << "Introduceti capacitatea dorita"<<endl;
	cin >> cantitateDorita;
	Recipient x(n), y(m);						///ele sunt aici doar sa mi faca mie mai clara si usoara crearea lor in Stare, eu le voi manipula din Stare de acum. Doamne Ajuta!
	Stare s(cantitateDorita);
	s.eInitiala(&x, &y);
	x.umplereApa();
	s.transferare(&x, &y);		///aici returneaza 1 fiindca ajunge in starea finala 
	s.afisareStari(&x, &y);
	//s.transferare(&y, &x);
	//s.afisareStari(&x, &y);
	return 0;
}