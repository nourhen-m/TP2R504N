import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message: str, pas: int = 1) -> str:
    resultat = ""
    for ch in message:
        if ch in CARACTERES:
            index = CARACTERES.index(ch)
            resultat += CARACTERES[(index + 1) % len(CARACTERES)]
        else:
            resultat += ch
    return resultat
