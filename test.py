print("# VOICI VOTRE SYSTEME DE CALCUL ")
def multiplication(a,b):
    resultat_multiplication = a*b
    return resultat_multiplication
def addition(a,b):
    resultat_addition=a+b
    return resultat_addition
def sustraction(a,b):
    resultat_sustraction=a-b
    return resultat_sustraction
def division(a,b):
    resultat_division=a/b
    return resultat_division
def modulo(a,b):
    resultat_modulo = a%b
    return resultat_modulo
#afficher un message aux users 
nombre_ex= 0
while nombre_ex<5:
    print("VOICI LE MENU DE CALCUL !")
    print("FAITE LE CHOIX DE VOTRE OPERATION LES MOGOR")
    print("1.multiplication")
    print("2.addition") 
    print("3.sustraction")
    print("4.divisioon") 
    print("5.modulo")  
    choix=input("Faite le choix de votre operation : ")
    nombre1= float(input("Entrez le premier nombre : "))
    noombre2 = float(input("Entrez le second nombre de l'operation : "))
    match(choix):
        case '1' :
            print("Voici le resultat de votre operation : ",multiplication(nombre1,noombre2))
        case '2' :
            print("Voici le resultat de votre operation : ",addition(nombre1,noombre2))
        case '3':
            print("Voici le resultat de votre operation : ",sustraction(nombre1,noombre2))
        case '4':
            print("Voici le resultat de votre operation : ",division(nombre1,noombre2))
        case '5':
            print("Voici le resultat de votre operation : ",modulo(nombre1,noombre2))
    nombre_ex =nombre_ex+1
