import random
import json

def lambda_handler(event, context):

	n = random.randint(0,16)

	return {"number": n}

def lambda_handler_2(number, event, context):

	lista_vacia = []

	for n in range(0,number):
		lista_vacia.append(n)

	return {lista_vacia}

def lambda_handler_3(number, event, context):

	newNumber = number + random.randint(0,16)
	print(number, newNumber)

	return {"number": newNumber}


def lambda_handler_4(event, context):
	print(envent)
	
	return(10)