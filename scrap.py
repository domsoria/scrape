#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

a_prezzo=[]
a_locali=[]
a_m2superficie=[]
a_bagni=[]
a_piano=[]

NUMERO_DI_PAGINE=500

for index in range(0,NUMERO_DI_PAGINE,1):
	print (index)
	page = 'https://www.immobiliare.it/vendita-case/milano/?pag='+str(index)
	web_result = requests.get(page).text
	soup = BeautifulSoup(web_result,'lxml')
	for ul in soup.findAll('ul',{'class':'listing-features list-piped'}):
		li=ul.findAll('li',{'class':'lif__item'});		
		
		try:
			prezzo=str(li[0].text).strip()
		except Exception as e:
			prezzo="ND"

		
		try:
			locali=str(li[1].span.text).strip()
		except Exception as e:
			locali="ND"

		try:
			m2superficie=str(li[2].span.text).strip()
		except Exception as e:
			m2superficie="ND"

		
		try:
			bagni=str(li[3].span.text).strip()
		except Exception as e:
			bagni="ND"
		

		try:
			piano=(li[4].abbr.text).strip()
		except Exception as e:
			piano="ND"
	
		a_prezzo.append(prezzo)
		a_locali.append(locali)
		a_m2superficie.append(m2superficie)
		a_bagni.append(bagni)
		a_piano.append(piano)

		print("prezzo: " + prezzo)
		print("locali: " + locali)
		print("m2superficie: " + m2superficie)
		print("bagni: " + bagni)
		print("piano: " + piano)

		print("************************************************************")

df = pd.DataFrame({'prezzo': a_prezzo,
                   'locali': a_locali,
                   'm2superficie': a_m2superficie,
                   'bagni' : a_bagni,
                   'piano' : a_piano})

df.to_csv('./dataset.csv')