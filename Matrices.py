#Add Matrix and perform multiple operations on matrix:

def main():
    x=inputMatrix()
    y=inputMatrix()
    printMatrix(x)
    printMatrix(y)
    z=addMatrices(x,y)
    printMatrix(z)
    


def inputMatrix():
    rows=int(input("Enter number of rows:"))
    columns=int(input("Enter number of columns:"))
    m= []
    for i in range(0,rows):
        r=[]
        for j in range(0,columns):
            r.append(int(input("Enter the element at ["+str(i)+"]["+str(j)+"]")))
        m.append(r)
    return m

def printMatrix(matrix):
    for row in matrix:        
        print(*row, sep=" ")

def nRows(matrix):
    return len(matrix)
    
def nColumns(matrix):
    return len(matrix[0])

def addMatrices(m1,m2):
    sum=[]
    if (nRows(m1)==nRows(m2)) and (nColumns(m1)==nColumns(m2)):        
        for i in range(0,nRows(m1)):
            srow=[]
            for j in range(0,nColumns(m1)):
                s=m1[i][j]+m2[i][j]
                srow.append(s)
            sum.append(srow)
    return sum
    
                
    
    
  

if __name__ == "__main__":
    main()