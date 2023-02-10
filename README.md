# ift630-docker-env

Environnement de développement pour les TPs en IFT630.

## To-do

- [ ] Support pour GPU nvidia avec OpenCL
- [ ] Tests intégrés pour OpenCL
- [ ] README sur dockerHub

## Utilisation

### Image docker Hub

Une image est fournie sur [dockerHub](https://hub.docker.com/repository/docker/gcleroux/ift630-docker-env/general).

Pour récupérer l'image, utilisez la commande suivante:

```bash
docker pull gcleroux/ift630-docker-env
```

Par la suite, vous pouvez exécuter le conteneur avec la commande suivante:

```bash
docker run -it -v <path-vers-fichiers-TP>:/TP gcleroux/ift630-docker-env
```

### Build from source

Si vous souhaitez bâtir l'image à partir de la source, vous pouvez suivre les
instructions suivantes:

1. Cloner le répertoire

   ```bash
   git clone https://github.com/gcleroux/ift630-docker-env.git
   ```

   ```bash
   cd ift630-docker-env
   ```

2. Construire l'image

   ```bash
   docker build -t ift630-docker-env .
   ```

3. Exécutez le conteneur

   ```bash
   docker run -it -v <path-vers-fichiers-TP>:/TP ift630-docker-env
   ```
