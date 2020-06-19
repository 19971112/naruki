# -*- coding: utf-8 -*-

f1 = open ("countrypart.txt","r")
f2 = open ("abbreviation.txt","r")

#Set dict
country_list=[]
abbreviation_list=[]
seq_abb_list=[]

for line_1 in f1:

    line1 = line_1.rstrip()

    con_abb = line1.split(",")

    #print(con_abb[0])

    country_list.append(con_abb[1])

    abbreviation_list.append(con_abb[0])

#print(country_list)

#print(abbreviation_list)

 
for line_2 in f2:

	#print(line_2)

	line2 = line_2.rstrip()

	#print(line2)

	seq_abb_list.append(line2)

#print(seq_abb_list)

for coun, abb in zip(country_list, abbreviation_list):

	#print(coun)

	#print(abb)

	if abb == seq_abb_list:

		print(coun)


