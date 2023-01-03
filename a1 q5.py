import math  
for i in range(0,360,15):
     x=math.radians(i) 
     y=math.sin(x)
     z=math.cos(x)
     y = round(y, 4)
     z = round(z, 4)
     print(i,'---',y,z) 

