


def f(x):
    return x**2 + 2


def f_prime(x):
    return 2*x

def newton_raphson(guess,max_itr,error_max):
    c1=guess
    itr=0
    root_list=[c1]
    error_list=[]
    
    while(True):
        itr=itr+1
        if(itr>max_itr):
            break
        c2=c1-f(c1)/f_prime(c1)
        root_list.append(c2)
        
        error=np.abs((c2-c1)/c2)
        error_list.append(error)
        
        if(error<error_max):
            break
        
        c1=c2
        
        
    return c2,root_list,error_list




def plot():
    x=np.arange(-2,2,0.01)
    y=f(x)
    fig, ax = plt.subplots(figsize=(10,10))
    plt.rc('xtick', labelsize=15) 
    plt.rc('ytick', labelsize=15) 
    
    ax.plot(x,y,linewidth=2)

    ax.grid(True, which='both')    
    ax.axhline(y=0, color='green',linewidth=3)
    ax.axvline(x=0, color='green',linewidth=3)
    
    plt.show()
def main():
    
    plot()
    res,root,error=newton_raphson(5,100,0.005)
    print("Result is" + str(res))
    plt.plot(error)
    import pandas as pd
    df=pd.DataFrame(list(zip(root,error)),columns=['root','error'])
    print(df) 
    
    

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    main()
    
        
    
