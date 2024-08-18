from Matrix import*
from tkinter import*
from Vector import*
from math import*
import webbrowser


mainwind=Tk()
mainwind.title('Calculator')
const={}

def Matrix_Calculator():
    global const
    global matrixes
    root=Toplevel()
    root.title("Matrix Calculator")
    matrixes={}

    e=Entry(root,width=50,borderwidth=1)
    e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    def Valid_Key(name):
        if name in matrixes:
            return True
        else:
            e.delete(0,END)
            e.insert(0,f'Matrix \'{name}\' is not defined')
            return False

    def Output(matrix1,top):
        l=len(matrix1)
        for i in range (l):
            for j in range (l):
                Label(top,text=str(matrix1[i][j])).grid(row=i,column=j,padx=6,pady=3)


    def Define_Matrix():

        top1=Toplevel()
        Label(top1,text='Size').grid(row=0,column=0)
        f=Entry(top1,width=10,borderwidth=1)
        f.grid(row=0,column=1)

        Label(top1,text='Name').grid(row=1,column=0)
        g=Entry(top1,width=10,borderwidth=1)
        g.grid(row=1,column=1)

        def Get_Matrix():
            size_m=int(f.get())
            top2=Toplevel()
            top2.title('Enter Matrix')
            el_name=0
            for i in range (size_m):
                for j in range (size_m):
                    globals()[f"my_variable_{el_name}"]=Entry(top2,width=6,borderwidth=1)
                    globals()[f"my_variable_{el_name}"].grid(row=i,column=j,columnspan=1,padx=10,pady=10)
                    el_name+=1

            def Confirm():
                global matrixes
                matrix=[]
                el_name=0
                for i in range(size_m):
                    row=[]
                    for j in range (size_m):
                        row.append((globals()[f"my_variable_{el_name}"].get()))
                        el_name+=1
                    matrix.append(row)
                try:
                    for i in range (size_m):
                        for j in range(size_m):
                                matrix[i][j]=float(matrix[i][j])
                    
                    p=g.get()
                    matrixes[p]=matrix
                except:
                    e.delete(0,END)
                    e.insert(0,'Invalid Entry')
            
                top2.destroy()
                top1.destroy()
            
            Button(top2,text='Save Matrix',command=Confirm).grid(row=size_m+1,column=0)

        Button(top1,text='Create Matrix',command=Get_Matrix).grid(row=2,column=0)

    def Add():
        global new_matrix
        try:
            a,b=e.get().split(',')

            if Valid_Key(a):
                if Valid_Key(b):
                    new_matrix=Add_Matrixes(matrixes[a],matrixes[b])
                    if not new_matrix==0:
                        top1=Toplevel()
                        Output(new_matrix,top1)
                    else:
                        e.delete(0,END)
                        e.insert(0,'These two matrixes can\'t be added')
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    def Substract():
        global new_matrix
        try:
            a,b=e.get().split(',')
            if Valid_Key(a):
                if Valid_Key(b):
                    new_matrix=Substract_Matrixes(matrixes[a],matrixes[b])
                    
                    if not new_matrix==0:
                        top1=Toplevel()
                        Output(new_matrix,top1)
                    else:
                        e.delete(0,END)
                        e.insert(0,'These two matrixes can\'t be substracted')
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    def Transpose_1():
        global new_matrix
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            new_matrix=Transpose(matrix)

            top1=Toplevel()
            Output(new_matrix,top1)

    def Inverse_1():
        global new_matrix
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            new_matrix=Inverse(matrix)
            
            if not new_matrix==0:
                top1=Toplevel()
                Output(new_matrix,top1)
            else:
                e.delete(0,END)
                e.insert(0,'Inverse can\'t be found for this matrix')

    def Multiply():
        global new_matrix
        try:
            a,b=e.get().split(',')
            if Valid_Key(a):
                if Valid_Key(b):
                    new_matrix=Multiply_Matrixes(matrixes[a],matrixes[b])

                    if not new_matrix==0:
                        top1=Toplevel()
                        Output(new_matrix,top1)
                    else:
                        e.delete(0,END)
                        e.insert(0,'Thesse two matrixes can\'t be multiplied')
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    def Power():
        global new_matrix    
        try:
            a,b=e.get().split(',')
            if Valid_Key(a):

                b=int(b)   
                new_matrix=Matrix_Power(matrixes[a],b)

                top1=Toplevel()
                Output(new_matrix,top1)
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    def Det():
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            n=Determinent(matrix)
            e.delete(0,END)
            e.insert(0,f'Determinent({name})={n}')

    def Adjoin_1():
        global new_matrix
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            new_matrix=Adjoin(matrix)

            top1=Toplevel()
            Output(new_matrix,top1)

    def Multiply_Num():
        global new_matrix
        try:
            a,b=e.get().split(',')
            b=float(b)
            matrix=matrixes[a]
            new_matrix=Multiply_fromNumber(matrix,b)

            top1=Toplevel()
            Output(new_matrix,top1)
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    def REF_1():
        global new_matrix
        name=e.get()
        if Valid_Key(name):
            new_matrix=REF(matrixes[name])

            top1=Toplevel()
            Output(new_matrix,top1)

    def RREF_1():
        global new_matrix
        name=e.get()
        if Valid_Key(name):
            new_matrix=RREF(matrixes[name])

            top1=Toplevel()
            Output(new_matrix,top1)

    def Rank_1():
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            n=Rank(matrix)
            e.delete(0,END)
            e.insert(0,f'Rank({name})={n}')

    def View_matrix():
        name=e.get()
        if Valid_Key(name):
            matrix=matrixes[name]
            
            top1=Toplevel()
            top1.title(f'Matrix {name}')
            Output(matrix,top1)

    def Clear_1():
        e.delete(0,END)

    def Delete_1():
        n=e.index(INSERT)
        e.delete(n-1,n)

    def Store_M():
        global new_matrix
        try:
            name=e.get()
            matrixes[name]=new_matrix
            e.delete(0,END)
            e.insert(0,f'Matrix has been saved to->{name}')
        except:
            e.delete(0,END)
            e.insert(0,'Invalid Entry')

    define=Button(root,text="Define Matrix",width=47,height=2,command=Define_Matrix)

    add=Button(root,text="Add",width=15,height=2,command=Add)  
    substract=Button(root,text="Subtract",width=15,height=2,command=Substract)
    multiply=Button(root,text="Multiply",width=15,height=2,command=Multiply)
    transpose=Button(root,text='Transpose',width=15,height=2,command=Transpose_1)
    power=Button(root,text='Power',width=15,height=2,command=Power)
    determinent=Button(root,text='Determinent',width=15,height=2,command=Det)
    adjoin=Button(root,text='Adjoin',width=15,height=2,command=Adjoin_1)
    multiply_num=Button(root,text='Matrix X n',width=15,height=2,command=Multiply_Num)
    inverse=Button(root,text='Inverse',width=15,height=2,command=Inverse_1)
    is_ref=Button(root,text='REF',width=15,height=2,command=REF_1)
    is_rref=Button(root,text='RREF',width=15,height=2,command=RREF_1)
    rank=Button(root,text='Rank',width=15,height=2,command=Rank_1)

    view=Button(root,text='View Matrix',width=15,height=2,command=View_matrix)
    clear_s=Button(root,text='Clear Screen',width=15,height=2,command=Clear_1)
    delete_1=Button(root,text='Delete',width=15,height=2,command=Delete_1)

    store=Button(root,text='Store\nMatrix',width=15,height=2,command=Store_M)
    vec=Button(root,text='Vector\nMode',width=15,height=2,command=Vector_Calculator)
    normal=Button(root,text='Normal\nMode',width=15,height=2,command=Normal_Calculator)


    add.grid(row=2,column=0)
    substract.grid(row=2,column=1)
    multiply.grid(row=2,column=2)
    transpose.grid(row=3,column=0)
    power.grid(row=3,column=1)
    determinent.grid(row=3,column=2)
    adjoin.grid(row=4,column=0)
    multiply_num.grid(row=4,column=1)
    inverse.grid(row=4,column=2)
    is_ref.grid(row=5,column=0)
    is_rref.grid(row=5,column=1)
    rank.grid(row=5,column=2)
    view.grid(row=6,column=0)
    clear_s.grid(row=6,column=1)
    delete_1.grid(row=6,column=2)
    define.grid(row=1,column=0,columnspan=3)
    store.grid(row=7,column=0)
    vec.grid(row=7,column=1)
    normal.grid(row=7,column=2)


