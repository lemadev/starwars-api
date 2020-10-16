# starwars-api

App que consume recursos de [SWAPI (the star wars api)](https://swapi.dev/)
La aplicación devuelve información del character ingresado. También se puede ingresar un id de personaje y su respectivo
rating. Una vez ingresado, en cada request, va a devolver el mayor rating y el rating promedio.

### Build en docker

```
docker-compose build
docker-compose up
```

### endpoints
##### Obtener character 
```
character/id
```
##### Insertar id_personaje y su respectivo rating
```
character/id/rating
```