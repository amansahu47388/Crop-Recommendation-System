
## Project Requirements

```
Python 3.10 or above
git bash CLI
Visual Studio Code - Code Editor

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
password - `   amansahu9755                  `<br>

###### Create new admin by following command

```
python manage.py createsuperuser
```

