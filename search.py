import sys
import json
import os

out = sys.argv[1]
meta = sys.argv[2]
field = int(sys.argv[3])
value = sys.argv[4]

span = 28000

c = 0

while c != span:
	j = open("{}{}.json".format(meta,c),"r")
	content = json.load(j)
	j.close()
	if value in content["attributes"][field]["value"]:
		print(c)
	c+=1
