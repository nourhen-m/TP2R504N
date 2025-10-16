def affiche():
    texte = ""
    for i in range(1, 6):
        if i % 15 == 0:
            texte += "FrisBee"
        elif i % 3 == 0:
            texte += "Fizz"
        elif i % 5 == 0:
            texte += "Buzz"
        else:
            texte += str(i)
    return texte
