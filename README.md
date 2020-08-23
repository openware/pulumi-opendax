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



Google Cloud Platform Resource Provider package is available in many languages in the standard packaging formats.

Node.js (Java/TypeScript)
To use from JavaScript or TypeScript in Node.js, install using either npm:

# npm install @pulumi/gcp
or yarn:

# yarn add @pulumi/gcp
Python
To use from Python, install using pip:

# pip install pulumi_gcp
Go
To use from Go, use go get to grab the latest version of the library

# go get github.com/pulumi/pulumi-gcp/sdk/v3
.NET
To use from .NET, install using dotnet add package:

# dotnet add package Pulumi.Gcp

### Run project
1.Install Pulumi on Linux by running the installation script:  
# curl -fsSL https://get.pulumi.com | sh

1.create first projekt:
# mkdir quickstart && cd quickstart
# pulumi new gcp-python

Let’s review some of the generated project files:

Pulumi.yaml defines the project.
Pulumi.dev.yaml contains configuration values for the stack we initialized.
__main__.py is the Pulumi program that defines our stack resources. Let’s examine it.


1.Let’s go ahead and deploy the stack:
# pulumi up -y

1.To destroy resources, run the following:
# pulumi destroy -y

1.To delete the stack itself, run pulumi stack rm. Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.
# pulumi stack rm

-------------

In order to use tf2pulumi to convert a Terraform project to Pulumi TypeScript and then deploy it, you'll first need to install the Pulumi CLI. Once the Pulumi CLI has been installed, navigate to the same directory as the Terraform project you'd like to import and create a new Pulumi TypeScript stack:
#  tf2pulumi
