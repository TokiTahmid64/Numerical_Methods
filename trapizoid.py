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
        h=((b-a)/n)
        x=np.zeros((n+1))
        x[0]=a
        for i in range(1,n):
            x[i]=8+(h*i)
        x[n]=b
        
        y=function(x)
        res=y[0]+y[n]
        for i in range(1,n):
            res=res+2*y[i]
            
        res=(b-a)/(2*n)*res
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
    print("Enter the value of Sub Intrvals n: ")
    n=int(input())
    a=8
    b=30
    h=((b-a)/n)
    x=np.zeros((n+1))
    x[0]=a
    for i in range(1,n):
        x[i]=a+(h*i)
    x[n]=b
    
    y=function(x)
    res=y[0]+y[n]
    for i in range(1,n):
        res=res+2*y[i]
        
    res=(b-a)/(2*n)*res
    
    print("Integral value for provided value of n= "+str(n)+ " is: " + str(res))
    
    show_error()

if __name__ == '__main__':
    
    import numpy as np
    import math
    import pandas as pd
    main()
    
    
    
    