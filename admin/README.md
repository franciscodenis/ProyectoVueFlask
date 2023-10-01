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
