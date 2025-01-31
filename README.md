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
- **Python 3.8+** (Check with `python3 --version` or `python --version`)
- **pip** (Check with `pip --version`)
- **venv** (Python's built-in virtual environment tool)

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
Once the virtual environment is activated, install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
### 3. Corre el servidor
	python stocksApp/manage.py runserver

## Highlights

##Conclusiones
