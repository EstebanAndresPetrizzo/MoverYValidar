import time


class Datos:
    def __init__(self):
        self.tiempo_total = time.time()
        self.cantidad_de_archivos_subidos = 0
        self.cantidad_de_archivos_fallidos = 0

    def tomar_tiempo(self):
        end_time = time.time()
        self.tiempo_total = end_time - self.tiempo_total

        print(f"Duración del proceso: {self.tiempo_total / 60} minutos")

    def sumar_archivo_ok(self):
        self.cantidad_de_archivos_subidos += 1

    def sumar_archivo_error(self):
        self.cantidad_de_archivos_fallidos += 1

    def tomar_cantidad(self):
        print(f"Cantidad de archivos fallidos en la subida: {self.cantidad_de_archivos_fallidos}/"
              f"{self.cantidad_de_archivos_subidos} subidos")
