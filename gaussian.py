def gausian(A,B,d):
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
            if(d==1):   
                A,B=x[:,:n],x[:,n]
                print("Matrix A after eliminating column: ",j, ", row:  ",i)
                print(A)
                print("Matrix B after eliminating column: ",j, ", row:  ",i)
                print(B)
                print('\n')
        
            result=np.zeros((n,))
  
        for index in range(n-1,-1,-1):
            res=0
            for i in range(index,n-1):
               res=res+ result[i+1]*x[index][i+1]
            
               
            result[index]=(x[index][n]-res)/x[index][index]
           
            
            
    
        #printing the results
        
    
    
    print("Final Output: ")
    for res in result:
        print(res)
                    
                
                

def main():
    import numpy as np
    n = int(input("Enter the number of variables:"))
   
    
    print("Input the coefficients: ")

    A=input()
    print(A)
    
    A=(A.replace('\n',' ').split(' '))
    A=[i for i in A if i]
    
    
    mat_A=[]
    for i in A[:(n*n)]:
        mat_A.append(float(i))
        
    mat_A=np.array(mat_A)
    mat_A=mat_A.reshape(n,n)
    
    mat_B=[]
    
    for i in A[-n:]:
        mat_B.append(float(i))
        
    mat_B=np.array(mat_B)
    mat_B=mat_B.reshape(n,1)
    gausian(mat_A,mat_B,1)
        

    
if __name__ == '__main__':
    import numpy as np
    main()
        
            
        
       
        
       
        
        
'''n=int(input())

a=[]
b=[]
for i in range(n):
    line=input()
    row=[]
    for item in line.split():
        row.append(float(item))
        
    a.append(row)'''
    
    
    
    
    
    
    
    
    
    
    
    
    