def Vector_Calculator():
    global vectors
    global const
    vectors={}
    root2=Toplevel()
    root2.title('Vector Calculator')

    e1=Entry(root2,width=50,borderwidth=1)
    e1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    def IsValid(name):
        if name in vectors:
            return True
        else:
            e1.delete(0,END)
            e1.insert(0,f'Vector \'{name}\' is not defined')
            return False
            
    def Output_V(v):
        e1.delete(0,END)
        if len(v)==3:
            e1.insert(0,f'{v[0]} i + {v[1]} j + {v[2]} k')
        else:
            e1.insert(0,f'{v[0]} i + {v[1]} j')

    def Define_V():
        top1=Toplevel()
        top1.title('Vector Parameters')

        Label(top1,text='Name').grid(row=1,column=0)
        g=Entry(top1,width=20,borderwidth=1)
        g.grid(row=1,column=1,columnspan=2)

        Label(top1,text='Size').grid(row=0,column=0)
        drop=StringVar()
        size_v=[
            '2',
            '3'
        ]
        menu=OptionMenu(top1,drop,*size_v)
        menu.grid(row=0,column=1)


        def GetVector():
            global size_v
            top2=Toplevel()
            top2.title('Enter Vector')
            name_v=g.get()
            uni1=('i','j','k')
            vec=[]
            size_v=int(drop.get())
            for i in range (size_v):
                globals()[f"my_variable_{i}"]=Entry(top2,width=6,borderwidth=1)
                globals()[f"my_variable_{i}"].grid(row=0,column=i*2,columnspan=1,padx=10,pady=10)
                if i !=size_v-1:
                    Label(top2,text=f'{uni1[i]} +').grid(row=0,column=2*i+1)
                else:
                    Label(top2,text=f'{uni1[i]}').grid(row=0,column=2*i+1)
            
            def Confirm_V():
                global vectors
                for i in range(size_v):
                    vec.append(globals()[f"my_variable_{i}"].get())
                
                try:
                    for i in range(len(vec)):
                        vec[i]=float(vec[i])
                    vectors[name_v]=vec
                except:
                    e1.delete(0,END)
                    e1.insert(0,'Invalid Entry')
                
                top2.destroy()
                top1.destroy()
            Button(top2,text='Save Vector',command=Confirm_V).grid(row=1,column=0)
        Button(top1,text='Create Vector',command=GetVector).grid(row=2,column=0)

    def Add_V():
        global vector
        a=e1.get()
        try:  
            vec=list(a.split(','))
            v=[]
            for i in vec:
                if not IsValid(i):
                    return
                else:
                   v.append(vectors[i])
            vector=AddVector_n(v)
            Output_V(vector)

        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def Substract_V():
        global vector
        try:
            a,b=e1.get().split(',')
            if IsValid(a):
                if IsValid(b):
                    v1,v2=vectors[a],vectors[b]
                    vector=SubstractVector(v1,v2)
                    Output_V(vector)
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')
    
    def MultiplyScalar_V():
        global vector
        try:
            v,n=e1.get().split(',')
            if IsValid(v):
                vec=vectors[v]
                n=float(n)
                vector=MultiplyScalar(vec,n)
                Output_V(vector)
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def Magnitude_V():
        v=e1.get()
        try:
            if IsValid(v):
                vec=vectors[v]
                ans=Magnitude(vec)
                e1.delete(0,END)
                e1.insert(0,ans)
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')
    
    def Unit_V():
        global vector
        v=e1.get()
        try:
            if IsValid(v):
                vec=vectors[v]
                vector=UnitVector(vec)
                Output_V(vector)
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def DotProduct_V():
        x=e1.get()
        try:
            a,b=x.split(',')
            if IsValid(a):
                if IsValid(b):

                    vec=DotProduct2(vectors[a],vectors[b])
                    e1.delete(0,END)
                    e1.insert(0,f'{a} . {b} = {vec}')
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def Angle_V():
        try:
            a,b=e1.get().split(',')
            if IsValid(a):
                if IsValid(b):

                    ans=round(Angle(vectors[a],vectors[b]),3)
                    e1.delete(0,END)
                    e1.insert(0,f'Angel= {ans} rad')
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def Scalar3_V():
        x=e1.get()
        try:
            a,b,c=x.split(',')
            if IsValid(a):
                if IsValid(b):
                    if IsValid(c):
                        ans=Scalar_3Product(vectors[a],vectors[b],vectors[c])
                        e1.delete(0,END)
                        e1.insert(0,f'[{a},{b},{c}] = {ans}')
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def CrossProduct_V():
        global vector
        vec=list(e1.get().split(','))
        try:
            vn=[]
            for i in (vec):
                if IsValid(i):
                    vn.append(vectors[i])
            if len(vn)==len(vec):
                x=[] # I don't know why but I have to add these steps to fix the code :0
                for i in vn:
                    y=[]
                    for j in i:
                        y.append(j)
                    x.append(y)  
                vector=CrossProduct_n(x)
                Output_V(vector)
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    def View_V():
        global vector
        a=e1.get()
        if IsValid(a):
            vector=vectors[a]
            Output_V(vector)


    def Clear_V():
        e1.delete(0,END)

    def Delete_V():
        n=e1.index(INSERT)
        e1.delete(n-1,n)

    def Store_V():
        global vectors
        try:
            v=e1.get()
            vectors[v]=vector
            e1.delete(0,END)
            e1.insert(0,f'{vector} stored to -> {v}')
            
        except:
            e1.delete(0,END)
            e1.insert(0,'Invalid Entry')

    define_vec=Button(root2,text='Define Vector',width=47,height=2,command=Define_V)
    add_v=Button(root2,text='Add',width=15,height=2,command=Add_V)
    substract_v=Button(root2,text='Subtract',width=15,height=2,command=Substract_V)
    multiply_scalar=Button(root2,text='Vector X n',width=15,height=2,command=MultiplyScalar_V)
    magnitude=Button(root2,text='Magnitude',width=15,height=2,command=Magnitude_V)
    unit_v=Button(root2,text='Unit\nVector',width=15,height=2,command=Unit_V)
    dot_product=Button(root2,text='Dot Product',width=15,height=2,command=DotProduct_V)
    angle_v=Button(root2,text='Angle',width=15,height=2,command=Angle_V)
    scalar_3=Button(root2,text='Scalar Triple\nProduct',width=15,height=2,command=Scalar3_V)
    cross_product=Button(root2,text='Cross Product',width=15,height=2,command=CrossProduct_V)
    view_vector=Button(root2,text='View Vector',width=15,height=2,command=View_V)
    clear_screen=Button(root2,text='Clear',width=15,height=2,command=Clear_V)
    delete_screen=Button(root2,text='Delete',width=15,height=2,command=Delete_V)
    store_vector=Button(root2,text='Store\nVector',width=15,height=2,command=Store_V)
    normal_mode=Button(root2,text='Normal\nMode',width=15,height=2,command=Normal_Calculator)
    matrix_mode=Button(root2,text='Matrix\nMode',width=15,height=2,command=Matrix_Calculator)

    define_vec.grid(row=1,column=0,columnspan=3)
    add_v.grid(row=2,column=0)
    substract_v.grid(row=2,column=1)
    multiply_scalar.grid(row=2,column=2)
    magnitude.grid(row=3,column=0)
    unit_v.grid(row=3,column=1)
    dot_product.grid(row=3,column=2)
    angle_v.grid(row=4,column=0)
    scalar_3.grid(row=4,column=1)
    cross_product.grid(row=4,column=2)
    view_vector.grid(row=5,column=0)
    clear_screen.grid(row=5,column=1)
    delete_screen.grid(row=5,column=2)
    store_vector.grid(row=6,column=0)
    normal_mode.grid(row=6,column=1)
    matrix_mode.grid(row=6,column=2)


