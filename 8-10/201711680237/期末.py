
# coding: utf-8

# In[1]:


#写函数，给定符号和行数，如’*’，5，可打印相应行数的如下菱形。主程序输入符号和行数调用该函数进行验证。（20分）
def diamond(n,s):
    for i in range(1,n+1):
        print(' '*(n-i) + s*i)
    for i in range(1,n):
        print(' '*i + s*(n-i))
s = input('请输入你想要输入的符号')
s = s +' '
n =int( input('请输入边长'))
diamond(n,s)

    


# In[4]:


# 打印空心菱形
def hollow_diamond(n,s):
    s = input('请输入一个你喜欢的符号:')
    s = s + ' '
    n = int(input('请输入边长:'))
    for i in range(1,n+1):
        if (i == 1) or (i == 2):
            print(' '*(n-i) + s*i)
        else :
            print(' '*(n-i) +(s + ' '*(2*(i-2)) + s))
    for i in range(1,n):
        if (i == n-1) or (i == n-2):
            print(' '*i + s*(n-i))
        else :
            print(' '*i + (s + ' '*(2*(n-2-i)) + s))    
        
    

hollow_diamond(n,s)


# In[16]:


#打印实心三角形
def triangle():
    s=input('请输入一个你喜欢的符号')
    s=s+' '
    n=int(input('请输入边长'))
    for i in range(1,n+1):
        print(' '*(n-i)+s*i)
triangle()


# In[24]:


#打印空心三角形
def hollow_triangle():
    s=input('请输入你喜欢的符号')
    s=s+' '
    n=int(input('请输入边长'))
    for i in range(1,n+1):
        if (i==1)or(i==2)or(i==n):
            print(' '*(n-i)+s*i)
        else:
            print(' '*(n-i)+s+' '*2*(i-2)+s)
hollow_triangle()


# In[3]:


# 打印空心等腰梯形
def trapezoid(n,m,k,s):
    for i in range(1,k+1):
        if (i == 1):
            print(' '*(k-i) + s*n)
        elif (i == k):
            print(s*m)
        else:
            print(' '*(k-i) + (s + ' '*(2*(m-2-k+i)) + s))

s = input('请输入一个你喜欢的符号:')
s = s + ' '
n = int(input('请输入上底的长度:'))
m = int(input('请输入下底的长度：'))
k = int(input('请输入高：'))
trapezoid(n,m,k,s)


# In[4]:


# 打印实心梯形
def tixing():
    for i in range(1,k+1):
        print(' '*(k-i) + s*(n+(i+1)))
    
s = input('请输入一个你喜欢的符号:')
s = s + ' '
n = int(input('请输入上底的长度:'))
k = int(input('请输入高：'))  
tixing()

