# 7- Validar un diccionario con emails y si estan activos o no
def validar_email(email):

    # compruebo que no haya mas de un @
    if email.count('@') != 1:
        return False

    # divido el email en usuario y dominio, partiendolo por el @
    usuario, dominio = email.split('@')
    
    if "@" not in email or (" " in usuario or "." in usuario) or (".") not in dominio:
        return False
    return True

emails = {
    "joaquin":{
        "email": "starseeker_noether@outlook.com",
        "activated": True
    },
    "rosalinda":{
        "email": "example@gmail.com",
        "activated": False
    },
}

for nombre, datos in emails.items():
    isActivo = datos['activated']
    print(f"Email valido: {datos['email']} y {"esta activo" if isActivo else "no esta activo" }") if validar_email(datos['email']) else print(f"Email invalido: {datos['email']}")