def Normal_Calculator():
    global const
    root1=Toplevel()
    root1.title("Simple Calculator")

    e2=Entry(root1,width=50,borderwidth=1)
    e2.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    def button_click(number):
        global z
        x=e2.get()
        z=x
        n=e2.index(INSERT)
        if x== 'Invalid Entry':
            e2.delete(0,END)
        elif '=' in x:
            x=x.split('=')[0]
            e2.delete(0,END)
            e2.insert(0,x)
            e2.icursor(n)
        
        e2.insert(n,number)

    def button_clear():
        global z
        z=e2.get()
        e2.delete(0,END)

    def del_button():
        global z
        z=e2.get()
        n=e2.index(INSERT)
        e2.delete(n-1,n)

    def button_equal_ ():
        global ans
        global z
        x=e2.get()
        z=x
        if '=' in x:
            x=x.split('=')[0]
            e2.delete(0,END)
            e2.insert(0,x)
        
        for i in const:
            if str(i) in x:
                x=x.replace(str(i),str(const[i]))
        
        try:
            y=x
            if '^' in x:
                y=x.replace('^','**')
            
            ans=eval(y)
            e2.insert(END,f'={ans}') 
        except:
            if x in const:
                e2.delete(0,END)
                e2.insert(0,const[x])
            else:
                e2.delete(0,END)
                e2.insert(0,'Invalid Entry')

    def button_store1():
        global const
        try:
            v=e2.get()
            const[v]=ans
            e2.delete(0,END)
            e2.insert(0,f'Saved to-> {v}')
        except:
            pass

    def button_undo1():
        e2.delete(0,END)
        e2.insert(0,z)

    def button_arrows(d):
        e2.icursor(e2.index(INSERT)+d)

    button_1=Button(root1,text="1",width=15,height=2,command= lambda:button_click(1))
    button_2=Button(root1,text="2",width=15,height=2,command=lambda:button_click(2))
    button_3=Button(root1,text="3",width=15,height=2,command=lambda:button_click(3))
    button_4=Button(root1,text="4",width=15,height=2,command=lambda:button_click(4))
    button_5=Button(root1,text="5",width=15,height=2,command=lambda:button_click(5))
    button_6=Button(root1,text="6",width=15,height=2,command=lambda:button_click(6))
    button_7=Button(root1,text="7",width=15,height=2,command=lambda:button_click(7))
    button_8=Button(root1,text="8",width=15,height=2,command=lambda:button_click(8))
    button_9=Button(root1,text="9",width=15,height=2,command=lambda:button_click(9))
    button_0=Button(root1,text="0",width=15,height=2,command=lambda:button_click(0))

    button_equal=Button(root1,text="=",width=15,height=2,command=button_equal_)
    button_decimalPoint=Button(root1,text=".",width=15,height=2,command= lambda:button_click('.'))
    button_delete=Button(root1,text='Del',width=15,height=2,command=del_button)

    button_addition=Button(root1,text="+",width=15,height=2,command= lambda:button_click('+'))
    button_clear1=Button(root1,text="Clear",width=15,height=2,command=button_clear)
    button_multiply=Button(root1,text="x",width=15,height=2,command= lambda:button_click('*'))
    button_substract=Button(root1,text="-",width=15,height=2,command= lambda:button_click('-'))
    button_devide=Button(root1,text="/",width=15,height=2,command= lambda:button_click('/'))

    button_bracket1=Button(root1,text="(",width=15,height=2,command= lambda:button_click('('))
    button_bracket2=Button(root1,text=")",width=15,height=2,command= lambda:button_click(')'))
    button_power=Button(root1,text="^",width=15,height=2,command= lambda:button_click('^'))

    button_sin=Button(root1,text="sin()",width=15,height=2,command= lambda:button_click('sin('))
    button_cos=Button(root1,text="cos()",width=15,height=2,command= lambda:button_click('cos('))
    button_tan=Button(root1,text="tan()",width=15,height=2,command= lambda:button_click('tan('))

    button_store=Button(root1,text='Store',width=15,height=2,command=button_store1)
    button_left=Button(root1,text='<-',width=15,height=2,command=lambda:button_arrows(-1))
    button_right=Button(root1,text='->',width=15,height=2,command=lambda:button_arrows(1))

    button_vector=Button(root1,text='Vector\nMode',width=15,height=2,command=Vector_Calculator)
    button_matrix=Button(root1,text='Matrix\nMode',width=15,height=2,command=Matrix_Calculator)
    button_undo=Button(root1,text='Undo',width=15,height=2,command=button_undo1)



    button_1.grid(row=3 ,column=0 )
    button_2.grid(row=3 ,column=1 )
    button_3.grid(row=3 ,column=2 )

    button_4.grid(row=2 ,column=0 )
    button_5.grid(row=2 ,column=1 )
    button_6.grid(row=2 ,column=2 )

    button_7.grid(row=1 ,column=0 )
    button_8.grid(row=1 ,column=1 )
    button_9.grid(row=1 ,column=2 )

    button_0.grid(row=4 ,column=0 )
    button_addition.grid(row=4,column=1)
    button_substract.grid(row=4,column=2)

    button_multiply.grid(row=5,column=0)
    button_devide.grid(row=5,column=1)
    button_power.grid(row=5,column=2)

    button_sin.grid(row=6,column=0)
    button_cos.grid(row=6,column=1)
    button_tan.grid(row=6,column=2)

    button_bracket1.grid(row=7,column=0)
    button_bracket2.grid(row=7,column=1)
    button_clear1.grid(row=7,column=2)


    button_equal.grid(row=8,column=0)
    button_decimalPoint.grid(row=8,column=1)
    button_delete.grid(row=8,column=2)

    button_store.grid(row=9,column=0)
    button_left.grid(row=9,column=1)
    button_right.grid(row=9,column=2)

    button_undo.grid(row=10,column=0)
    button_matrix.grid(row=10,column=1)
    button_vector.grid(row=10,column=2)
   

def Instructions():
    webbrowser.open('https://youtu.be/8z4yCvIRvuY')



Label(mainwind,text='Main Menu',bg='yellow',width=40,height=3).grid(row=0,column=0)
Button(mainwind,text='Normal Calculator',width=40,height=3,command=Normal_Calculator).grid(row=1,column=0)
Button(mainwind,text='Matrix Calculator',width=40,height=3,command=Matrix_Calculator).grid(row=2,column=0)
Button(mainwind,text='Vector Calculator',width=40,height=3,command=Vector_Calculator).grid(row=3,column=0)
Button(mainwind,text='Instructions',width=40,height=3,command=Instructions).grid(row=4,column=0)
Button(mainwind,text='Exit',width=40,height=3,command=mainwind.quit).grid(row=5,column=0)

mainwind.mainloop()