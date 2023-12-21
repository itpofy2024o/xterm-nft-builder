import sys
import json
import os

meta = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
name = "Exo"
sym = "E"
collection = ""
family = ""
url = ""
description = ""
compiler = ""

span = end-start+1

c = 0 

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	name_n = name + " " +content["name"].split(" ")[1]
	content["name"]=name_n
	content["symbol"]=sym
	content["description"]=description
	content["collection"]["name"]=collection
	content["collection"]["family"]=family
	content["external_url"]=url
	content["compiler"]=compiler
	print(content)
	# content["attributes"][field]["value"]=str(value)
	# r = open("./jsons/{}.json".format(start),"w")
	# json.dump(content,r)
	# r.close()
	start+=1
	c+=1
