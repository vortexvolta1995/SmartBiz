produits=[]

def ajouter_produit(nom,prix):
    """
    Ajoute un produit a la liste 'produits'
    """
    nouveau_produit={"nom":nom,"prix":prix}

    produits.append(nouveau_produit)
    print("Produit",nom,"ajoute avec succes !")

def lister_produits():
    """
    Afficher tous les produits stockes dans la liste
    """
    if not produits:
       print("Aucun produit en stock.")
       return
    
    print("\n Liste des produits :")
    for index, produit in enumerate(produits, start=1):
        print(index.produit['nom']-produit['prix'],"FCFA")

def rechercher_produit(nom_recherche):
    """
    Recherche un produit par son nom(insensible a la casse).
    """
    for produit in produits:
        if produit['nom'].lower()==nom_recherche.lower():
            print("Produit trouve:",produit['nom']-produit['prix'],"FCFA")
            return
    print("Aucun produit trouve avec le nom",nom_recherche)
