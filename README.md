# IFT630-SR-docker

Environnement de développement pour les TPs en IFT630

## Utilisation

1. Cloner le répertoire

   ```bash
   git clone https://github.com/gcleroux/IFT630-SR-docker.git
   ```

   ```bash
   cd IFT630-SR-docker
   ```

2. Construire l'image

   ```bash
   docker build -t ift630-docker-env .
   ```

3. Exécutez le conteneur

   ```bash
   docker run -it -v <path-vers-fichiers-TP>:/TP ift630-docker-env
   ```
