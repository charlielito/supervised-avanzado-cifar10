# Reto CIFAR-10
## Descripción
El [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) es un conjunto de 60000 imágenes a color de 10 distintas categorías. Las categorías son: avión, automovil, pájaro, gato, venado, perro, rana, caballo, barco y camión. El tamaño por defecto es 32x32 pixeles.

![alt text][s1] ![alt text][s2] ![alt text][s3] ![alt text][s4] ![alt text][s5] ![alt text][s6] ![alt text][s7] ![alt text][s8] ![alt text][s9] ![alt text][s10]

![alt text][s11] ![alt text][s21] ![alt text][s31] ![alt text][s41] ![alt text][s51] ![alt text][s61] ![alt text][s71] ![alt text][s81] ![alt text][s91] ![alt text][s101]

El reto es construir un clasificador de imágenes que sea capaz de reconocer las 10 categorías.

### Objetivo
1. Crear un algoritmo que tome una imagen de entrada, ya sea como vector o matriz, y retorne el clase (`class_id`) a la que pertenece esa imagen.
1. Entrenar este algoritmo utilizando los datos de la carpeta `data/training-set`.
1. Medir el performance/score del algoritmo utilizando los datos de la carpeta `data/test-set`. El performance debe ser medido como
```python
score = n_aciertos / n_imagenes * 100
```
donde `n_aciertos` es el numero de imagenes clasificadas de forma correcta y `n_imagenes` es el numero total de imagenes en el `test-set`.

### Requerimientos
Clona este repositorio y ejecuta el commando
```bash
git checkout red-fire
```
Despues puedes instalar los requirementos fácilmente utilizando el commando

```bash
pip install -r requirements.txt
```
Dependiendo de tu entorno puede que necesites instalar paquetes del sistema adicionales, si tienes problemas revisa la documentación de estas librerías.

### Descarga y Preprocesamiento
Para descargar los datos ejecuta el comando
```bash
dataget get --dont-process cifar10
```
Esto descarga los archivos en la carpeta `.dataget/data`, los divide en los conjuntos `training-set` y `test-set`, las cuales tienen imágenes en `jpg` de dimensiones `32x32`.

### Método
##### Modelo
Se utilizó una Red Neuronal Convolucional con la siguiente arquitectura:

* Inputs: 3 filtros (RGB)
* Capa Convolucional: 96 filtros, kernel 7x7, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 16, filtros expand-1x1 64, filtros expand-3x3 64, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 16, filtros expand-1x1 64, filtros expand-3x3 64, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 32, filtros expand-1x1 128, filtros expand-3x3 128, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 32, filtros expand-1x1 128, filtros expand-3x3 128, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 48, filtros expand-1x1 192, filtros expand-3x3 192, padding 'same', funcion de activacion ELU
* Max Pooling: kernel 3x3, stride 2, padding 'same'
* Capa Fire: filtros sequeez 48, filtros expand-1x1 192, filtros expand-3x3 192, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 64, filtros expand-1x1 256, filtros expand-3x3 256, padding 'same', funcion de activacion ELU
* Capa Fire: filtros sequeez 64, filtros expand-1x1 256, filtros expand-3x3 256, padding 'same', funcion de activacion ELU
* Capa Convolucional: 43 filtros, kernel 1x1, padding 'same', funcion de activacion lineal
* Average Pooling: kernel 16x16, stride 1
* Flatten: se convierte a vector de 43 dimensiones
* Softmax: funcion de activacion softmax directamente sobre flatten

###### Parámetros
Este modelo utiliza `757,483` parametros.

##### Entrenamiento
Se utilizó un Stocastic Gradient Descent con los siguentes parámetros

* Optimizador: ADAM
* Learning Rate: 0.001
* Batch Size: 64

##### Notas
No se intentó optimizar el modelo de ninguna manera, en especial:

* No se preprocesaron los datos de ninguna manera excepto estandarizar su tamaño de las imagenes a `32x32`

### Procedimiento
El modelo se encuentra en el archivo `model.py`. Para entrenarlo ejecuta el comando
```
python train.py
```
Este script realiza lo siguiente

* Utiliza `seed = 32` para controlar la aleatoreidad y que los resultados sean reproducibles
* Entrena el modelo por `16000` iteraciones
* Graba el modelo en los archivos `basic-conv-net.tf.*`


### Resultados
Ver el score del `test-set` ejecuta
```
python test.py
```

Resultado: **0.7787**


### Visualización
El cuaderno de jupyter `solucion.ipynb` incluye visualizaciones de algunos resultados, para verlo ejecuta el comando
```bash
jupyter notebook .
```
y abrelo desde el explorador de archivos de jupyter.




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
