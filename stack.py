import os
import sys
from PIL import Image as pmg
import numpy as np
import imageio as io
import json

timgs = sys.argv[1]
back = sys.argv[2]
out = sys.argv[3]
limit = sys.argv[4]

bd = os.listdir(back)
td = os.listdir(timgs)
up = int(limit)

for k in range(len(td)):
	c = 0
	num = np.random.randint(1,101)
	while c != num:
		if len(os.listdir(out))==up:
			break
		i = np.random.randint(len(bd))
		t = pmg.open(timgs+td[k])
		f = pmg.open(back+bd[i])
		f.paste(t,(0,0),mask=t)
		io.imwrite("./out/{}.png".format(len(os.listdir(out))),f)
		j = open("./jsons/{}.json".format(len(os.listdir(out))-1),"r")
		content = json.load(j)
		j.close()
		text = " ".join(bd[i].split("_")).split(".png")[0]
		content["attributes"][1]["value"]=str(text)
		r = open("./jsons/{}.json".format(len(os.listdir(out))-1),"w")
		json.dump(content,r)
		r.close()
		c+=1
	if len(os.listdir(out))==up:
			break
