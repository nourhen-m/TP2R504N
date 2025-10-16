def affiche(n):
    texte = ""
    for i in range(1, n + 1):

        if i % 3 == 0:
            texte += "Fizz"
        elif i % 5 == 0:
            texte += "Buzz"
        else:
            texte += str(i)

    return texte

