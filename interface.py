# INFO 202 - TP 3

# -*- coding: utf-8 -*-

from livre import saisir_livre, afficher_livre

from bibliotheque import (
    Bibliotheque,
    ajouter_livre,
    recherche_par_titre,
    recherche_par_auteur,
    recherche_par_categorie,
    affiche_liste_livres,
)

from abonnes import ListeAbonnes, saisir_et_ajouter_abonne, identifiant

from emprunts import (
    afficher_livres_empruntes,
    emprunter_livre,
    retourner_livre,
    emprunts_par_abonne,
)


def menu() -> None:
    """Affiche le menu principal."""
    print("Que souhaitez-vous faire ?")
    print("1 - Emprunter un livre")
    print("2 - Retourner un livre")
    print("3 - Creer un nouveau livre")
    print("4 - Creer un nouvel abonne")
    print("5 - Rechercher un livre")
    print("6 - Afficher la liste des livres empruntes par abonne")
    print("7 - Quitter")


def choix_recherche() -> None:
    """Sous-menu de recherche de livre."""
    print("Comment voulez-vous rechercher ?")
    print("1 - Par titre")
    print("2 - Par auteur")
    print("3 - Par categorie")
    print("4 - Afficher tous les livres")
    choix = input()

    if choix == "1":
        print("Titre du livre :")
        t = input()
        livre = recherche_par_titre(Bibliotheque, t)
        if livre:
            afficher_livre(livre)
        else:
            print("Aucun livre trouve.")
    elif choix == "2":
        print("Auteur :")
        a = input()
        res = recherche_par_auteur(Bibliotheque, a)
        if res:
            for l in res:
                afficher_livre(l)
                print("-" * 40)
        else:
            print("Aucun livre trouve.")
    elif choix == "3":
        print("Categorie :")
        c = input()
        res = recherche_par_categorie(Bibliotheque, c)
        if res:
            for l in res:
                afficher_livre(l)
                print("-" * 40)
        else:
            print("Aucun livre trouve.")
    elif choix == "4":
        affiche_liste_livres(Bibliotheque)
    else:
        print("Choix de recherche invalide.")


def demander_id_abonne() -> str:
    """Demande l'adresse mail (identifiant) d'un abonne a l'utilisateur."""
    print("Adresse mail de l'abonne :")
    return input()



def gestionBU() -> None:
    """Boucle principale de gestion de la BU."""
    continuer = True
    while continuer:
        menu()
        choix = input()

        # 1 - Emprunter un livre
        if choix == "1":
            print("ID du livre a emprunter :")
            entree = input()
            action_valide = True

            if not entree.isdigit():
                print("Identifiant de livre invalide.")
                action_valide = False

            if action_valide:
                id_livre = int(entree)
                id_abonne = demander_id_abonne()
                if emprunter_livre(id_livre, id_abonne):
                    print("Emprunt enregistre.")
                else:
                    print("Emprunt impossible (livre deja emprunte ou erreur).")

        # 2 - Retourner un livre
        elif choix == "2":
            print("ID du livre a retourner :")
            entree = input()
            action_valide = True

            if not entree.isdigit():
                print("Identifiant de livre invalide.")
                action_valide = False

            if action_valide:
                id_livre = int(entree)
                id_abonne = demander_id_abonne()
                if retourner_livre(id_livre, id_abonne):
                    print("Retour enregistre.")
                else:
                    print("Retour impossible (emprunt non trouve).")

        # 3 - Creer un nouveau livre
        elif choix == "3":
            nouveau = saisir_livre()
            ajouter_livre(Bibliotheque, nouveau)
            print("Livre ajoute a la bibliotheque :")
            afficher_livre(nouveau)

        # 4 - Creer un nouvel abonne
        elif choix == "4":
            nouvel_abonne = saisir_et_ajouter_abonne()
            print("Nouvel abonne enregistre :")
            print(identifiant(nouvel_abonne))

        # 5 - Rechercher un livre
        elif choix == "5":
            choix_recherche()

        # 6 - Afficher la liste des livres empruntes par abonne
        elif choix == "6":
            id_abonne = demander_id_abonne()
            liste = emprunts_par_abonne(id_abonne)
            if not liste:
                print("Aucun emprunt pour cet abonne.")
            else:
                print("Emprunts pour", id_abonne)
                for e in liste:
                    print(
                        "Livre ID :", e["id_livre"],
                        "- Date emprunt :", e["date_emprunt"],
                        "- Retour :", e["retour"]
                    )

        # 7 - Quitter
        elif choix == "7":
            continuer = False

        else:
            print("Choix invalide, veuillez recommencer.")




