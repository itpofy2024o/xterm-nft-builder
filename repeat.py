import sys
import json
import os

out = sys.argv[1]
meta = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])
other = int(sys.argv[5])

span = end-start+1

c = 0 # 92

while c != span:
	j = open("{}{}.json".format(meta,start),"r")
	content = json.load(j)
	j.close()
	p = open("{}{}.json".format(meta,other),"r")
	othercontent = json.load(p)
	p.close()
	content["attributes"][0]["value"]=str(othercontent["attributes"][0]["value"])
	content["attributes"][2]["value"]=str(othercontent["attributes"][2]["value"])
	content["attributes"][3]["value"]=str(othercontent["attributes"][3]["value"])
	content["attributes"][4]["value"]=str(othercontent["attributes"][4]["value"])
	content["attributes"][5]["value"]=str(othercontent["attributes"][5]["value"])
	# if len(othercontent["attributes"]) > 7: # index 6
	# 	rest = len(othercontent["attributes"])
	# 	extra_index = []
	# 	difference = rest - 7
	# 	while difference != 0:
	# 		val = 7+difference-1
	# 		extra_index.append(val)
	# 		difference-=1
	# 	s = sorted(extra_index)
	# 	while len(content["attributes"]) != len(othercontent["attributes"]):
	# 		arg = {"trait_type": othercontent["attributes"][s[0]]["trait_type"],
	# 		 "value": othercontent["attributes"][s[0]]["value"]}
	# 		content["attributes"].append(arg)
	# 		s = s[0+1:]
	r = open("./jsons/{}.json".format(start),"w")
	json.dump(content,r)
	r.close()
	start+=1
	c+=1
