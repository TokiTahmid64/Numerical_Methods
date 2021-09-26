def gausian(A,B):
    x=np.append(A,B,axis=1)
    
    n=A.shape[0]
    
    
    
    
    
    
    
    
    #check if they coincident
    
    for i in range(0,n):
        for j in range(i+1,n):
            p=x[i]/x[j]
            if(np.all(p==p[0])):
                print("INFINITE SOLUTION")
                return
    # check if parallel
    
    for i in range(0,n):
        for j in range(i+1,n):
            p=x[i]/x[j]
            if(np.all(p[:-1]==p[0])==True and np.all(p[:]==p[0])==False):
                print("NO SOLUTION")
                return 
            
            
                
    
    
    #partial pivot 
    for j in range(0,n):
        
        
        for p in range(j+1,n):
            if(x[p][j]>x[j][j]):
                x[[j,p]]=x[[p,j]]
        
       
            
        i=j+1
            
        for i in range(i,n):
            x[i]=x[i]-x[j]*x[i][j]/x[j][j]
            '''if(d==1):   
                A,B=x[:,:n],x[:,n]
                print("Matrix A after eliminating column: ",j, ", row:  ",i)
                print(A)
                print("Matrix B after eliminating column: ",j, ", row:  ",i)
                print(B)
                print('\n')'''
        
            result=np.zeros((n,),dtype=np.float64)
  
        for index in range(n-1,-1,-1):
            res=0.0
            for i in range(index,n-1):
               res=np.float64(res+ result[i+1]*x[index][i+1])
            
               
            result[index]=np.float64((x[index][n]-res)/x[index][index])
           
            
            
    
        #printing the results
        
    
    
    
    
    return result
                         
def exponential_regression(X,Y):
    n=X.shape[0]
    Y=np.log(Y)
    a1=(n*np.sum(X*Y)-(np.sum(X)*np.sum(Y))) / (n*np.sum(X**2) - (np.sum(X))**2)
    a0=np.mean(Y)-a1*np.mean(X)
    b=a1
    a=np.exp(a0)
    
    return a,b


def plot(X,Y,result1,result2,result3,result4):
    
    
    trend1=result1[0]+result1[1]*X
    trend2=result2[0]+result2[1]*X +result2[2]*X**2 
    trend3=result3[0]+result3[1]*X +result3[2]*X**2+ result3[3]*X**3
    trend4=result4[0]*np.exp(result4[1]*X)
    
    rms1 = mean_squared_error(Y, trend1, squared=False)
    rms2 = mean_squared_error(Y, trend2, squared=False)
    rms3 = mean_squared_error(Y, trend3, squared=False)
    rms4 = mean_squared_error(Y, trend4, squared=False)
    corr1,_=pearsonr(Y,trend1)
    corr2,_=pearsonr(Y,trend2)
    corr3,_=pearsonr(Y,trend3)
    corr4,_=pearsonr(Y,trend4)
    print("Correlation: ")
    print("Degree 1: "+ str(corr1))
    print("Degree 2: "+ str(corr2))
    print("Degree 3: "+ str(corr3))
    print("Exp: "+ str(corr4))
    
    plt.rc('font', size=20,weight='bold')          # controls default text sizes
    plt.rc('axes', titlesize=25)     # fontsize of the axes title
    plt.rc('axes', labelsize=25)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=25)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=25)    # fontsize of the tick labels
    fig,ax=plt.subplots(figsize=(12,12))
    ax.scatter(X,Y,s=3,color='black')
    X=np.linspace(0,10,100)
    trend1=result1[0]+result1[1]*X
    trend2=result2[0]+result2[1]*X +result2[2]*X**2 
    trend3=result3[0]+result3[1]*X +result3[2]*X**2+ result3[3]*X**3
    trend4=result4[0]*np.exp(result4[1]*X)
    
    

    
    
    ax.plot(X,trend1,label='Degree 1: '+str(rms1),linewidth=3)
    ax.plot(X,trend2,label='Degree 2: '+str(rms2),linewidth=3)
    ax.plot(X,trend3,label='Degree 3: '+str(rms3),linewidth=3)
    ax.plot(X,trend4,label='Exponential Fitting :'+str(rms4),linewidth=3)
    ax.legend()
    
    
    

           
def polynomial_regression(X,Y,order):
    A=np.ones((order+1,order+1),dtype=np.float64)
    n=X.shape[0]
    
    for i in range(order+1):
        for j in range(order+1):
            #print(i+j)
            A[i][j]=np.sum(X**(i+j))
            
    
    B=np.zeros((order+1,1),dtype=np.float64)
    
    for i in range(order+1):
        B[i]=np.sum(X**(i)*Y)
        
    
    result=gausian(A,B)
    print("Final Output: ")
    for (i,res) in zip(range(len(result)),result):
        print('a'+str(i)+'=  '+str(res))
        
    return result
        
        
    
def main():
    with open('E:/2-1/dld lab/books/input.txt') as f:
        lines = f.readlines()
    
    x_list=[]
    y_list=[]
    for line in lines:
        x=line.replace('\n',' ').split(' ')
        x_list.append(np.float64(x[0]))
        y_list.append(np.float64(x[1]))
        
    
    X=np.array(x_list)
    Y=np.array(y_list)
       
    result1=polynomial_regression(X,Y,1)
    result2=polynomial_regression(X,Y,2)
    result3=polynomial_regression(X,Y,3)
    result4=exponential_regression(X,Y)
    plot(X,Y,result1,result2,result3,result4)
    
    

if __name__ == '__main__':
    
    import numpy as np
    import math
    import pandas as pd
    from sklearn.metrics import mean_squared_error
    import matplotlib.pyplot as plt
    from scipy.stats import pearsonr
    main()
    
    
    
    
    
    
    
    
    
    