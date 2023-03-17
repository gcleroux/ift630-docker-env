# Environnement de développement IFT630

## Utilisation

### Image docker Hub

Deux images sont fournies sur [dockerHub](https://hub.docker.com/repository/docker/gcleroux/ift630-docker-env/general).

- gcleroux/ift630-docker-env:intel
- gcleroux/ift630-docker-env:nvidia

Il est possible de relier votre GPU au conteneur pour faire de la programmation
avec OpenCL. Pour l'instant, uniquement les GPU Intel et Nvidia sont supportées.
Les GPU AMD ne sont pas testées puisque je n'en ai pas à ma disposition.

Si vous ne savez pas quelle image prendre ou que vous ne souhaitez pas relier
de GPU au conteneur, je recommande l'image `intel` par défaut.

Pour récupérer l'image, utilisez la commande suivante:

```bash
docker pull gcleroux/ift630-docker-env:intel
```

Par la suite, vous pouvez exécuter le conteneur avec la commande suivante:

```bash
docker run -it -v <path-vers-fichiers-TP>:/TP gcleroux/ift630-docker-env:intel
```

### Utilisation GPU avec OpenCL

**L'environnement de développement supporte uniquement les GPU intel/nvidia**

Les fonctionnalités OpenCL et GPU ne sont pas testées automatiquement lors du
déploiement de l'image, puisque GitHub [n'offre pas encore de runner avec GPU](https://github.com/github/roadmap/issues/505).
Il est fortement recommandé de tester votre architecture localement afin de vous
assurer votre GPU est supportée. Plus d'information est disponible dans la section
[Test OpenCL](#test-opencl-avec-support-gpu).

#### GPU Intel

Pour relier votre GPU Intel au conteneur, utilisez cette commande:

```bash
docker run --device /dev/dri:/dev/dri -it -v <path-vers-fichiers-TP>:/TP gcleroux/ift630-docker-env:intel
```

#### GPU Nvidia

Afin de relier votre GPU au conteneur, il faut d'abord que vous ayez installé le
`nvidia-container-runtime` sur votre distribution. Les instructions pour l'installation
se trouvent [ici](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

Pour relier votre GPU Nvidia au conteneur, utilisez cette commande:

```bash
docker run --runtime=nvidia --gpus all -it -v <path-vers-fichiers-TP>:/TP gcleroux/ift630-docker-env:nvidia
```

## Build from source

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
   docker compose build
   ```

3. Exécutez le conteneur

   ```bash
   docker compose run intel
   ```

   ```bash
   docker compose run nvidia
   ```

   Pour relier vos fichiers locaux dans le conteneur, vous pouvez ajouter leur emplacement
   dans la fichier `docker-compose.yml` dans l'étiquette `volumes` prévue à cet effet.

### Test OpenCL avec support GPU

Afin de voir si votre GPU est supportée par le conteneur, utilisez les
commande suivante:

```bash
# Build
docker compose build
```

#### Intel

```bash
docker compose run test-opencl-intel
```

#### Nvidia

```bash
docker compose run test-opencl-nvidia
```
