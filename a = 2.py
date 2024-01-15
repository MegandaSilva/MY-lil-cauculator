print(" Seja bem vindo à melhor calculadora do mundo")
nm =input("Me diga seu nome: ")
print("olá", nm)
sinal= (input(" qual o sinal de operação que gostaria de usar?(+,-,*,/) "))
n1 =float(input("primeiro numero:"))
n2 = float( input("segundo numero: "))

if sinal == "+":
    print("resultado:",n1+n2)
elif sinal == "-":
    print("resultado:",n1-n2)
elif sinal == "*":
    print("resultado:",n1*n2)
else:
    print("resultado:",n1/n2)
    

