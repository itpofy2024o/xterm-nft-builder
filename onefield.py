import sys
import json
import os

meta = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
field = int(sys.argv[4])
value = sys.argv[5]

span = end-start+1

c = 0 

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	print(content)
	j.close()
	content["attributes"][field]["value"]=str(value)
	r = open("./jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
