import math
import Matrix

def Create3vector(v1,v2):
    l=len(v2)
    if len(v1)>l:
        v2.append(0)
    elif len(v1)<l:
        v1.append(0)
    return v1,v2

def AddVector2(v1,v2):
    v1,v2=Create3vector(v1,v2)

    l=len(v2)

    vector=[]
    for i in range (l):
        vector.append(v1[i]+v2[i])
    return vector

def SubstractVector(v1,v2):
    v1,v2=Create3vector(v1,v2)
    l=len(v2)

    vector=[]
    for i in range (l):
        vector.append(v1[i]-v2[i])
    return vector

def MultiplyScalar(v,n):
    vector=[]
    for i in v:
        i*=n
        vector.append(i)
    return vector

def Magnitude(v):
    magnitude=0
    for i in v:
        magnitude+=i**2
    magnitude=magnitude**0.5
    return magnitude

def UnitVector(v):
    vec=[]
    u=Magnitude(v)
    for i in v:
        vec.append(round(i/u,5))
    return vec

def DotProduct2(v1,v2):
    v1,v2=Create3vector(v1,v2)
    l=len(v2)

    p=0
    for i in range(l):
        p+=v1[i]*v2[i]
    return(p)

def Angle(v1,v2):
    v1Mag=Magnitude(v1)
    v2Mag=Magnitude(v2)
    dotProdut=DotProduct2(v1,v2)

    cos_Value=dotProdut/(v1Mag*v2Mag)

    return math.acos(cos_Value)

def CrossProduct2(v1,v2):
    v1,v2=Create3vector(v1,v2)

    l=len(v1)
    if l==3:
        vector=[]
        vec=[[1,1,1],v1,v2]

        for i in range (3):
            v=Matrix.Create_SubMatrix(vec,0,i)
            vector.append(Matrix.Determinent(v)*((-1)**i))
                        

    else:
        vec=[v1,v2]
        vector=[0,0,Matrix.Determinent(vec)]
        
    return vector

def Scalar_3Product(v1,v2,v3):
    vx=[0,0,0]
    vx,v1=Create3vector(vx,v1)
    v1,v2=Create3vector(v1,v2)
    v2,v3=Create3vector(v2,v3)
    v3,v1=Create3vector(v3,v1)

    v=[v1,v2,v3]
    return Matrix.Determinent(v)

def CrossProduct_n(v):
    Len=len(v)

    if Len==0: return None
    elif Len==1: return v[0]
    elif Len==2: return CrossProduct2(v[0],v[1])
    else:
        a=CrossProduct2(v[0],v[1])
        for i in range(2,Len):
            a=CrossProduct2(a,v[i])
        
        return(a)

def AddVector_n(v):
    l=len(v)
    
    if l==0: return None
    elif l==1: return v[0]
    elif l==2: return AddVector2(v[0],v[1])
    else:
        a=AddVector2(v[0],v[1])
        for i in range(2,l):
            a=AddVector2(a,v[i])
        
        return(a)