from collections import defaultdict
from scipy.stats import hypergeom
import codecs
def database(x):
	database = {}
	database = defaultdict(list)
	glst = []
	f = codecs.open(x,'r',encoding = 'utf8')
	for i in f:
		i=i.strip()
		k=i.split("\t")
		for d in k[2:]:
			database[k[0].strip()].append(d)
			if d not in glst:
				glst.append(d)
	return database,glst

def getinput(fx):
	input = []
	fil = open(fx,'r')
	for f in fil:
		if f.strip() not in input:
			input.append(f.strip())
	return input
	
def enrichment(dbfx,inp):
	print("*************************************************************************************************")
	print("Database :"+str(dbfx))
	print("Input file:"+str(inp))
	fout = codecs.open("Enrichment_results.csv",'w',encoding = "utf8")
	fout.write("PATHWAY_NAME\tLENGTH OF PATHWAY\tINPUT_GENESET\tOVERLAPPED_GENESET\tPValue\n")
	input = []
	glst = []
	input = set(getinput(inp))
	db = {}
	db,glst = database(dbfx)
	M = len(glst)
	for d in db.keys():
		overlap = len(input.intersection(set(db[d])))
		if overlap > 0:
			ora = hypergeom(M,len(set(db[d])),len(input))
			p = ora.pmf(overlap)
#			print(str(M)+"\t"+str(len(set(db[d])))+"\t"+len(input)+"\t"+str(overlap)+str(p)+"\n")
			fout.write(str(d)+"\t"+str(len(set(db[d])))+"\t"+str(len(input))+"\t"+str(overlap)+"\t"+str(p)+"\n")	
'''
print("Enter Database \n MSigDB ? y/N")
dec = raw_input()
print("Input format\n 1. Entrez ID \n 2. Entrez Name\n Press 1 or 2")
fr = raw_input()
print("Enter Input Filename")
inp = raw_input()
if dec == 'y' or dec == 'Y':
	if fr == 1:
		enrichment("c2.all.v5.1.entrez.gmt",inp)
	elif fr == 2:
		enrichment("c2.all.v5.1.symbols.gmt",inp)
	else:
		pass
	print("Enrichment Process Done")
	print("*************************************************************************************************")

else:
	print(" Enter Correct Database ")
'''
