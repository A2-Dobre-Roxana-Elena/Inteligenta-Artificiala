#include "Recipient.h"
#include <iostream>


 Recipient::Recipient(int x)
{
	 this->capacitate=x;
	 this->stare_curenta = 0;
}

void Recipient::umplereApa()
 {
	 this->stare_curenta = capacitate;
 }

void Recipient::golireApa()
{
	this->stare_curenta = 0;
}


bool Recipient::adaugareApa(int x)
 {
	
	int posibil = this->stare_curenta + x;
	 if (posibil > this->capacitate)
		 return false;
	 else
	 {
		 this->stare_curenta = posibil;
		 return true;
	 }
 }

 bool Recipient::extragereApa(int x)
 {
	 if (this->stare_curenta < x )
		 return false;
	 else
	 {
		 this->stare_curenta -= x;
		 return true;
	 }
 }

