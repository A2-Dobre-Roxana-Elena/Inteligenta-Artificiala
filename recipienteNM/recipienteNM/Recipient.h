#pragma once
class Recipient
{
public: 
	int capacitate;
	int stare_curenta;
	Recipient(int x);
	void umplereApa();
	void golireApa();
	bool adaugareApa(int x);
	bool extragereApa(int x);
};

