"""
Referencias: 
 1. Acceder a una variable de una clase: https://www.codigopiton.com/variables-de-clase-y-de-instancia-en-python/#:~:text=Como%20puedes%20ver%2C%20para%20acceder,código%20definido%20en%20la%20clase.
 2. Acceder a un método de una clase: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#:~:text=Para%20crear%20un%20objeto%20de,se%20llamara%20a%20una%20función).&text=El%20código%20anterior%20crea%20una,objeto%20a%20la%20variable%20obj%20.
 3. Inicializar una clase: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30
 4. Clases en Python: https://tutorial.recursospython.com/clases/#:~:text=Para%20crear%20una%20clase%20vamos,mayúscula%2C%20y%20sin%20guiones%20bajos.
"""
#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from textures import * #Importando los métodos del archivo textures.py.

def main():
    glCreateWindow(5120, 5120) #Creando la ventana.
    glClearColor(0, 0, 0) #Color del fondo.
    glClear() #Limpiando el framebuffer con el color creado en glClearColor.
    
    glViewPort(2100, 2100, 300, 300) #Asignando el viewport.

    col1 = (0.6, 0.1, 0.9) #Otro color.

    lookAt(V3(0, 0, 10), V3(0, 1, 0), V3(0, 1, 0))

    scale = (3, 3, 3) #Escala para las cajas.
    translate = (0, 0, 0) #Traslación para las cajas.
    
    rotacion = (0, 0, 0) #Rotación para las cajas.

    print("Rotación: ", rotacion)
    
    #Esta llamada puede no estar acá.
    loadModelMatrix(translate, scale, rotacion) #Se carga la matriz de transformación del modelo. Acá se recibe la traslación, la escala y la rotación.

    #Esta función ahora recibe primero el path del obj, luego el path del bmp, el color.
    modelo("./sphere.obj", "", col1) 

    glFinish() #Escribiendo el framebuffer en la imagen y guardándola en un archivo.

main()