import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def decrypt(message: str) -> str:
    if message == "":
        return ""

    resultat = ""
    for ch in message:
        if ch in CARACTERES:
            i = CARACTERES.index(ch)
            resultat += CARACTERES[(i - 1) % len(CARACTERES)]
        else:
            resultat += ch
    return resultat

