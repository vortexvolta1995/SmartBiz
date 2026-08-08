def valider_nom(nom) :
    """
    Verifie si le nom est valide(non vide et pas que des espaces)
    Retourne True si valide, False sinon.
    """
    if not nom:#si la chaine est vide
        return False
    if nom.strip()=="":#si la chaine ne contient que des espaces
        return False
    return True
    
def valider_prix(prix):
    """
    Verifie si le prix est un nombre positif
    return true si valide, false sinon
    """
    try:
        prix_float=float(prix)
        if prix_float<=0:
            return False
        return True
    except ValueError:
        return False