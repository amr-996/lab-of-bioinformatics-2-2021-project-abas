
from math import *
M1=[]
M=[]
S=[]

ids=open("") # path + the ids of training data
l=[]
for lines in ids :
  l.append( lines.rstrip().split("."))
   
for i in l :
    p=open(""+i[0]+".profile") #path+ sequnces profiles of our training dataset files
    ss=open("" + i[0] +".dssp") #path+ secondry structure conformations sequnces from dssp files
    
   
    
   
          
    matrix=[]
   
    for linep in p :
        linep=linep.split()
        matrix.append(linep)
    M.append(matrix)

#training phase
  
    m=[]
    list1=[] 
    for lines in ss:
        if lines[0]!=">":
           lines=lines.split()
           lines ="".join(lines )
           list2=[]
           for i in lines :
               list2.append(i)
               m2=[]
               n=0
               for i1 in range (0,len(list2)):
                   n=+i1
                   m2.append(n)
    matrix1 = [] # matrix ss +pos
    for  i in range((len(m2))):
         matrix1.append([list2[i], m2[i]])
    M1.append(matrix1)

RH=[]
R_=[]
RE=[]

for matrix ,matrix1 in zip(M,M1):
    for k in matrix1:
        if k[0]=="H":
           
           MH=[]
           for i in  range(k[1]-8,k[1]+9):
               if i>-1 and i <len(matrix):
                   MH.append([float(x) for x in matrix[i]])
               else :
                    MH.append([0.0]*20)
           RH.append (MH)
        if k[0]=="-":
            M_=[]
            for i in  range(k[1]-8,k[1]+9):
                 if i>-1 and i <len(matrix):
                   M_.append([float(x) for x in matrix[i]])
                 else :
                    M_.append([0.0]*20)
            R_.append (M_)
#print len (R_)
        if k[0]=="E":
           ME=[]
           for i in  range(k[1]-8,k[1]+9):
               if i>-1 and i <len(matrix):
                  ME.append([float(x) for x in matrix[i]])
               else :
                  ME.append([0.0]*20)
           RE.append (ME)
_=[]
n=20
m=17  
for col in range (0,m):
    for row in range (0,n):
        if row ==0:
           _.append([0.0]*20)
E=[]
n=20
m=17  
for col in range (0,m):
    for row in range (0,n):
        if row ==0:
           E.append([0.0]*20)     
       
       
       
H=[]
n=20
m=17  
for col in range (0,m):
    for row in range (0,n):
        if row ==0:
           H.append([0.0]*20)
for i in range (len(RH)):
    W=RH[i]
  
    for j in range (len(W)):
   
        for r in range (20):
             H[j][r]=H[j][r]+W[j][r]
    W=RE[i]
   
    for j in range (len(W)):
    
        for r in range (20):
             E[j][r]=E[j][r]+W[j][r]
for i in range (len(R_)):
    W=R_[i]
   #print W
   # print len(W)
    for j in range (len(W)):
    #    print j
        for r in range (20):
             _[j][r]=_[j][r]+W[j][r]

R=[]
n=20
m=17  
for col in range (0,m):
    for row in range (0,n):
        if row ==0:
           R.append([0.0]*20)
RF=[]
n=20                                       
m=17  
for col in range (0,m):
    for row in range (0,n):
        if row ==0:
           RF.append([0.0]*20)
           
for i in range (len(H)):
    #print i
    for j in range(len(H[0])):
       # print r
       R[i][j] =E[i][j]+H[i][j]
       
        
for i in range (len(_)):
    #print i
    for j in range(len(_[0])):
       # print r
       RF[i][j] =_[i][j]+R[i][j]

N=[]
for i in range (len(RF)):
    
    row=RF[i]
    sum_=0
    for values in row:
        sum_+= values
    N.append( sum_)
#print _[0][0]
#print _[0][0]/N[0]
for rows in range (len(RF)):                           
        for col in range (len(RF[0])):
            RF[rows][col] = RF[rows][col]/float(N[rows]) #normalize all
            
            
            
for rows in range (len(H)):
        for col in range (len(H[0])):                           #normalizeH
            H[rows][col]=H[rows][col]/float(N[rows])
          
            
            
            
for rows in range (len(E)):
        for col in range (len(E[0])):
            E[rows][col]=E[rows][col]/float(N[rows])
            
            
       
            
for rows in range (len(_)):
        for col in range (len(_[0])):
            _[rows][col]=_[rows][col]/float(N[rows])
            


totalE=len(RE)/float(N[8])
total_=len(R_)/float(N[8])
totalH=len(RH)/float(N[8])
#print totalH
#print total_
#print totalE


for rows in range (len(H)):                           
        for col in range (len(H[0])):
            
         H[rows][col]= log((H[rows][col])/(((RF[rows][col]))*float(totalH)))
for rows in range (len(E)):                           
        for col in range (len(E[0])):
            
         E[rows][col]= log((E[rows][col])/(((RF[rows][col]))*float(totalE)))
for rows in range (len(_)):                           
        for col in range (len(_[0])):
            
         _[rows][col]= log((_[rows][col])/(((RF[rows][col]))*float(total_)))
         




#prediction phase 


p=[]
N=[]
A=[]
ids2=open("")  # path +the ids of the blind/test dataset 

l=[]
for lines in ids2 :
  l.append( lines.rstrip().split("."))
   #print l
for i in l :
    if len(i)<2:
        pro=open(""+i[0]+".profile") # path + sequnces profiles of our testing  dataset files
      
        
    B=".".join (i)
    N.append(B)
    
    
    
    
    matrix=[]
    for linep in pro :
        linep=linep.split()
        matrix.append(linep)
    p.append( matrix)
for name,matrix in zip(N,p) :
    PF=[]
    for i in range(len(matrix)):
        l=[]
        for k in  range(i-8,i+9):
       
            if k>-1 and k <len(matrix):
                l.append(matrix[k])
            else:
                 l.append([0.0]*20)
        PF.append(l)
    
    
# count for H 
    FH=[]
    FE=[]
    F_=[]
   
    for i in range (len(PF)):
        
    
        W=PF[i]
        #print len(W)
        SC1 = 0.0
        for j in range (len(W)):
           
            
            for r in range (20):
                SC1+=float(H[j][r])* float(W[j][r])
        #print SC1
            
                
        FH.append(SC1)
    
        
    for i in range (len(PF)):
    
        W2=PF[i]
        SC2 = 0.0
        for j in range (len(W2)):
           for r in range (20):
              SC2+=float(E[j][r])* float(W2[j][r])
        FE.append(SC2)
    
    for i in range (len(PF)):
    
        W3=PF[i]
        SC3 = 0.0
        for j in range (len(W3)):
            for r in range (20):
                SC3+=float(_[j][r])* float(W3[j][r])
        F_.append(SC3)
    ss=[]
    for i in range (len(matrix)):
        R= max(FH[i],FE[i],F_[i])
        if R==FH[i]:
           ss.append( "H")
        if R==FE[i]:
            ss.append("E")
        if R==F_[i]:
             ss.append( "-")
    G= "".join(ss)
    A.append(G)
for i ,j in zip(N,A):
   
    print (">",i,j,'\n')

    

