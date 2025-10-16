def affiche(n):
    texte = ""
    for i in range(1, n + 1):

        if i % 3 == 0:
            texte += "Fizz"
        else:
            texte += str(i)

    return texte

