## Anible-azure-big-ip

This solution uses Ansible "azure_rm_deployment" module to launch a standalone 3-NIC BIG-IP VE in Microsoft Azure from the following ARM template https://github.com/F5Networks/f5-azure-arm-templates/tree/v9.5.0.0/supported/standalone/3nic/existing-stack/payg

## Version

This template is tested in the following version: Annsible 2.9.1

## Prerequisites

Since this is existing stack deployment, Resource Group, VNet, and subnets needs to be created in advance Azure. Alternatively, these resources can be created using create-rg.yaml playbook from the current directory.

Make sure that file https://raw.githubusercontent.com/F5Networks/f5-azure-arm-templates/v9.5.0.0/supported/standalone/3nic/existing-stack/payg/azuredeploy.json can be fetched from Ansible host where you run azure-arm-3nic-payg-UK-South.yaml playbook.

## Installation

```
git clone https://github.com/y-myk/Ansible.git
cd Ansible/Azure/standalone/3NIC/PAYG
```

Modify Resource group name/vnet name/subnet names and other template parameter in arm-template-vars.yaml file (Varibles from this file are used in create-rg.yaml and in azure-arm-3nic-payg-UK-South.yaml playbooks). Then run:

```
ansible-playbook main.yaml -v
```

## Authentication

This solution requires access to the Azure API.

Ansible supports a number of different methods for authenticating to Azure: https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html#authenticating-with-azure. This solution relies on authenticating to Azure using service principal credentials. Microsoft tutorial describing how to create a service principal: https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal. After stepping through the tutorial you will have:

- Client ID
- Secret key
- tenant ID

Provide values to service principal credentials variables in /root/azure_creds.yaml file. Varibles from this file are used in create-rg.yaml and in azure-arm-3nic-payg-UK-South.yaml playbooks.
