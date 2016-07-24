from hypergeometric import *
print("Enter Database \n MSigDB ? y/N")
dec = raw_input()
print("Input format\n 1. Entrez ID \n 2. Entrez Name\n Press 1 or 2")
fr = raw_input()
print("Enter Input Filename")
inp = raw_input()
if dec == 'y' or dec == 'Y':
	if fr == '1':
		enrichment("c2.all.v5.1.entrez.gmt",inp)
	elif fr == '2':
		enrichment("c2.all.v5.1.symbols.gmt",inp)
	else:
		pass
	print("Enrichment Process Done")
	print("*************************************************************************************************")

else:
	print(" Enter Correct Database ")

