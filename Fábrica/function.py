#Definindo a função
def function(repeticao, numeroDeIdades):

    repeticao = int(0)
    somaDeIdades = int(0)

    while (repeticao < numeroDeIdades):

        idade = int(input("Informe uma idade: "))
        somaDeIdades = somaDeIdades + idade
        repeticao +=1 
    
    print ("O somatório das idades vale ", +somaDeIdades)