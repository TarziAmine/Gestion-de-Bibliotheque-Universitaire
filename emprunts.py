# INFO 202 - TP 3


# -*- coding: utf-8 -*-

from datetime import date, timedelta
from bibliotheque import Bibliotheque
from abonnes import ListeAbonnes, identifiant


# Chaque emprunt est un dictionnaire :
# { "id_livre": int, "id_abonne": str, "date_emprunt": date, "retour": bool }

ListeEmpruntes = []



def afficher_livres_empruntes() -> None:
    """Entree : aucune
    Sortie : None, affiche les livres actuellement empruntes
    """
    for e in ListeEmpruntes:
        if not e["retour"]:
            print("Livre ID :", e["id_livre"],
                  "- Abonne :", e["id_abonne"],
                  "- Date emprunt :", e["date_emprunt"])



def creer_emprunt(id_livre: int, id_abonne: str) -> dict:
    """Entrees : id_livre (entier), id_abonne (chaine)
    Sortie : dictionnaire representant un emprunt
    """
    emprunt = {
        "id_livre": id_livre,
        "id_abonne": id_abonne,
        "date_emprunt": date.today(),
        "retour": False
    }
    return emprunt


def emprunter_livre(id_livre: int, id_abonne: str) -> bool:
    """Entrees : id_livre (entier), id_abonne (chaine)
    Sortie : booleen, True si l'emprunt a reussi, False sinon
    """
    if not livre_disponible(id_livre):
        return False


    e = creer_emprunt(id_livre, id_abonne)
    ListeEmpruntes.append(e)
    return True


def retourner_livre(id_livre: int, id_abonne: str) -> bool:
    """Entrees : id_livre (entier), id_abonne (chaine)
    Sortie : booleen, True si le retour a reussi, False sinon
    """
    for e in ListeEmpruntes:
        if (e["id_livre"] == id_livre
                and e["id_abonne"] == id_abonne
                and e["retour"] is False):
            e["retour"] = True
            return True
    return False

def livre_disponible(id_livre: int) -> bool:
    """Entree : id_livre (entier)
    Sortie : booleen, True si le livre n'est pas actuellement emprunte
    """
    for e in ListeEmpruntes:
        if e["id_livre"] == id_livre and e["retour"] is False:
            return False
    return True








def emprunts_par_abonne(id_abonne: str) -> list:
    """Entree : id_abonne (chaine, mail de l'abonne)
    Sortie : liste des emprunts de cet abonne
    """
    resultat = []
    for e in ListeEmpruntes:
        if e["id_abonne"] == id_abonne:
            resultat.append(e)
    return resultat






DELAI_PRET = 21  # 3 semaines

def livres_en_retard() -> list:
    """Entree : aucune
    Sortie : liste des emprunts en retard (non retournes et > 3 semaines)
    """
    aujourd_hui = date.today()
    resultat = []
    for e in ListeEmpruntes:
        if not e["retour"]:
            # nombre de jours écoulés depuis l'emprunt
            ecart = (aujourd_hui - e["date_emprunt"]).days
            if ecart > DELAI_PRET:
                resultat.append(e)
    return resultat


def afficher_livres_en_retard() -> None:
    """Entree : aucune
    Sortie : None, affiche les emprunts en retard
    """
    retard = livres_en_retard()
    if not retard:
        print("Aucun livre en retard.")
    else:
        print("Livres en retard :")
        for e in retard:
            print(
                "Livre ID :", e["id_livre"],
                "- Abonne :", e["id_abonne"],
                "- Date emprunt :", e["date_emprunt"]
            )
