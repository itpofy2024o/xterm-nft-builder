import sys
import json
import os

out = sys.argv[1]
meta = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

ment = {
	"0":"000",
	"1":"000"
}

for k in ment:
	print(k)
	f = input("3 digits between 000 to 333: \n")
	ment.update({k:f})

span = end-start+1

c = 0 

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	back = content["attributes"][1]["value"]
	val = ment[back]
	content["attributes"][6]["value"]=str(val)
	r = open("./jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
