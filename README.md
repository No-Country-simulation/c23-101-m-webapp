# c23-101-m-webapp STOCK APP
## Stack usado
### Backend
- **Python**
- **Django**
- **Django Rest Framewor**

### Frontend
- **HTML**
- **CSS**
  
### Base de Datos
- **MySQL**
  
## Prerequisitos
- **Python 3.8+** (Verifica con `python3 --version` o `python --version`)
- **pip** (Verifica con `pip --version`)
- **venv** ( Herramienta incluida de Python para crear entornos virtuales)

Si falta alguno de estos, instálelo:

### Ubuntu:

- Instala Python, pip, y venv:

    ```bash
    cd stocksApp
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    ```

### 2. Crea y activa un entorno virtual:
```bash
cd stocksApp
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate
```


### 3. Instala  las dependencias
Una vez activas el entorno virtual, instala las dependencias requeridas usando el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
### 3. Corre el servidor
	python stocksApp/manage.py runserver

## Highlights

### Modelos
Los modelos son una parte esencial de Django para crear las tablas de las bases de datos. Con ellos, pudimos agilizar la creación de las tablas para los productos y los usuarios.

![image](https://github.com/user-attachments/assets/35ee4e63-f2cb-46f8-a2a8-8452665d6a14)

![image](https://github.com/user-attachments/assets/37535827-20d4-4851-b577-f1c1da863711)

### Routers
En Django Rest Framework viene incluida una clase que permite crear los endpoints de forma rápida y automática, lo que nos agilizó mucho esa tarea.

![image](https://github.com/user-attachments/assets/918a1063-3426-4872-9e08-c12f7651ae49)

![image](https://github.com/user-attachments/assets/55ce07e2-b6c4-4454-9675-cfcf7ebe4160)

## Conclusiones
El proyecto nos ayudó mucho a mejorar no solo nuestras habilidades técnicas, sino también las blandas. A lo largo de todo el desarrollo, nos enfrentamos a dificultades y problemas que fuimos corrigiendo en equipo, lo que nos permitió mejorar nuestro conocimiento sobre la web y la construcción de APIs. Además, nos hizo crecer en nuestra forma de trabajar, ayudándonos a aprender cómo manejar situaciones complejas y lidiar con un equipo y la presión de entregar un producto. Por todo esto, estamos contentos con el resultado y esperamos que les guste.
