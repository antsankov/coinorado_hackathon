#!/usr/bin/python
# -*- coding: latin-1 -*-

import random
import blockchain.exchangerates
import datetime


#returns a value indicating the number of satoshis a user specified. 
#if it returns -1, an invalid amount / character was input
def get_satoshis(string, debug = False):
	print "{0} - ".format(string)
	#satoshis per bitcoin
	spb = 100000000
	#if the string is a solid amount
	if(string.isdigit()):
		int(string)
		if(string > 0):
			return string
		else:
			return -1
	#get the prefered character
	c = string[0]
	#get the amount
	string = string[1:]
	#if it is
	ccy = ''
	if(string.isdigit()):
		int(string)
		if(string > 0):
			return string
		else:
			return -1
		if(c == 'b'):
			return string * spb
		elif(c == '$'):
			ccy = USD
		# elif(c == '£'):
		# 	ccy = GPB
		# elif(c == '€'):
		# 	ccy = EUR
		# elif(c == '¥'):
		# 	ccy = JPY
		btc = blockchain.exchangerates.to_btc(ccy, string, 'c62026c6-89e3-4200-93a9-f51250ad1ea5')
		return btc * spb
	return -1
# def test():
# 	print get_satoshis("20",True)
# 	print get_satoshis("20.0",True)
# 	print get_satoshis("-20",True)
# 	print get_satoshis("b20",True)
# 	print get_satoshis("$20",True)
# 	print get_satoshis("£20",True)
# 	print get_satoshis("€20",True)
# 	print get_satoshis("¥20",True)
# 	print get_satoshis("$-20",True)
# 	print get_satoshis("£-20",True)
# 	print get_satoshis("€-20",True)
# 	print get_satoshis("¥-20",True)
# 	print get_satoshis("£-5.55",True)
# 	print get_satoshis("$-5.55",True)
# 	print get_satoshis("€-5.55",True)
# 	print get_satoshis("¥-5.55",True)



