# ift630-docker-env

Environnement de développement pour les TPs en IFT630.

## To-do

- [ ] Support pour GPU Nvidia avec OpenCL
- [ ] Tests intégrés pour OpenCL nvidia

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

### Utilisation GPU avec OpenCL

**Ce conteneur supporte uniquement les GPU intel pour l'instant**

Les fonctionnalités OpenCL et GPU ne sont pas testées automatiquement lors du
déploiement de l'image, puisque GitHub n'offre pas encore de runner avec GPU
(autre que les self-hosted runner). Il est fortement recommandé de tester votre
architecture localement afin de vous assurer votre GPU est supportée. Plus
d'information est disponible dans la section [Build from source](#build-from-source).

#### GPU intel

Pour relier votre GPU intel au conteneur, utilisez cette commande:

```bash
docker run --device /dev/dri:/dev/dri -it -v <path-vers-fichiers-TP>:/TP gcleroux/ift630-docker-env
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

   Pour l'utilisation d'une GPU avec le conteneur, vous pouvez vous référer
   à la section [Utilisation GPU avec OpenCL](#utilisation-gpu-avec-opencl)

#### Test support GPU intel

Afin de voir si votre GPU intel est supportée par le conteneur, utilisez les
commande suivante:

```bash
# Build
docker compose build
```

```bash
# Run tests
docker compose run test-intel
```
