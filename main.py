from app.produits import ajouter_produit, lister_produits, rechercher_produit


def afficher_menu():
    print("\n===SmartBiz ERP V0.2===")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Rechercher un produit")
    print("Quitter")
    return input("Votre choix : ")

def main():
    while True:
        choix=afficher_menu()
        if choix=="1":
            print("\n---Ajout d'un produit---")
            nom=input("Nom du produit : ")
            prix=input("Prix (FCFA) : ")

            #Conversion du prix en nombre avec gestion d'erreur
            try:
                prix=float(prix)
                ajouter_produit(nom, prix)
            except ValueError :
                print("Le prix doit etre un nombre valide.")
        
        elif choix=="2":
            lister_produits()

        elif choix=="3":
            print("\n---Recherche d'un produit---")
            nom=input("Nom a rechercher : ")
            rechercher_produit(nom)

        elif choix=="4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez reesayer.")
if __name__=="__main__":
    main()   