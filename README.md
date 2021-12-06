#*Proyecto Integrador///*

######*Jose Luis Hernandez Hurtado* | **A01365190**
######*Ricardo Adolfo Gonzalez Teran* | **A01769410**
######*Diego Bahena Hernandez* | **A01367116**

###**Cambios al diagrama de clases**

  El aeropuerto ahora tiene una clase de agregación AeropuertoAD es de tipo agregación ya que el Aeropuerto
  puede existir sin tener pilotos, copilotos, asistentes, pasajeros, etc.

  La clase CSV se encarga de juntar todas las estadisticas y escribirlas al archivo csv correspondiente.

###**Cambios en el programa**

  Se agrego un menu para cada opcion de edicion como de agregacion, esto con el fin de facilitarle al usuario sus interacciones con el programa, las funciones incluyen cosas como regresar a menus anteriores, seleccionar el aspecto que se quiere editar, etc.

  Junto con el menu se implementaron funciones de validaciones de respuestas por parte del usuario, esto para garantizar una respuesta ante cualquier entrada que de el usuario.
  En adicion a esto, tambien se implemento un diccionario que dependiendo el numero de entrada que de el usuario ejecutara el metodo deseado, esto con el fin de que las cosas sean mas ordenadas y que tengan un mejor entendimiento en el codigo fuente.

###**Logica del Programa**

  El programa funciona de manera que al iniciar, al usuario se le muestra un menu con opciones para editar cierta informacion de la poblacion de un aeropuerto, parte de la poblacion se componen de asistentes, pilotos, pasajeros, etc. Cuando el usuario selecciona un puesto se le da un menu de informacion que puede ser editada al gusto del usuario, esto igual incluye ciertas limitaciones, ya que al editar la informacion el programa se serciora de que la nueva informacion introducida tenga logica con el aspecto que se esta queriendo editar. Toda la informacion, tanto la predeterminada como la sobreescribible se alamcena en objetos, dichos objetos tienen un identificador para hacer mas facil la localizacion del mismo, esto ayuda a que el usuario sepa que la persona que quiera editar exista en la base de datos.

  Una vez que el usuario termina de editar la informacion deseada, se muestra el menu principal, en el cual se incluye una opcion para salir del programa, cuando el usuario selecciona la opcion de salida, el programa sobreescribe la informacion previamente editada y la guarda en la base de datos, una vez hecho esto, se calculan ciertas estadisticas sobre el aeropuerto y se escriben en un archivo denominado por comas (.csv) en el cual cualquier usuario puede leer y ocupar la informacion de una manera mas facil.

###**Justificaciones**

####*CSV*:

  Se hizo el uso de archivos con extension ".csv" porque resulta mas facil la lectura del archivo sin depender de un sistema opertaivo (ej. Windows, MacOS, Linux) en especifico, estos tipos de archivos se adaptan al programa que se use y muestran la informacion ordenada y sin errores de edicion, todo esto mientras se utilice un programa que muestra hojas de claculo con celdas.

####*Estructura de datos*

  La estructura de la base de datos se basa en diccionarios de objetos, esto con el fin de que sea mas eficiente y mas facil identificar aspectos sobre la poblacion del aeropuerto y los componentes del mismo, igualmente ayuda a que la informacion este mejor ordenada y no genere confusiones

####*Multiples menus*

  Utilizamos multiples menus para crear una mejor experiencia de interaccion con el usuario, permitiendole elejir a voluntad los aspectos que desea editar e irse desplazando entre el programa de una manera mas estetica y eficiente

##**Datos finales de funcionamiento**

####*Clases*

  Se utilizaron clases para cada tipo de poblacion del aeropuerto, en las cuales se cuenta con su informacion personal (atributos), y su papel que tienen en el aeropuerto, ademas se agregaron metodos para realizar cambios y registrar a nueva poblacion (ya sea pasajeros, pilotos, asistentes, etc.)

  Como ultimo dato, se tiene 1 superclase llamada "Airport" que engloba toda la poblacion y componentes del aeropuerto, primeramente contiene datos predeterminados para hacer pruebas y despues tiene un metodo para cargar los datos de la poblacion en memoria

####*Modularizacion*

  Se agrego una clase que modifica los datos, esto con el fin de que el programa se modularize de una manera mas eficiente, y a la vez sea mas facil de editar el programa como para interpretarlo por parte del desarrollador.

####*Main*

  En el programa principal, especificamente en el main (proyect.py), se agregaron ciclos while para validar las opciones de entrada del usuario, esto con el fin de tener una respuesta de salida en todos los casos de entradas posibles, si el usuario mete una opcion invalida se le pedira de nuevo la entrada hasta que sea valida.
