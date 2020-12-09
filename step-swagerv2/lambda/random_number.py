import random
import json


def lambda_handler(event, context):

	n = random.randint(1,16)

	return {"number": n}

def lambda_handler_2(event, context):
	numbers = []

	for n in range(1,event['number']+1):
		numbers.append({"number": n})
	return {"numbers": numbers}

def lambda_handler_3(event, context):
	newNumber = event['number'] + random.randint(0,16)

	return {"number": newNumber}

def lambda_handler_4(event, context):
	
	return(10)