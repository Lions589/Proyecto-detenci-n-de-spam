# Proyecto de Detección de Spam en Correos Electrónicos

Este proyecto implementa una aplicación web desarrollada en Python utilizando Flask para enviar correos electrónicos. La aplicación analiza los correos utilizando un modelo de inteligencia artificial entrenado para detectar spam y clasificar los correos en "spam" o "ham" (no spam). Los resultados del análisis se guardan en una base de datos SQL Server.

## Características

- Envío de correos electrónicos utilizando la API de Gmail.
- Clasificación automática de los correos electrónicos enviados como "spam" o "ham".
- Almacenamiento de los resultados del análisis en la base de datos correspondiente.
- Entrenamiento del modelo de IA utilizando el dataset público **SpamAssassin**.
- Uso de SQL Server para almacenar los correos electrónicos clasificados.
- Interfaz web desarrollada con Flask.


### Descripción de los Archivos Principales

- **app.py**: Archivo principal que contiene la lógica de la aplicación Flask, la integración con el modelo de machine learning y las funciones para enviar correos electrónicos y almacenar los resultados en la base de datos.
  
- **ml_logic.py**: Contiene la lógica para cargar, procesar y entrenar el modelo de detección de spam utilizando el dataset SpamAssassin.

- **datasets/spamassassin/**: Contiene los subdirectorios con los correos electrónicos de entrenamiento y prueba divididos en las carpetas `easy_ham`, `hard_ham` y `spam_2`.

- **index.html**: Archivo HTML que contiene la interfaz gráfica del usuario (GUI) para enviar correos electrónicos.

## Requisitos

### Instalación

1. Clonar el repositorio.

   ```bash
   git clone https://github.com/usuario/proyecto_correos.git
   cd proyecto_correos
### Crear y activar un entorno virtual.
     python -m venv venv
    source venv/bin/activate  # 
    En Windows: 
    venv\Scripts\activate


    pip install -r requirements.txt

### Configurar las variables de entorno para la conexión con Gmail y la base de datos.

    export GMAIL_USER="tu_email@gmail.com"
    export GMAIL_PASS="tu_contraseña"
    export DB_CONNECTION="mssql+pyodbc://usuario:contraseña@servidor/nombre_base_de_datos"

### Base de Datos
Se utiliza SQL Server para almacenar los correos electrónicos clasificados. Debes tener una base de datos con las tablas:

spam: Para almacenar los correos clasificados como spam.
ham: Para almacenar los correos clasificados como no spam (ham).

## Entrenamiento del Modelo
El modelo de machine learning se entrena utilizando el dataset SpamAssassin. Para entrenar el modelo, asegúrate de que los datos estén en el directorio datasets/spamassassin/. 
El código en ml_logic.py se encarga de cargar y procesar estos datos para entrenar el modelo y guardarlo para el uso posterior en la aplicación web.

### Uso
## Iniciar la aplicación Flask.

    python app.py


## Acceder a la aplicación web desde tu navegador:
    http://localhost:5000

Enviar un correo electrónico desde la interfaz web. El correo será analizado y clasificado como spam o ham, y los resultados se guardarán en la base de datos.

### Tecnologías Utilizadas
Python 3.x
Flask: Framework web utilizado para la interfaz y el backend.
SQL Server: Base de datos relacional para almacenar los resultados del análisis de spam.
scikit-learn: Biblioteca para el entrenamiento del modelo de clasificación de correos electrónicos.
SpamAssassin Public Corpus: Dataset utilizado para entrenar el modelo de IA.
Gmail API: Para el envío de correos electrónicos.

### Próximas Mejoras
Autenticación de usuarios: Implementar un sistema de registro y autenticación para personalizar el envío y análisis de correos.
Mejorar la precisión del modelo: Ajustar los parámetros del modelo para obtener mejores resultados en la clasificación.
Reportes y visualización: Añadir gráficos y estadísticas sobre el rendimiento del sistema de detección de spam.

### Participantes en el proyecto 

Alejandro Argoti, Lizandro Duran, 
Maryuri Rivadeneria, Anthony Lanchi , 
Cristhian Recalde, Bryan Velasco , 
Alexis Velasco, Brandon Nula, Gabriel Salazar.






