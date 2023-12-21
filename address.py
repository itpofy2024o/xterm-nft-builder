import sys
import json
import os

meta = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

span = end-start+1

c = 0 # 92

while c != span:
	j = open("./assets/jsons/{}.json".format(start),"r")
	content = json.load(j)
	j.close()
	content["properties"]["creators"][0]["address"]=str("")
	r = open("./assets/jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
