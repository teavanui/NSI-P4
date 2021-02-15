import pandas
import random
import pendu_helper.py as helper

global db
global mot
global score
global helpCount
global found

def avoirMot(diff):
    """
    Retrieve a random word depending of the difficulty chosen (diff), from the db.

    Parameters
    ----------
    diff : int
        Difficulty used to find a word.

    Returns
    -------
    pandas.core.series.Series
        Row of the matched word.

    """
    global db
    mots=db.loc[db["dificulte"]==diff,["mot", "aide_1", "aide_2", "longueur"]]
    if mots["mot"].count() == -1:
        return -1
    else:
        r = random.randint(0, mots["mot"].count()+1)
        return mots.iloc[r]

def userResearch():
    """
    Second proc loop. While user is palying, lokking for a word, use this loop.

    Returns
    -------
    None.

    """
    

def main():
    """
    Main proc loop.

    Returns
    -------
    None.

    """
    global db
    global score
    #Setu global vars
    db_path = "./base_pendu.csv"
    db = pandas.read_csv(db_path, delimiter=";")
    score = 0
    run = True
    while run:
        if (score >= 12):
            print("Vous avez gagné!! Votre score est de " + score)
            score = 0
            answer = input("Vous ne voulez pas rejouer?? [O]ui ou autre: ")
        else:
            answer = input("Voulez-vous quitter? [O]ui ou autre: ")
        
        if answer != "O" and answer != "o":
            val = input("Entrez une difficulté, de 1 à 3: ")
            while ((not val.isnumeric()) or int(val)<1 or int(val)>3):
                val = input("Mauvaise valeur, entrez un nombre de 1 à 3: ")
            
            #Setup match vars
            global mot
            global found
            global helpCount
            mot=avoirMot(int(val))
            found=[]
            helpCount=0
        else:
            run=False
            print("Au revoir!")

main()