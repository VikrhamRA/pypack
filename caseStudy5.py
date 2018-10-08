
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


file=open("caseStudy5.txt","r")
data=[]
score1=[]
#i=0
for f in file:
    a=f.strip().split(" ")
    data.append(a)   
df1=pd.DataFrame(data,columns=['Score1','Score2','Change','Device'])
df2=df1[df1.columns[0]]
df3=df1[df1.columns[1]]
df4=df1[df1.columns[2]]
score1=df2
score2=df3
score3=df4
B=score3.tolist()
#print(score1)
#print(score2)
print(score3)
print(B)

