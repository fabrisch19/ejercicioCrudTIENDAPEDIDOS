import pickle

# funcion para guardar datos en archivos binarios
def guardar_datos_en_archivo(archivo, datos):
    with open(archivo, "wb") as file:
        pickle.dump(datos, file)
    print(f"Datos guardados correctamente en {archivo}.")


#funcion para poder cargar ahora los datos en ese archivo binario 
def cargar_datos_desde_archivo(archivo):
    try:
        with open(archivo, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se devuelve la lista vacia.")
        return []  # si no existe el archivo da la lista vacia
    except EOFError:
        print(f"El archivo {archivo} esta vacio.")
        return []  # si el archivo esta creado pero vacio, dara una lista VACIA