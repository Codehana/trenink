#! /usr/bin/env python3

vety = input("Zadejte věty, které mají být rozděleny: ")

def rozdel_vety(vety):
	print()
	if "." in vety:
		print(vety.split("."))
	return""
print(rozdel_vety(vety))
