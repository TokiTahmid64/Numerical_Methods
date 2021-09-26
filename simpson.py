import numpy as np
import pandas as pd

def function(x):
    u=2000
    q=2100
    g=9.8
    mo=140000
    
    res=u*np.log(mo/(mo-q*x))-(g*x)
    return res


def show_error():
    result=[]
    for n in range(1,6):
        a=8
        b=30
        h=((b-a)/(2*n))
        x=np.zeros((2*n+1))
        x[0]=a
        for i in range(1,2*n):
            x[i]=a +(h*i)
        x[2*n]=b
        
        y=function(x)
        
        
        res=0
        for i in range(0,2*n,2):
            sub=((x[i+2]-x[i])/6)*(y[i]+4*y[i+1]+y[i+2])
            res=res+sub
        result.append(res)
        #print("Result for n= "+str(n)+" is: "+str(res))
    
    error=['-']
    for i in range(1,5):
        err=np.abs(result[i]-result[i-1])/result[i]*100
        error.append(err)
    
    index=list(np.arange(1,6))
    df=pd.DataFrame(list(zip(index,result,error)),columns=['Sub Intervals','Distance Covered','    | Absolute Approximate Relative Error |%'])
    print(df) 
    
def main():
    print("Enter the value of n: ")
    n=int(input())
    a=8
    b=30
    h=((b-a)/(2*n))
    x=np.zeros((2*n+1))
    x[0]=a
    for i in range(1,2*n):
        x[i]=a +(h*i)
    x[2*n]=b
    
    y=function(x)
    
    
    res=0
    for i in range(0,2*n,2):
        sub=((x[i+2]-x[i])/6)*(y[i]+4*y[i+1]+y[i+2])
        res=res+sub
        
    
        
    print("Distance traveled between 8s to 30s using Simpsons rule:  " +str(res))
    print("\n")
    
    show_error()
    
if __name__ == '__main__':
    
    import numpy as np
    import math
    import pandas as pd
    main()
    
        
        