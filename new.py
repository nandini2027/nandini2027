import numpy as np
import cv2 as cv
import random as r
from pprint import pprint

img=cv.imread(r"C:\Users\ASUS\Pictures\Screenshots\Screenshot 2024-03-07 185349.png")
data=np.array(img)
#print(type(data))
dim=data.shape
#print(data)
elem=data.flatten()
#print(elem)
random=[]
i=0
while i<32:
    random.append(r.randint(0,32))
    i+=1
#pint(random)    
ascii={"A":format(ord("A"),'08b'),"B":format(ord("B"),'08b'),"C":format(ord("C"),'08b'),"D":format(ord("D"),'08b')}
#print(ascii)
changed=[]

for i in random:
    changed.append(format(elem[i],'08b'))
        
#print(changed)
changed_new=changed[:]

new=[]
k=0
for i in (ascii.keys()):
    for j in (ascii[i]):
        while k<32:
            a=list(changed_new[k])
            a[-1]=j
            new.append("".join(a))
            k+=1
            break
#print(new)
for i in range(len(new)):
    new[i]=int(new[i],2)
#print(new)
j=0
for i in random:
    while j<32:
        elem[i]=new[j]
        j+=1
        break
#print(elem) 
data_new=elem.reshape(data.shape)
#print(data_new) 
cv.imshow("img_new",data_new)
cv.waitKey(0)






    

       


