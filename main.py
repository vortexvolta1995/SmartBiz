def afficher_menu():
    print("\n===SmartBiz ERP V0.1===")
    print("1. Gestion des produits")
    print("2. Gestion des clients")
    print("3. Quitter")
    return input("Votre choix : ")

def main():
    while True:
        choix=afficher_menu()
        if choix=="1":
            print("Module produit bientot disponible")
        
        elif choix=="2":
            print("Module client (bientot disponible)")

        elif choix=="3":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez reesayer.")
if __name__=="__main__":
    main()   