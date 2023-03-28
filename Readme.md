# Purpose
Just an MVP to demonstrate:
- Building a simple app that will run in a docker container.
- Having that app use inejected secrets to do something interesting. In this case we reach out to KeyVault to pull secrets which the application needs. 
- How to build images of this service in a Github action and push the artifact to a container repository. In this case it's Dockerhub.

# Generating the key
The process we used to generate the key is as follows:
```bash
ssh-keygen -t rsa -m PEM
# By default the key is generated as ~/.ssh/id_rsa
az keyvault key import --pem-file ~/.ssh/id_rsa --pem-password Password --name my-private-key --vault-name <vault name>
```

This simulates the way we have received keys, which is password protected PEM files. However, since the key content is now stored in KeyVault there is no need for password protection. 

# Injecting runtime values
While there are several ways to get settings into the container runtime, here we have used a Docker env file (not to be confused with the .env file used in Compose). The usage for this is as follows

```bash
docker run --env-file ./env_file -it poc
```
where the env file has the specific settings for your target environment. There is an example in this repo. 