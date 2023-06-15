import hashlib


def calcular_hash(archivo):
    # Crea un objeto hash
    hash_object = hashlib.md5()

    # Lee el archivo en bloques para manejar archivos grandes
    with open(archivo, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)

    # Devuelve el hash en formato hexadecimal
    file.close()
    return hash_object.hexdigest()
