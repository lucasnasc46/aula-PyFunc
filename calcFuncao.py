def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if (b==0):
        print('ERRO')
    else:
        return a/b
    

n1= float(input("digite um núemro: "))
n2= float(input("digite outro numero: "))

opc=input('escolha o caracter referente a operação q deseja')


if (opc == '+'):
    r= soma(n1, n2)
    print(r)

elif(opc == '-'):
    r= sub(n1,n2)
    print(r)

elif(opc == '*'):
    r=mult(n1, n2)
    print(r)

elif(opc == '/'):
    r=div(n1,n2)
    print (r)

else:
    print('opcao invalida')