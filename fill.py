import os
import sys
from PIL import Image as pmg
import numpy as np
import imageio as io
import json

timgs = sys.argv[1] # item
back = sys.argv[2] # img
out = sys.argv[3]
jsons = sys.argv[4]
ox = int(sys.argv[5])
oy = int(sys.argv[6])
field = sys.argv[7]

bd = os.listdir(back)
td = os.listdir(timgs)

for n in range(len(bd)):
	chosen_item_index = np.random.randint(len(td)) # 0 - 3
	character = pmg.open(back+bd[n])
	item = pmg.open(timgs+td[chosen_item_index])
	character.paste(item,(ox,oy),mask=item)
	io.imwrite("{}{}".format(out,bd[n]),character)
	j = open("{}{}.json".format(jsons,bd[n].split(".")[0]),"r")
	content = json.load(j)
	j.close()
	val = ""
	name = td[chosen_item_index].split(".")[0]
	if len(name.split("_")) > 1:
		name_arr = name.split("_")
		for v in name_arr:
			val+=v
			if name_arr.index(v) != len(name_arr)-1:
				val+=" "
	else:
		val=name
	arg = {"trait_type": field, "value": val}
	content["attributes"].append(arg)
	r = open("{}{}.json".format(jsons,bd[n].split(".")[0]),"w")
	json.dump(content,r)
	r.close()
