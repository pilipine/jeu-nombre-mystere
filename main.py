import random

#Demande à l'utilisateur un nombre entre 0 et 100

def demande_nombre():
    nombre = int (input("Entrer un nombre entre 0 et 100: "))

    if 0 <= nombre <= 100:
        print ("Merci d'avoir entrer le nombre :", nombre)
    else:
        print ("Erreur: le nombre n'est pas entre 0 et 100")
demande_nombre()

def jouer_une_partie(min_val: int = 0, max_val: int = 100, max_essais: int = 10) -> bool:
# on a donné au programme de choisir un réel entre 1 et 100.
    secret = random.randint(min_val, max_val)
    print ("J'ai choisi un nombre entre {min_val} et {max_val}. n\A toi de jouer !")


    for essai in range(1, max_essais + 1):
            proposition = demander_entier(f"Essai {essai}/{max_essais} > ", min_val, max_val)

            if proposition < secret:
                print("Trop petit.")
            elif proposition > secret:
                print("Trop grand.")
            else:
                print(f"🎉 Bravo ! Le nombre était bien {secret}. Tu as trouvé en {essai} essai(s).")
            return True


    
    print(f"Dommage… Le nombre était {secret}.")
    return False


def demande_de_rejouer() -> bool:
    """Demande si on rejoue (o/n)."""
    while True:
        rep = input("Rejouer ? (o/n) : ").strip().lower()
        if rep in {"o", "oui", "y", "yes"}:
            return True
        if rep in {"n", "non", "no"}:
            return False
        print("Réponse non comprise. Tape 'o' (oui) ou 'n' (non).")


def selection_dificulté():

    print ("Selectionner un niveau de difficulté:")
    print("1 - Facile (0 à 100)  | 5 essaies")
    print("2 - Normal (0 à 500)  |9 essaies")
    print("3 - Difficulté (0 à 1000) |12 essaies")

    choix = input("Ton choix (1/2/3) : ").strip()
    
    match choix:
            case "1":
                return 0, 100, 5
            case "2":
                return 0, 500, 9
            case "3":
                return 0, 1000, 12
            case _:
                print("Choix invalide. Difficulté par défaut : Normal (0 à 500).")
                return 0, 500, 9




        
