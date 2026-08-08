from app.produits import ajouter_produits, lister_produits, rechercher_produits, supprimer_produits


def afficher_menu():
    print("\n===SmartBiz ERP V0.5===")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Rechercher un produit")
    print("4. Supprimer un produit")
    print("5. Quitter")
    return input("Votre choix : ")

def main():
    while True:
        choix=afficher_menu()
        if choix=="1":
            print("\n---Ajout d'un produit---")
            nom=input("Nom du produit : ")
            prix=input("Prix (FCFA) : ")

            ajouter_produits(nom, prix)
        
        elif choix=="2":
            lister_produits()

        elif choix=="3":
            print("\n---Recherche d'un produit---")
            nom=input("Nom a rechercher : ")
            rechercher_produits(nom)

        elif choix=="4":
            print("\n---Suppression d'un produit---")
            nom=input("Nom du produit a supprimer : ")
            supprimer_produits(nom)

        elif choix=="5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez reesayer.")
if __name__=="__main__":
    main()   