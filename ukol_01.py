#! /usr/bin/env python3

slovo = input("Jaké slovo se má spočítat? ")
pismeno = input("Jaké písmeno se má spočítat? ")

def spocitej_pismenko(slovo, pismeno):
	pismeno = pismeno.lower()
	slovo = slovo.lower()
	print("Ve slově",slovo," je pismeno",pismeno," {}krát".format(slovo.count(pismeno)))
	return("")
print(spocitej_pismenko(slovo, pismeno))
