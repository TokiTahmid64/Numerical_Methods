
import numpy as np
import matplotlib.pyplot as plt
import math

def fun(x):
    """ This is the definition of the given function """
    x1=x/(1-x) * math.sqrt(6/(2+x))
    return x1-0.05
  
def plot():
    """This function plots the given equation to guess the position of the root"""
    
    fig, ax = plt.subplots(figsize=(10,10))
    plt.rc('xtick', labelsize=15) 
    plt.rc('ytick', labelsize=15) 
    
    x_axis_before1=[]
    x_axis_after1=[]
    for i in np.arange(-1.99,0.99,0.01):
            x_axis_before1.append(i)
         
    for i in np.arange(1.01,3,0.01):
            x_axis_after1.append(i)
            
    x1=np.array(x_axis_before1)
    x2=np.array(x_axis_after1)
    

    fun2=np.vectorize(fun)
    y1=fun2(x1)
    y2=fun2(x2)
   
    ax.plot(x1,y1,linewidth=5)
    ax.plot(x2,y2,linewidth=5)

    ax.grid(True, which='both')    
    ax.axhline(y=0, color='green')
    ax.axvline(x=0, color='green')
    
    plt.show()

def bisection(low,up,app_error,max_itr):
    
    """ Bisection method is used in this function to determine the value of root"""
    app_error=app_error/100
    if(fun(low)*fun(up)>=0):
        print("Not proper selection")
        return
    
    else:
        root=[]
        error_list=[]
        c1=None
        itr=0
        while(True):
            itr=itr+1
            if(itr>max_itr):
                break
            
            
            c2=(low+up)/2
            
            if(c1!=None):
                error=np.abs((c2-c1)/c2)
                error_list.append(error)
                if(error<app_error):
                    break
            c1=c2
            if(fun(c2)==0.0):
                break
            
            if(fun(c2)*fun(low)<0):
                up=c2
            else:
                low=c2
            
            root.append(c2)
        root.append(c2)
        error_list.append(error)
    return c2,root,error_list

def main():
    """Main function"""
    plot()
    print("Visual Estimation of the root is between -0.9 to 0.5")
    res,root,error=bisection(-0.9,0.5,5,1000)
    print("Estimated Root from bisection :" + str(res))
    import pandas as pd
    df=pd.DataFrame(list(zip(root,error)),columns=['root','error'])
    print(df) 
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    main()
    
            
            
            
        
    
   