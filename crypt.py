import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message: str, pas: int = 1) -> str:
    resultat = ""
    for ch in message:
        if ch in CARACTERES:
            i = CARACTERES.index(ch)
            resultat += CARACTERES[(i + pas) % len(CARACTERES)]

        else:
            resultat += ch
    if pas != 1:
        return resultat + str(pas)
    else:
        return resultat
