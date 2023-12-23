import sys
import json
import os

out = sys.argv[1]
meta = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])
field = sys.argv[5]
value = sys.argv[6]

span = end-start+1

c = 0 

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	arg = {"trait_type": field, "value": value}
	content["attributes"].append(arg)
	# print(content)
	r = open("./jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
