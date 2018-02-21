#! /usr/bin/env python3
from pohovor import slovo 
from pohovor import pismeno

def spocitej_pismenko(slovo, pismeno):
	pismeno = pismeno.lower()
	slovo = slovo.lower()
	print("Ve slově",slovo," je pismeno",pismeno," {}krát".format(slovo.count(pismeno)))
	return("")
print(spocitej_pismenko(slovo, pismeno))
