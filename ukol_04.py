#! /usr/bin/env python3

text = input("Zadejte text: ")
slovo_1 = input("Které slovo má být nahrazeno? ")
slovo_2 = input("Kterým slovem se má nahradit? ")

def nahrad(text,slovo_1,slovo_2):
	print(text.lower().replace(slovo_1.lower(), slovo_2))
	return""
print(nahrad(text,slovo_1,slovo_2))
