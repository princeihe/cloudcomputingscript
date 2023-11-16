import requests
import json

url = "https://management.azure.com/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/vm4?api-version=2023-07-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQwZTZlZTE5LWEyYTctNDY4ZC05NjM3LTFkZTQ3YjNhMmIwNC8iLCJpYXQiOjE3MDAxNDQwODIsIm5iZiI6MTcwMDE0NDA4MiwiZXhwIjoxNzAwMTQ4NjA0LCJhY3IiOiIxIiwiYWlvIjoiQVlRQWUvOFZBQUFBTmVMZW9Wd2RwR1dBYUZFRXFvRnhxQzA4NlVMZTJrRnZ4ZW9JalB6enZFRGc4ME43RjB5MXpaN1BFd1ExbzN6QVJodElIV3A4VklTSVpSVm5BZWZ6d3lyY3dZaTN3dVVGYVk0ZlBwME8wblgwNFEyM2RVenp3dlZ2Y0JIbUNQMVNKZGkvaSs5M0hIaGViaW50WjVOdzBOMU12ODBOQUx6b3A4N1QzNGxNajNnPSIsImFsdHNlY2lkIjoiMTpsaXZlLmNvbTowMDAzMDAwMDY0RDU0OEU0IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImVtYWlsIjoicHJpbmNlaWhlMTIzQGdtYWlsLmNvbSIsImZhbWlseV9uYW1lIjoiSWhla3dlcmVtZSIsImdpdmVuX25hbWUiOiJQcmluY2UiLCJncm91cHMiOlsiMmFhYzk4MDEtMjcyOS00ZjAxLWFlNzUtZTBiZWY5MjAwYzIyIl0sImlkcCI6ImxpdmUuY29tIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTQ3LjI1Mi4xOS4xNzQiLCJuYW1lIjoiUHJpbmNlIEloZWt3ZXJlbWUiLCJvaWQiOiI3Y2M2MDlmMS1jMzBjLTQ3ODQtOGQzOC1jMjI4NDRmYTg1ZGQiLCJwdWlkIjoiMTAwMzIwMDMwRkRGQkFGNSIsInJoIjoiMC5BYTRBR2U3bVFLZWlqVWFXTngza2V6b3JCRVpJZjNrQXV0ZFB1a1Bhd2ZqMk1CT3JBTk0uIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiczVNSk5CMzl6TjRXZHVMNVlLcDBNWVNtbEw0RVNqUEkwSE9nNlo1RGpfdyIsInRpZCI6IjQwZTZlZTE5LWEyYTctNDY4ZC05NjM3LTFkZTQ3YjNhMmIwNCIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jcHJpbmNlaWhlMTIzQGdtYWlsLmNvbSIsInV0aSI6IjBsa0dYNTBhUzBhNWNyaFplYnNOQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNjk5MjcwMzQ5fQ.OS8bMa8AgJGUIAhCY5jNUdvj7efTpynywAotJbUtFM3ufX6nn3Fwn8Hyr78G6d-6H6U3GdYsEGRqQHLtKOg-ifi9QVRMmgZZTbX9nusnbZRu0IUaTPyvgoW4UghAXoPjUDe3FO_DQild_nXOCk_1nDztQvaUGVZF2l4nswipwkTO81XgBCqjqxCMqf6bEtGXsjqS0U7mAQUj9sxzmvqCBNK-FpqfHs7CY68BwEcxnkuXZ0s3yGEoZcJIfnKWSVXyakG0NnXfgkKC3ZnGgKABv6YoWf9oDbxnGZcemG83bfsUKwzD6SRrg0ME5J5IKsdXEuk6F3VIt0JMyk3H_e4Gzg'

}

data = {
    "id": "/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Compute/virtualMachines/vm4",
    "type": "Microsoft.Compute/virtualMachines",
    "properties": {
      "osProfile": {
        "adminUsername": "paul",
        "secrets": [
          
        ],
        "computerName": "vm4",
        "linuxConfiguration": {
          "ssh": {
            "publicKeys": [
              {
                "path": "/home/paul/.ssh/authorized_keys",
                "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsxP2gmr2VhefmSeB07WtVpOP3IquuVmGgx23jjW7i hA+rJjsUnEA/ uf5a9Qr5tvA3fDlaADTKOn8A54j2KVut1My4soro4YL5ziyiIYjzcn9CCI7EUscB41f1vNQqGuhvJot2 UB4mKRLDgJgtCUzM5jm5Su32yJQa1Zybl9uxyU/ BFnK3JFiynoMl30ADbZYBz6owc4+yFJDy46l0SiAiOJRKlPQmrH10YMnWQyiFrON07b2RJRyPr80 QXt9t+ynWGwJeO5nv1WQZirNVuzze1yWCQtQ8L3ySFSj9LA3Xw2n34NEWUvK6PMGmJf1+Fnx jVzC6KxExKkglXXfcv8N9 paul@paul "
              }
            ]
          },
          "disablePasswordAuthentication": True
        }
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4",
            "properties": {
              "primary": True
            }
          }
        ]
      },
      "storageProfile": {
        "imageReference": {
          "sku": "16.04-LTS",
          "publisher": "Canonical",
          "version": "latest",
          "offer": "UbuntuServer"
        },
        "dataDisks": [
          
        ]
      },
      "hardwareProfile": {
        "vmSize": "Standard_D1_v2"
      },
      "provisioningState": "Creating"
    },
    "name": "vm4",
    "location": "westeurope"
  }

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())