import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

file=open("caseStudy5.txt","r")
data=[]
score1=[]
#i=0
for f in file:
    a=f.strip().split(" ")
    data.append(a)   
df1=pd.DataFrame(data,columns=['Score1','Score2','Change','Device'])
#df2=df1[df1.columns[0]]
df3=df1[df1.columns[1]]
df4=df1[df1.columns[2]]

df4=df4.tolist()
#print(score1)
#print(score2)
print(df4)
 
k=np.arange(1,51)
del df3[0]  

med1=df3[0:29]
med2=df3[29:50]
'''plt.scatter(k, df3, label= "stars", color= "green",  
        s=10) 
  
# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My scatter plot!') 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show()''' 

print(stat.mean(med1))
print(stat.median(med1))




