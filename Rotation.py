def getlist(matrix,n):
    a=[]
    
    for i in range(0,len(matrix[0])):
        a.append(matrix[0][i])
        
    for i in range(1,len(matrix)):
        a.append(matrix[i][len(matrix)-1])
        
    for i in range(len(matrix)-2,0,-1):
        a.append(matrix[len(matrix)-1][i])
        
    for i in range(len(matrix[0])-1,0,-1):
        a.append(matrix[i][0])
        
    print("--input--")
    display(matrix)
    data=circle(a,n)
    putlist(data,matrix)
    
def circle(data1,n):
    b=[]
    for i in range(len(data1)-n,len(data1)):
        b.append(data1[i])
        
    for i in range(0,len(data1)-n):
        b.append(data1[i])
        
    return b
    
def putlist(data,matrix):
    matrix_len=len(matrix)
    
    for i in range(0,len(matrix[0])):
        matrix[0][i]=data[i]
        
    for i in range(1,len(matrix)):
        matrix[i][len(matrix)-1]=data[i+(matrix_len-1)]

    count=(len(matrix[0])+len(matrix))-1
    
    for i in range(len(matrix)-2,0,-1):
        matrix[len(matrix)-1][i]=data[count]
        count+=1
        
    for i in range(len(matrix[0])-1,0,-1):
        matrix[i][0]=data[count]
        count+=1
        
    print("--output--")
    display(matrix)
    
def display(matrix):
    for i in matrix:
        for j in i:
            if len(str(j))==2:
                print(j,end=" ")
            else:
                print(j,end="  ")
        print()
    
matrix=[[1,2,3,4,5,6],[20,0,0,0,0,7],[19,0,0,0,0,8],[18,0,0,0,0,9],[17,0,0,0,0,10],[16,15,14,13,12,11]]
rotation=5
getlist(matrix,rotation)
