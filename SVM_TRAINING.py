import sys
from sklearn import svm
import pickle , gzip
from math import *
M1=[]
M=[]
S=[]

CV=sys.argv[1] # ids of proteins in the training dataset
ids=open(CV)
l=[]
for lines in ids :
  l.append( lines.rstrip().split("."))
   #print l
for i in l :
   # if len(i)<2:
        p=open(""+i[0]+".profile") # path + sequnces profiles for the proteins in our training dataset
        ss=open("" + i[0] +".dssp") # path +  secondry structure conformatons sequnces for the proteins in our training dataset
#    else:
        
    matrix=[]
    #print array1
    for linep in p :
        linep=linep.split()
        matrix.append(linep)
    M.append(matrix)


   # print len(matrix)
    m=[]
    list1=[] #print len(linep)
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
    
X_all=[]
for matrix ,matrix1 in zip(M,M1):
  #  X=[]
    for k in matrix1:
       
        all_pro=[]
        for i in  range(k[1]-8,k[1]+9):
           # print range(k[1]-8,k[1]+9)
            if i>-1 and i <len(matrix):
                all_pro.append([float(x1) for x1 in matrix[i]])
            else :
                    all_pro.append([0.0]*20)
        X_all.append(all_pro)

   # X_all.append(X)
#print len(X_all[0][0])
X=[]
for matrix in X_all:
    f_X=[]
   # print len(matrix)
    for list1 in matrix:
        for val in list1:
            f_X.append(val)
    X.append(f_X)

#all_y=[]   #len of xall 3 the number of matrices =>[profiles]=>profile=[[],[]] windows for every position
for matrix1 in M1:
    y=[]
    for k in matrix1:
        if k[0]=="H":
            k[0]=1
        if k[0]=="E":
            k[0]=2
        if k[0]=="-":
            k[0]=3
Y=[]
for matrix in M1:
   for l in matrix:
      Y.append (l[0])
mySVC=svm.SVC(C=2.5,kernel='rbf',gamma=0.20) # the parameters
mySVC.fit(X,Y)
 
pickle.dump (mySVC, gzip.open("/home/um55/project/modelB_.pkl.gz",'w')) #save the model
