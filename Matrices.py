#Add Matrix and perform multiple operations on matrix:

def main():
    x=inputMatrix()
    printMatrix(x)
    y=inputMatrix()   
    printMatrix(y)
    z=multiplyMatrices(x,y)
    printMatrix(z)
    


def inputMatrix():
    rows=int(input("Enter number of rows:"))
    columns=int(input("Enter number of columns:"))
    m= [[int(input("Enter the element at ["+str(i)+"]["+str(j)+"]")) for j in range(0,columns)] for i in range(0,rows)]           
    return m

def printMatrix(matrix):
    if len(matrix)!=0:
        for row in matrix:        
            print(*row, sep=" ")
    else:
        print("The matrix is empty/does not exist")
    
        

def nRows(matrix):
    return len(matrix)
    
def nColumns(matrix):
    return len(matrix[0])

def addMatrices(m1,m2):    
    sum=[[m1[i][j]+m2[i][j] for j in range(0,nColumns(m1))] for i in range(0,nRows(m1)) if ((nRows(m1)==nRows(m2)) and (nColumns(m1)==nColumns(m2)))]    
    if len(sum)!=0:
        return sum
    else:
        print("Addition of matrices with different number of rows and columns is not possible")
        return []


def subMatrices(m1,m2):
    sub=[[m1[i][j]-m2[i][j] for j in range(0,nColumns(m1))] for i in range(0,nRows(m1)) if ((nRows(m1)==nRows(m2)) and (nColumns(m1)==nColumns(m2)))]    
    if len(sub)!=0:
        return sub
    else:
        print("Subtraction of matrices with different number of rows and columns is not possible")
        return []
    
                
def multiplyMatrices(m1,m2):
     m=[]
     if(nColumns(m1)==nRows(m2)):
         n=nColumns(m1)
         for i in range(0,nRows(m1)):
             row=[]
             for j in range(0,nColumns(m2)):
                 sum=0
                 for x in range(0,n):
                     sum+=m1[i][x]*m2[x][j]
                 row.append(sum)
             m.append(row)
     return m

                 
    
    

if __name__ == "__main__":
    main()