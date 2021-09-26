def createtable(x,y):
    n=y.shape[0]
    ara=np.zeros((n,n))
    for i in range(n):
        ara[i,0]=y[i]
    
    i=0
    for col in range(1,n):
        for row in range(n-col):
            ara[row,col]=(ara[row+1,col-1]-ara[row,col-1])/(x[col+i]-x[i])
            i=i+1
        i=0   
    return ara
def takepoints(x,y,val,n):
  xs=[]
  ys=[]
  tempx=x
  tempy=y
  for i in range(n):
    idx=(np.abs(tempx-val)).argmin()
    xs.append(tempx[idx])
    ys.append(tempy[idx])
    tempx=np.delete(tempx,idx)
    tempy=np.delete(tempy,idx)
    
  tempx=np.array(xs)
  tempy=np.array(ys)

  return tempx,tempy

def compute(ara,x,val):
    res=0
    n=x.shape[0]
    
    for i in range(n):
        temp=1
        for j in range(i):
            temp=temp*(val-x[j])
        res=res+(temp*ara[0,i])
        
        
    for i in range(n):
        print('b'+str(i)+': '+str(ara[0,i]))
                     
    return res  


def main(): 
    import numpy as np
    '''print("How many points do you want to enter? :")
    n=int(input())
    print("Please enter the values: ")
    x=[]
    y=[]
    
    for i in range(n):
        print("X:")
        x1=float(input())
        print("Y:")
        y1=float(input())
        x.append(x1)
        y.append(y1)
    
    print("Please enter the value of interest: ")
    value=float(input())
    
    print("Please enter the degree of polynomial: ")
    d=int(input())
        
    x=np.array(x)
    y=np.array(y)'''
    
    with open('E:/2-1/dld lab/books/input.txt') as f:
        lines = f.readlines()
    
    x_list=[]
    y_list=[]
    for line in lines:
        x=line.replace('\n',' ').split(' ')
        x_list.append(np.float64(x[0]))
        y_list.append(np.float64(x[1]))
        
    
    x=np.array(x_list)
    y=np.array(y_list)
    print("Please enter the value of interest: ")
    value=float(input())
    
    print("Please enter the degree of polynomial: ")
    d=int(input())
    
    
    
    
    x,y=takepoints(x,y,value,d+1)
    ara=createtable(x,y)
    res=compute(ara,x,value)
    print(res)
        
 
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    main()
        
    















        