# so exam-3
Nombre: James Steven Montealegre Gutiérrez  
Código: A00014976  
Asignatura: Sistemas operacionales  
Correo personal: steven.montealegre91@gmail.com  
URL repositorio: https://github.com/StevenMontealegre/so-exam3  

## III. Servicio web en flask con estructura vista en clase:  
Debemos crear un servicio virtualizado (flaskdev) junto con 2 archivos requeridos para ese ambiente virtual (requirements_dev.txt y requirements.txt). Seguido, debemos crear una carpeta que llevará el nombre op_stats, en donde estará localizado el archivo python stats.py, este será el encargado de arrojar el estado de nuestra máquina: CPU, MEMORY y HARD DISK.  
continuación creamos otro archivo (app.py) el cual contiene los métodos para la ejecución del servicio.  

Finalmente, ejecutamos el comando python [_op_stats/app.py_] y con ayuda de POSTMAN realizamos peticiones http, con lo cual, tenemos los resultados de nuestro sistema de cómputo:   
![](imagenes/Captura%20de%20pantalla%20(26).png)  
![](imagenes/Captura%20de%20pantalla%20(27).png)  
![](imagenes/Captura%20de%20pantalla%20(28).png)  

Podemos evidenciar las peticiones que se hicieron y la respuesta del servidor:  
![](imagenes/Captura%20de%20pantalla%20(29).png)  

## IV. Implementación de las pruebas unitarias empleando Fixtures y Mocks:  
Creamos una carpeta con un nombre alusivo a la actividad que realizaremos por ejemplo, test. Dentro de esta carpeta estará un archivo llamado _test_stats.py_, este es requerido para ejecutar las pruebas del servicio. Seguido escribimos en consola el comando pytest -v para correr las pruebas.  

![](imagenes/Captura%20de%20pantalla%20(30).png)  

## V. Servicio de integración para la pruebas unitarias:  
Creamos un archivo llamado tox.ini en el cual estarán localizados la información básica del proyecto y las pruebas que se quieran ejecutar. Enfatizamos el lenguaje a usado, el comando a ejecutar, las librerias y las dependencias:   
Finalmente se muestra los resultados de la ejecución (para ello se ejecuto el comando tox -e pytest)  
![](imagenes/Captura%20de%20pantalla%20(31).png)  

En ultima instancia se crea un archivo .travis.yml, en el cual agregamos el directorio raíz del repositorio (formato YAML). este archivo especifica entre otras cosas, el lenguaje de programación utilizado y el entorno de construcción. Para cuando se ha activado Travis CI en un repositorio en GitHub, se notificarán los nuevos cambios. También Travis puede limitar la ejecución para un branch específico. Travis CI revisará la rama y ejecutará los comandos especificados en .travis.yml.  
![](imagenes/Captura%20de%20pantalla%20(32).png)  
![](imagenes/Captura%20de%20pantalla%20(33).png)  
![](imagenes/Captura%20de%20pantalla%20(34).png) 

## Observación:  
* (_los códigos utilizados se encuentran en el fichero: Códigos_python.txt_)  






 

