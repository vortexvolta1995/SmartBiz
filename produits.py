produits=[]#la liste qui contiendra tous nos produits(en memoire)

def ajouter_produit(nom, prix):
    """
    Ajoute un produit a la liste 'produits'
    """
    #On cree un dictionnaire pour le nouveau produit
    nouveau_produit={"nom":nom,"prix":prix}

    #On l'ajoute a la liste
    produits.append(nouveau_produit)
    print("Produit",nom,"ajouter avec succes !")

def lister_produits():
    """
    Affiche tous les produits
    """
    if not produits:#Si la liste est vide
        print("Aucun produit en stock")
        return
    
    print("\n Liste des produits :")
    for index, produit in enumerate(produits, start=1):
        print(index.produit['nom']-produit['prix'],"FCFA")

def recherche_produit(nom_recherche):
    """
    Recherche un produit par son nom(insensible a la casse).
    """
    for produit in produits:
        if produit["nom"].lower()==nom_recherche.lower():
            print("Produit trouve: ",produit['nom']-produit['prix'],"FCFA")
            return
    print("Aucun produit trouve avec le nom ",nom_recherche)
        