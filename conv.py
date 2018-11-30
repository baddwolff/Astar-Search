import sys
import math
import pandas as pd
import numpy as np
loc={}
res={}
with open("loc.txt", 'r') as file:
      for line in file:
          line = line.strip().split(",")
          node = line[0].strip()
          x= int(line[1].strip())
          y= int(line[2].strip())
          loc[node]=[x,y]

dest=sys.argv[1]
print(loc)
if dest not in loc.keys():
    print("invalid")
else:
    p1=loc[dest]
    for k,v in loc.iteritems():
        dist=math.sqrt((p1[0]-v[0])**2+(p1[1]-v[1])**2)
        res[k]=int(dist)
print(res)
f=open('res.txt','w')
for k,v in res.iteritems():
    s=str(k)+","+str(v)+"\n"
    f.writelines(s)
