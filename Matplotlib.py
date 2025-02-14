import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  

# Series create karna
ns= pd.Series([2,4,6,8,10],index =["A","B","c","D","E"],name = "EVEN")
print(ns)
print(ns[0])
print(ns["A"])

# DataFrame create karna
arr2D = np.random.randint(1,10,(3,4))
firstDF = pd.DataFrame(arr2D,columns =["AJAY","AALU","PANDEY","MOSHI"],index=["MATHS","PHYSICS","CHEMISTRY"])
print(firstDF)

# List of lists (LOL) se DataFrame banana
LOL = [["amar",10],["AKBAR",15],["anthony",14]]
df = pd.DataFrame(LOL,columns=["name","age"])
print(df)

# Dictionary se DataFrame banana
emp = {"employe name":["raju","sabu","mangu"],"income":[25000,30000,45000]}
emp = pd.DataFrame(emp)
print(emp)

# Series se dictionary banana
serdict ={"FIRST SER": ns,"SECOND SER": pd.Series([10,20,30,40,50])}
print(serdict)

# Random image generate karna
height =100
width =100 
random_image =np.random.randint(0,256,(height ,width,3),dtype=np.uint8) 

# Matplotlib se random image display karna
plt.imshow(random_image)
plt.axis('off')
plt.show()
