import string

CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def decrypt(message: str) -> str:
    if message == "":
        return ""

    pas = 1
    if message[-1].isdigit():
        pas = int(message[-1])
        message = message[:-1]

    resultat = ""
    for ch in message:
        if ch in CARACTERES:
            i = CARACTERES.index(ch)
            resultat += CARACTERES[(i - pas) % len(CARACTERES)]
        else:
            resultat += ch
    return resultat
