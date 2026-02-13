# INFO 202 - TP 3


# -*- coding: utf-8 -*-


Abonne_1 = {
    "Nom": "Dupont",
    "Prenom": "Alice",
    "Mail": "alice.dupont@example.com"
}

Abonne_2 = {
    "Nom": "Martin",
    "Prenom": "Louis",
    "Mail": "louis.martin@example.com"
}

Abonne_3 = {
    "Nom": "Durand",
    "Prenom": "Emma",
    "Mail": "emma.durand@example.com"
}


ListeAbonnes = [Abonne_1, Abonne_2, Abonne_3]




def identifiant(abonne: dict) -> str:
    """Entree : abonne (dictionnaire)
    Sortie : chaine de caracteres, mail de l'abonne
    """
    return abonne["Mail"]


def creer_abonne(nom: str, prenom: str, mail: str) -> dict:
    """Entrees : nom (chaine), prenom (chaine), mail (chaine)
    Sortie : dictionnaire representant un abonne
    """
    abonne = {
        "Nom": nom,
        "Prenom": prenom,
        "Mail": mail
    }
    return abonne


def saisir_et_ajouter_abonne() -> dict:
    """Entree : aucune (utilise input)
    Sortie : dictionnaire du nouvel abonne (ajoute aussi a ListeAbonnes)
    """
    print("Quel est le nom de l'abonne ?")
    nom = input()
    print("Quel est le prenom de l'abonne ?")
    prenom = input()
    print("Quelle est l'adresse mail de l'abonne ?")
    mail = input()

    nouvel = creer_abonne(nom, prenom, mail)
    ListeAbonnes.append(nouvel)
    return nouvel
