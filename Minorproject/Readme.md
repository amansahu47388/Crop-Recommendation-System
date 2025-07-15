#### Crop Recommendation System

## Project Requirements

```
8 GB RAM   <br>
Code Editor VSCode / Pycharm   <br>
Git CLI<br>
Web Browser Chrome / Edge   <br>
python 3.12.4   <br>

```


## Project Setup : 

#### Open git bash and run the following commands

###### Clone the project
```
git clone https://github.com/amansahu47388/Minor-Project-1.git
```

###### Change Directory
```
cd crop_recommendation_system/
``` 

###### Prepare Python virtual environment
```
python -m venv env
```

###### Open vscode by this command
```
code .
```


#### Start new terminal in vscode and run following commands

###### Activate venv if not acivated automatically
```
.\env\Scripts\activate
```

###### Download all Dependencies
```
pip install -r requirements.txt
```

###### Switch to the project
```
cd CRS
```

##### Run commands for migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```


#### Run this commands to start Django server

```
python manage.py runserver
```

#### Admin Credentials to login in Django Admin Panel

username - `   amansahu47388@gmail.com       `<br>
password - `   Aman@9755                  `<br>

###### Create new admin by following command

```
python manage.py createsuperuser
```

##### Setup Environment Variables in `.env` file under `Crop_recommendation_system/`
```
# django settings
DEBUG_MODE = TRUE
ALLOWED_HOSTS = 'localhost:8000 127.0.0.1:8000 '
SECRET_KEY = ''
```


##### Run the Project
```
cd .\crop_recommendation_system\
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


#### Update the Code
- `Reach the crop_recommendation_system directory first`<br>

```
git pull
.\env\Scripts\activate
pip install -r requirements.txt
cd .\crop_recommendation_system\
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
