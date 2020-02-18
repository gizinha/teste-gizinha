dic = {"1":"domingo","2":"segunda","3":"terça","4":"quarta","5":"quinta","6":"sexta","7":"sabado"}
numero = str(input("Digite o número desejado entre 1 e 7: "))
dia=dic.get(numero)
print(dia)