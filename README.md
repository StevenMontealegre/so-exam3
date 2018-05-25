# so exam-3
Nombre: James Steven Montealegre Gutiérrez  
Código: A00014976  
Asignatura: Sistemas operacionales  
Correo personal: steven.montealegre91@gmail.com  
URL repositorio: https://github.com/StevenMontealegre/so-exam3  

## III. Servicio web en flask con estructura vista en clase:  
Debemos crear un servicio virtualizado (flaskdev) junto con 2 archivos requeridos para ese ambiente virtual (requirements_dev.txt y requirements.txt). Seguido, debemos crear una carpeta que llevará el nombre op_stats, en donde estará localizado el archivo python stats.py, este será el encargado de arrojar el estado de nuestra máquina: CPU, MEMORY y HARD DISK.  
continuación creamos otro archivo (app.py) el cual contiene los métodos para la ejecución del servicio.  
* (_los códigos utilizados se encuentran en el fichero: Códigos_python.txt_)  

Finalmente, ejecutamos el comando python [_op_stats/app.py_] y con ayuda de POSTMAN realizamos peticiones http, con lo cual, tenemos los resultados de nuestro sistema de cómputo:   
![](imagenes/Captura%20de%20pantalla%20(26).png)  
![](imagenes/Captura%20de%20pantalla%20(27).png)  
![](imagenes/Captura%20de%20pantalla%20(28).png)  

Podemos evidenciar las peticiones que se hicieron y la respuesta del servidor:  
![](imagenes/Captura%20de%20pantalla%20(29).png)  

## III. Implementación de las pruebas unitarias empleando Fixtures y Mocks:  
Creamos una carpeta con un nombre alusivo a la actividad que realizaremos por ejemplo, test. Dentro de esta carpeta estará un archivo llamado _test_stats.py_, este es requerido para ejecutar las pruebas del servicio. Seguido ejecutamos el comando pytest -v para correr las pruebas.  
* (_los códigos utilizados se encuentran en el fichero: Códigos_python.txt_)  

![](imagenes/Captura%20de%20pantalla%20(30).png)  



 

