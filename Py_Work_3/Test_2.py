
#作业1 实现Print_String
def Print_String( *values, sep = ' ',end = '\n'):
    string = ''
    for value in values:
        string += str(value)
        string += sep
    lenth = len(string)
    string = string[0:lenth-1] + end
    print(string)

    return string

Print_String("This is a Test Function")
Print_String("This","is","a","Test","Function")
Print_String("This","is","a","Test","Function",sep = '-')
Print_String("This","is","a","Test","Function",sep = '_',end = '.')

#作业2 用三种方式实现斐波那契数列
# F(n) = F(n-1)+F(n-2) (n>=3,F(1) = 1, F(2) = 1)

#方法1
def Print_Fib_M1( n ):
    f1,f2 = 1,1
    print(f1,end=' ')
    print(f2, end=' ')
    i = 2
    while( 1 ):
        Fn = f1 + f2
        f1 = f2
        f2 = Fn
        i += 1
        if i > n:
            break
        print(Fn, end=' ')
    print(end='\n')
    return
#方法2
def Print_Fib_M2( n ):
    f1,f2 = 1,1
    print(f1,end=' ')
    print(f2, end=' ')
    i = 2
    for i in range(i,n):
        Fn = f1 + f2
        f1 = f2
        f2 = Fn
        print(Fn, end=' ')
    print(end='\n')
    return

#方法3
def Print_Fib_M3_Transfer(j,n1,n2):
    Fn = n1 + n2
    n1 = n2
    n2 = Fn
    print(Fn,end=' ')
    j += 1
    return j,n1,n2

def Print_Fib_M3(n):
    f1, f2 = 1, 1
    print(f1, end=' ')
    print(f2, end=' ')
    i = 2
    while i < n:
        i,f1,f2 = Print_Fib_M3_Transfer( j = i, n1 = f1, n2 = f2)

    return



Print_Fib_M1( 25 )
Print_Fib_M2( 25 )
Print_Fib_M3( 25 )