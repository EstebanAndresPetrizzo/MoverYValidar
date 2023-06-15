import os
from pathlib import Path
import hash
import s3_get
import s3_put
import datosCorrida

datos = datosCorrida.Datos()


# antes de subir los archivos a AWS debemos posicionarnos donde se encuentran en el disco de ISILON
def buscar_origen():
    mi_pc = "Users\\espetrizzo.SMG\\Documents" #rudi/
    ruta_raiz = os.path.abspath(os.path.sep)
    return f'{ruta_raiz}{mi_pc}'


# busco en el arbol de directorios los archivos a subir
def upload_aws_tree(src, trm, fch):
    # Se entiende que la variable src será la raiz del disco
    # y la secuencia trm/fch/trm es la forma en que se graba en este caso en ISILON
    # ejemplo PADM/2023-05-02/PADM
    # luego quedan las subcarpetas que son las instancias del tramite
    ruta_a_buscar = Path(src, trm, '/publicadas', fch, trm)
    existe = ruta_a_buscar.exists()
    if existe:
        list_de_carpetas = list(ruta_a_buscar.iterdir())
        for carpeta in list_de_carpetas:
            for file in carpeta.iterdir():
                archivo_a_subir = file.name
                try:
                    s3_put.put_object(trm, fch, carpeta, archivo_a_subir)
                    validar(src, Path(trm, fch, trm, carpeta.name, file.name))
                except Exception as e:
                    print(e)
                    datos.sumar_archivo_error()


def validar(src, dst):
    # descargamos el archivo para validar que quedo igual
    s3_get.get_object(dst)

    # calculamos los hashes
    print('verificamos que el archivo se haya subido correctamente')
    hash_origen = hash.calcular_hash(src / dst)
    hash_destino = hash.calcular_hash(f'./{dst.name}')
    if hash_origen == hash_destino:
        print("Los archivos son iguales.")
        print('*' * 50)
        datos.sumar_archivo_ok()
        # borramos el archivo recién descargado
        os.remove(f'./{dst.name}')
        # borramos el archivo en el disco original
        os.remove(src / dst.parent / dst.name)
    else:
        print("Los archivos no son iguales.")
        print('*' * 50)
        print(src / dst)
        datos.sumar_archivo_error()
        os.remove(f'./{dst.name}')


fecha = '2023-04-12'
tramite = 'PADM'
origen = buscar_origen()
upload_aws_tree(Path(origen), tramite, fecha)
