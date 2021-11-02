# Flask API Development
## Create Python Virtual Enviournment
```
virtualenv venv <--python=python3.5>
```

## Activate in windows
```
cd ./venv/Scripts/activate.bat
```


## All enviourment list
```
conda info --envs
```

## all librabry installed in Enviournment
```
pip freeze
```

## Activate Env
```
activate <Env_name>
```

## Deactivate Env
```
deactivate <Env_name>
```


# Git Command

## SSH Key Generation
```
ssh-keygen
```


# Heroku Command
Add Procfile ,requirements.txt ,runtime.txt ,uwsgi.ini Files to Deploy in Heroku
```
heroku login
heroku logs --app=flask-item-api
```