import json as sj
import sys as ysy

start = int(ysy.argv[1])
end = int(ysy.argv[2])
name = ysy.argv[3]

var_s = []

for i in range(start,end+1):
    record = open("./jsonfolder/{}.json".format(i),"r")
    content = sj.load(record)
    record.close()
    var_s.append(content)

lists = [sj.dumps(i) for i in var_s]

lists = '{'+','.join(lists)+'}'

with open("{}".format(name),"w") as f:
    sj.dump(var_s,f)
    f.close()
