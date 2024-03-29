#Variaveis
h = float(input("Insira sua altura: "))
Gen= int(input("insira seu gênero sendo 0 para homem e 1 para mulher"))
CalcH = int((72.7*h) - 58)
CalcM = int((62.1*h) - 44.7)


#forçando o usuario a usar 0 ou 1
while (Gen>=2):
    Gen = int(input("insira seu gênero sendo 0 para homem e 1 para mulher"))


#Condições
if Gen == 0:
    print("seu peso ideal é de",CalcH,"Kg")
elif Gen == 1:
    print("seu peso ideal é de",CalcM,"Kg")