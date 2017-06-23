# Reto CIFAR-10
## Descripción
El [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) es un conjunto de 60000 imágenes a color de 10 distintas categorías. Las categorías son: avión, automovil, pájaro, gato, venado, perro, rana, caballo, barco y camión. El tamaño por defecto es 32x32 pixeles.

![alt text][s1] ![alt text][s2] ![alt text][s3] ![alt text][s4] ![alt text][s5] ![alt text][s6] ![alt text][s7] ![alt text][s8] ![alt text][s9] ![alt text][s10]

![alt text][s11] ![alt text][s21] ![alt text][s31] ![alt text][s41] ![alt text][s51] ![alt text][s61] ![alt text][s71] ![alt text][s81] ![alt text][s91] ![alt text][s101]

El reto es construir un clasificador de imágenes que sea capaz de reconocer las 10 categorías.

### Ranking
Ver [ranking](https://github.com/charlielito/supervised-avanzado-cifar10/blob/master/ranking.md).

### Formato Datos
Todos los datos están en la carpeta `.dataget/data/cifar10` y se dividen en 2 grupos
```
|- .dataget
   |- data
      |- cifar10
         |- traning-set
         |- test-set
```

**Estructura** <br>
Cada sub conjunto de datos (training-set o test-set) tiene la siguiente estructura
```
|- {subset}
   |- {class_id}
      |- {image_id}.jpg
```
Donde
* `subset`: es `training-set` o `test-set`
* `class_id`: es el identificador de una clase, e.g. 0, 1, 2, ..., 9
* `image_id`: es el nombre de una imagen.

### Variables
Cada imagen como tal puede ser representada por una matriz de dimensiones `height x width x 3` dado que es RGB.

### Objetivo
1. Crear un algoritmo que tome una imagen de entrada, ya sea como vector o matriz, y retorne el clase (`class_id`) a la que pertenece esa imagen.
1. Entrenar este algoritmo utilizando los datos de la carpeta `data/training-set`.
1. Medir el performance/score del algoritmo utilizando los datos de la carpeta `data/test-set`. El performance debe ser medido como
```python
score = n_aciertos / n_imagenes * 100
```
donde `n_aciertos` es el número de imágenes clasificadas de forma correcta y `n_imagenes` es el número total de imágenes en el `test-set`.

### Notas Teóricas
* Dado que las imagenes son conjuntos con dimensiones muy altas, usualmente la mejor manera de atacar el problema es utilizando [redes neuronales](https://en.wikipedia.org/wiki/Artificial_neural_network).
  * Para imágenes es recomendable utilizar redes [convolucionales](http://cs231n.github.io/convolutional-networks/).

### Solución
Ver procedimiento de [solución](https://github.com/colomb-ia/formato-retos#solucion)

##### Requerimientos
*Indica los requerimientos para utilizar el codigo de tu solucion*

##### Procedimiento
*Indica el procedimiento que se debe seguir para reproducir tu solucion*

##### Método
*Indica el metodo que utilizaste para solucionar el reto*

##### Resultados
*Indica el metodo que utilizaste para solucionar el reto*

## Getting Started
Para resolver este reto primero has un [fork](https://help.github.com/articles/fork-a-repo/) de este repositorio y [clona](https://help.github.com/articles/cloning-a-repository/) el fork en tu máquina.

```bash
git clone https://github.com/{username}/supervised-avanzado-cifar10
cd supervised-avanzado-cifar10
```

*Nota: reemplaza `{username}` con tu nombre de usuario de Github.*

### Requerimientos
Para descargar y visualizar los datos necesitas Python 2 o 3. Las dependencias las puedes encontrar en el archivo `requirements.txt`, el cual incluye
* pillow
* pandas
* numpy
* jupyter
* dataget

Puedes instalarlas fácilmente utilizando el commando

```bash
pip install -r requirements.txt
```
Dependiendo de tu entorno puede que necesites instalar paquetes del sistema adicionales, si tienes problemas revisa la documentación de estas librerías.

### Descarga y Preprocesamiento
Para descargar los datos ejecuta el comando
```bash
dataget get --keep-raw --dont-process cifar10
```
Esto descarga los archivos en la carpeta `.dataget/data`, los divide en los conjuntos `training-set` y `test-set`, y carga todas las imágenes en `jpg` de dimensiones `32x32`.


# Starter Code Python
Para iniciar con este reto puedes correr el codigo de Python en Jupyter del archivo `python-sample.ipynb`. Este código que ayudará a cargar y visualizar algunas imágenes. Las dependencias son las mismas que se instalaron durante la descarga de los datos, ver [Requerimientos](#requerimientos).

Para iniciar el código solo hay que prender Jupyter en esta carpeta

```bash
jupyter notebook .
```
y abrir el archivo `python-sample.ipynb`.


[s1]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/airplane4.png "S"
[s2]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/automobile5.png "S"
[s3]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/bird7.png "S"
[s4]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/cat2.png "S"
[s5]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/deer2.png "S"
[s6]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/dog2.png "S"
[s7]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/frog2.png "S"
[s8]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/horse2.png "S"
[s9]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/ship2.png "S"
[s10]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/truck2.png "S"

[s11]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/airplane2.png "S"
[s21]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/automobile7.png "S"
[s31]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/bird5.png "S"
[s41]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/cat3.png "S"
[s51]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/deer6.png "S"
[s61]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/dog5.png "S"
[s71]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/frog8.png "S"
[s81]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/horse9.png "S"
[s91]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/ship4.png "S"
[s101]: https://www.cs.toronto.edu/~kriz/cifar-10-sample/truck6.png "S"


