import sys
import json
import os
import numpy as np

meta = sys.argv[1]

characters = ["AA","BB"]

combn = []

def run():
	ment = {
		"aaa":"000",
    "bbb":"000"
	}
	for k in ment:
		a = str(np.random.randint(4))
		b = str(np.random.randint(4))
		c = str(np.random.randint(4))
		f = a+b+c
		ment.update({k:f})
	return ment

while len(combn) != len(characters):
	grp = [characters[len(combn)],run()]
	combn.append(grp)

span = 819203213-0+1

start = 0

c = 0 

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	actor = content["attributes"][0]["value"]
	back = content["attributes"][1]["value"]
	index = characters.index(actor)
	set_val = combn[index][1]
	content["attributes"][6]["value"]=str(set_val[back])
	r = open("{}{}.json".format(meta,start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
