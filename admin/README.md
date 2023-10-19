# ADMIN
## Variables de entorno
La aplicación necesita que las siguientes variables de entorno estén definidas:

### Base de datos
- DB_USER (valor recomendado "postgres")
- DB_PASS (valor recomendado "postgres")
- DB_HOST (valor recomendado "localhost")
- DB_NAME (valor recomendado "grupo32")
- DB_PORT (valor recomendado 5432)


## Inicialización
Una vez que están definidas las variables de entorno necesarias, se puede crear una base de datos usando docker compose con el siguiente comando:
```sh
docker-compose up -d
```
> Nota: En caso de no lograr conectar a la base de datos una vez creada, si se está usando colima u otra variante de docker, revisar si es necesario que DB_HOST esté asignado a la IP de la máquina virtual en lugar de usar localhost.

Para recrear la base de datos, ejecutar
```sh
flask resetdb
```

Para volcar el contenido de seeds a la base de datos, ejecutar
```sh
flask seedsdb
```

## How to run the app:
admin> poetry shell
Spawning shell within C:\Users\fran_\AppData\Local\pypoetry\Cache\virtualenvs\web-EV70jHJ_-py3.8
admin> flask run
admin> flask --debug run

Git logs in graph:
git log --pretty=oneline --graph

Acceso a db:
Contraseña abc123
Puerto 5432

## How debut .lock and .toml after merge:
Remove .lock
admin> Poetry add "new dependencies"
admin> Poetry install

### set poetry env var: 
set DB_USER=postgres
set DB_PASS=abc123
set DB_NAME=grupo32
set DB_PORT=5432

### Servidor de emails:
Para que funcione el server de correos (exclusivamente Gmail), deben también configurarse las siguientes variables de entorno (completar con valores luego del signo "=" ).

set APP_EMAIL_ADDRESS=
set APP_EMAIL_PASSWORD=
set APP_BASE_URL=
