import os
import yaml
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from http.server import BaseHTTPRequestHandler, HTTPServer

def main():
    vault_url = os.environ["VAULT_URL"]
    print("accessing vault at {}".format(vault_url))
    credential = ClientSecretCredential(
        client_id=os.environ["AZURE_CLIENT_ID"],
        client_secret=os.environ["AZURE_CLIENT_SECRET"],
        tenant_id=os.environ["AZURE_TENANT_ID"],
        connection_verify=False
    )
    client = SecretClient(vault_url=vault_url, credential=credential)
    key= client.get_secret(os.environ["PRIVATE_KEY_KEY"]).value    
    print("the private key is {}".format(key))

if __name__ == "__main__":
    main()