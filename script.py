import requests
import json

# Replace these values with your actual credentials and details
subscription_id = '0c1e4b5e-1263-48f1-b7cf-2a4715eebc20'
resource_group = 'lab4'
location = 'westeurope'
access_token = 'your_access_token'

# Function to deploy a resource
def deploy_resource(api_url, resource_payload):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.put(api_url, headers=headers, json=resource_payload)
    print(response.json())

# 1. Deploy Public IP Address
public_ip_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/publicIPAddresses/ip4?api-version=2023-05-01'
public_ip_payload = {
    location: "westeurope"
}
deploy_resource(public_ip_url, public_ip_payload)

# 2. Deploy Network Interface Card (NIC)
nic_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/networkInterfaces/nic4?api-version=2023-05-01'
nic_payload = {
    "properties": {
        "ipConfigurations": [
            {
                "name": "ipconfig1",
                "properties": {
                    "publicIPAddress": {
                        "id": "/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Network/publicIPAddresses/ip4"
                    },
                    "subnet": {
                        "id": "/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4"
                    }
                }
            }
        ]
    },
    "location": "westeurope"
}
deploy_resource(nic_url, nic_payload)

# 3. Deploy Virtual Machine
vm_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/vm4?api-version=2023-07-01'
vm_payload = {
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
          "disablePasswordAuthentication": true
        }
      },
      "networkProfile": {
        "networkInterfaces": [
          {
            "id": "/subscriptions/0c1e4b5e-1263-48f1-b7cf-2a4715eebc20/resourceGroups/lab4/providers/Microsoft.Network/networkInterfaces/nic4",
            "properties": {
              "primary": true
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
deploy_resource(vm_url, vm_payload)
