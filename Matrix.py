import copy

def Is_squareMatrix(a):
    for i in a:
        if not len(i)==len(a):
            return False
    else:
        return True

def Create_SubMatrix(b,m,n):

        b2=copy.deepcopy(b)

        for j in range (len(b2)):
            b2[j].pop(n)
        b2.pop(m)
        return b2
    
def Magnitude_Number(n):
        if n>=0: return n
        else: return -1*n
    
def is_UpperTriangular(b):
        l=len(b)
        for i in range (1,l):
            for j in range(i):
                if b[i][j] !=0:
                    return False
        else:
            return True

def Define_Matrix(m,n):
    matrix=[]
    for i in range  (m):
        while True:
            r = list(map(int, input(f"Row{i+1} :").split(",")))
            if len(r)==n:
                break
            else:
                print('Number of rows dosent match')
        matrix.append(r)
    return matrix

def Is_Zero(matrix,row):
    for i in (matrix[row]):
        if i!=0: return False
    else: return True

def Add_Matrixes(a,b):
    if not (len(a)==len(b) and (len(a[0]))==len(b[0])):
        return 0
    else:
        addition=[]
        for i in range (len(a)):
            r=[]
            for j in range (len(a[0])):
                r.append(a[i][j]+b[i][j])
            addition.append(r)
        return (addition)

def Substract_Matrixes(a,b):
    if not (len(a)==len(b) and (len(a[0]))==len(b[0])):
        return 0
    else:
        substraction=[]
        for i in range (len(a)):
            r=[]
            for j in range (len(a[0])):
                r.append(a[i][j]-b[i][j])
            substraction.append(r)
        return (substraction)

def Multiply_Matrixes (a,b):
    multiplication=[]
    if len(a[0])==len(b) :
        for i in range (len(a)):
            r=[]
            for j in range (len(b[0])):
                element=0
                for k in range (len(a[0])):
                    element+=1000+a[i][k]*b[k][j]-1000
                r.append(element)
            multiplication.append(r)
        return multiplication
    else:
        return 0

def Transpose (a):
    transpose=[]
    for i in range(len(a[0])):
        r=[]
        for j in range (len(a)):

            if len(a[j])!=len(a[0]):
                print('Invalid Matrix')
                return None

            r.append(a[j][i])
        transpose.append(r)
    return transpose

def Matrix_Power(a,n):

    b=copy.deepcopy(a)
    
    for i in range(n-1):
        b=Multiply_Matrixes(b,a)
    return b


def Determinent(b):
    a=copy.deepcopy(b)
    l=len(a)
    p=1
    for x in range (l):
        for y in range (l-x-1):
            if a[y][y]==0 and y!=l-x-1:
                a[y],a[y+1]=a[y+1],a[y]
                p*=-1
    for i in range (l):
        for j in range(l-1,i,-1):
            if a[i][i]==0: #Not Essential
                if i != l-1: #
                    a[i],a[i+1]=a[i+1],a[i] #
                    p*=-1 #
                else: #
                    for m in range(l):
                        if a[l-1][m] !=0:
                            fac2=a[l-1][m]
                    for m in range(l):
                        a[l-1][m]=a[l-1][m]/fac2

                break

            fact=a[j][i]/a[i][i]
            for k in range(l-1,i-1,-1):
                a[j][k]=a[j][k]-fact*a[i][k]
    det=1*p
    for i in range(l):
        det*=a[i][i]
    det=100+det-100   
    return det

def Adjoin(a):
    b=copy.deepcopy(a)
    l=len(b)
    for i in range(l):
        for j in range (l):
            c=Determinent(Create_SubMatrix(a,i,j))
            b[i][j]=c*((-1)**(j+i))
    b=Transpose(b)
    return b

def Multiply_fromNumber(b,n):
    a=copy.deepcopy(b)
    l=len(a)
    for i in range (l):
        for j in range (l):
            a[i][j]=a[i][j]*n
    return a

def Inverse(a):
    x=Determinent(a)
    if x!=0:
        return Multiply_fromNumber(Adjoin(a),1/x)
    else:
        return 0

def REF(b):
    a=copy.deepcopy(b)
    l=len(a)

    for x in range (l):
        for y in range (l-x-1):
            if a[y][y]==0 and y!=l-x-1:
                a[y],a[y+1]=a[y+1],a[y]
    for i in range (l):
        for j in range(l-1,i,-1):
            if a[i][i]==0:
                if i != l-1:
                    a[i],a[i+1]=a[i+1],a[i]

                else:
                    for m in range(l):
                        if a[l-1][m] !=0:
                            fac2=a[l-1][m]
                            for m in range(l):
                                a[l-1][m]=a[l-1][m]/fac2

                            break

            fact=a[j][i]/a[i][i]
            for k in range(l-1,i-1,-1):
                a[j][k]=a[j][k]-fact*a[i][k]

    for i in range(l):
        for j in range(l):
            if a[i][j] !=0: 
                fac=1/a[i][j]
                for k in range(j,l):
                    a[i][k]=a[i][k]*fac
                break



    return a

def RREF(b):
    a=copy.deepcopy(b)

    a=REF(a)
    l=len(a)
    
    for i in range(l):
        for j in range(l):
            if a[i][j]==1:
                for k in range(l):
                    if  k!=i:
                        fact=a[k][j]
                        for m in range(j,l):
                            a[k][m]=a[k][m]-a[i][m]*fact
                break


    return a

def Is_REF(a):
    l=len(a)
    def Bottom_Zero(b):
        m=0
        for i in range(l-1,0,-1):
            for j in (b[i]):
                if j !=0:
                    m=i
                    break
            else:
                if i<m:
                    return False
        else:
            return True
        
    def Leading_1(b):
        lead=[]
        for i in range(l):
            lead.append(l+1)
        
        for i in range(l):
            for k in range (l):
                j=b[i][k]
                if j!=0:
                    if j==1:
                        lead[i]=k
                        break
                    else:
                        return False
        for k in range(l-1,-1,-1):
            m=max(lead)
            if  m != lead[k]:
                return False
            else:
                lead.pop(k)
        else:
            return True

    if Bottom_Zero(a) and Leading_1(a):
        return True
    else:
        return False

def Is_RREF(a):
    if Is_REF(a):
        l=len(a)
        for i in range(l):
            for j in range(l):
                if a[i][j]==1:
                    for k in range(l):
                        if a[k][j]!=0 and k!=i:
                            return False
                    else: 
                        break
        else: return True
    else:
        return False

def Rank(b):

    a=copy.deepcopy(b)

    a=REF(a)

    l=len(a)
    m=l
    for i in range (l-1,-1,-1):
        if Is_Zero(a,i):
            m-=1
    return m