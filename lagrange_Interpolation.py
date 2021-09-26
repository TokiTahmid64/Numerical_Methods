def compute(x,y,value,n):
    res=0
    for i in range(n):
        temp=1
        for j in range(n):
            if(i!=j):
                temp=temp*(value-x[j])/(x[i]-x[j])
        res=res+(temp*y[i])
    
    return res

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



def main(): 
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
    res=compute(x,y,value,d+1)
    print(res)

 
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    main()
    
            
                   
        
    
    
    
    
    
    
    
    
    
    
    