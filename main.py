import os
import yaml
from azure.keyvault.keys import KeyClient
from azure.identity import ClientSecretCredential

def main():
    credential = ClientSecretCredential(
        client_id=os.environ["AZURE_CLIENT_ID"],
        client_secret=os.environ["AZURE_CLIENT_SECRET"],
        tenant_id=os.environ["AZURE_TENANT_ID"],
        # connection_verify=False
    )
    vault_url = os.environ["VAULT_URL"]
    print("accessing vault at {}".format(vault_url))
    client = KeyClient(vault_url=vault_url, credential=credential)
    key = client.get_key("my-private-key").key
    print("the private key ID is {}".format(key.kid))

if __name__ == "__main__":
    main()