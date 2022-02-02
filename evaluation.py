from math import *
import sys
pre_test=sys.argv[1] # the protein secondry structure conformations sequnces file(output of the predection method)
idss=sys.argv[2]     # ids of the blind dataset
S_PRE=[]
S_OB=[]
print idss
f=open(pre_test)
l=[]
for line in f: 
	if line[0]!=">":  
	 	line= line.rstrip()
    	 	line=line.split()
		

  #  	 if  len(line) >0:
     		s1= (line[0] )
      		S_PRE.append(s1)


l=[]
ids=open(idss)
for line in ids:
   l.append( line.rstrip())
#print(l)
for i in l:
    #k=[]
    ss=open(""+i+".dssp") # observed protein secondry structure conformations(output of dssp ) 
    for line in ss :
       if line[0]!=">":
        s2=( line.rstrip())
        S_OB.append(s2)
#print len(S_PRE[10])
#print len(S_OB[10])
FP=[]
FO=[]
for listp,listo in zip(S_PRE,S_OB):
    for resp,reso in zip(listp,listo):
      FP.append( resp)
      FO.append(reso)
l1= FO  
l2=FP 

m2=[]
n=0
             
for i1 in range (0,len(l1)):
     n=+i1
     m2.append(n)
#print m2
list1=[]
for i,j in zip (m2,l1):
    list1.append([j,i])
#print list1
for i,j in zip (m2,l2):
    list1.append([j,i])
#print list1
phh=[]
for k1,k2 in zip(l1,l2):
    if k1=="H" and k2=="H":
        phh.append(k1)
PHH=len(phh)
phe=[]
for k1,k2 in zip(l1,l2):
    if k1=="H" and k2=="E":
        phe.append(k1)
PHE=len(phe)
ph_=[]
for k1,k2 in zip(l1,l2):
    if k1=="H" and k2=="-":
        ph_.append(k1)
PH_=len(ph_)
peh=[]
for k1,k2 in zip(l1,l2):
    if k1=="E" and k2=="H":
        peh.append(k1)
PEH=len(peh)


pee=[]
for k1,k2 in zip(l1,l2):
    if k1=="E" and k2=="E":
        pee.append(k1)
PEE=len(pee)

pe_=[]
for k1,k2 in zip(l1,l2):
    if k1=="E" and k2=="-":
        pe_.append(k1)
PE_=len(pe_)

p_h=[]
for k1,k2 in zip(l1,l2):
    if k1=="-" and k2=="H":
        p_h.append(k1)
P_H=len(p_h)

p_e=[]
for k1,k2 in zip(l1,l2):
    if k1=="-" and k2=="E":
        p_e.append(k1)
P_E=len(p_e)

p__=[]
for k1,k2 in zip(l1,l2):
    if k1=="-" and k2=="-":
        p__.append(k1)
P__=len(p__)


Ce=PEE

Ue=PEH+PE_
Ne=PHH+P__+P_H+PH_
Oe=PHE+P_E
MCCE=float(Ce*Ne-Oe*Ue)/(((Ce+Oe)*(Ce+Ue)*(Ne+Oe)*(Ne+Ue))**0.5)
SENE=Ce/float(Ce+Ue)
PPVE=Ce/float(Ce+Oe)

C_=P__

U_=P_H+P_E
N_=PHH+PEE+PEH+PHE
O_=PH_+PE_
MCC_=float(C_*N_-O_*U_)/(((C_+O_)*(C_+U_)*(N_+O_)*(N_+U_))**0.5)
SEN_=C_/float(C_+U_)
PPV_=C_/float(C_+O_)



Ch=PHH
Uh=PHE+PH_
Nh=PEE+P__+P_E+PE_
Oh=PEH+P_H
MCCH=float(Ch*Nh-Oh*Uh)/(((Ch+Oh)*(Ch+Uh)*(Nh+Oh)*(Nh+Uh))**0.5)
SENH=Ch/float(Ch+Uh)
PPVH=Ch/float(Ch+Oh)


#SEN=Ch/Ch+Uh
#PPV=Ch/Ch+Oh
#print SEN
#print PPV
#print MCC_


Q3=float((PHH+PEE+P__)/float(len(l1)))

print ("Q3","=",Q3)
print ("MCCH","=",MCCH)
print ("MCCE","=",MCCE)
print ("MCC_","=",MCC_)
print ("SENH","=",SENH)
print ("SENE","=",SENE)
print ("SEN_","=",SEN_)
print ("PPVH","=",PPVH)
print ("PPVE","=",PPVE)
print ("PPV_","=",PPV_)


