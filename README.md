# pulumi-opendax
Demo deployment system with pulumi

## System overview

Pulumi must create :
 * a dedicated Network
 * a dedicated Firewall
 * a Virtual machine 8GB - 4 cores
 * a Cloud SQL (MySQL)
 
### Level 1:

Then install ruby, docker, docker-compose, OpenDAX
Start up the containers

### Level 2:

Do not use the docker MySQL but use the deployed Cloud SQL.


1.Install Pulumi on Linux by running the installation script:  
curl -fsSL https://get.pulumi.com | sh

1.create first projekt
mkdir quickstart && cd quickstart
pulumi new gcp-python

Let’s review some of the generated project files:

Pulumi.yaml defines the project.
Pulumi.dev.yaml contains configuration values for the stack we initialized.
__main__.py is the Pulumi program that defines our stack resources. Let’s examine it.


1.Let’s go ahead and deploy the stack:
pulumi up -y

1.To destroy resources, run the following:
pulumi destroy -y

1.To delete the stack itself, run pulumi stack rm. Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.
pulumi stack rm

