import sys
import json
import os

out = sys.argv[1]
meta = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])
obj = sys.argv[5]
sand = sys.argv[6]
nion = sys.argv[7]
sory = sys.argv[8]
ture = sys.argv[9]

span = end-start+1

c = 0

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	content["attributes"][0]["value"]=str(ture)
	content["attributes"][2]["value"]=str(nion)
	content["attributes"][3]["value"]=str(sand)
	content["attributes"][4]["value"]=str(obj)
	content["attributes"][5]["value"]=str(sory)
	r = open("./jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
