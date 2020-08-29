import pulumi
from pulumi import ResourceOptions
from pulumi_gcp import compute
from network import compute_network, compute_firewall
import pulumi_gcp as gcp


script = """#!/bin/bash
apt -y update
useradd -g users -s `which bash` -m app
apt -y update
apt -y install make apt-transport-https ca-certificates curl git software-properties-common
git clone https://github.com/openware/opendax.git
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
apt -y update
mkdir -p /home/legion/.ssh
chmod 700 /home/legion/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC22PSFCvJxCyh5+OdBXuZ7soeYljNO2q4Rxh3NUuQdVchN+88urpmD++DU4UwoNgc5WQVOHivJljp3EM8JJ497YObu0WIyRnW8+wuv+IL/LiyED8+vEjYVB98kUPE1rv6KOjvztTIISVvTJa9+X7qVE244YX6hqk7iWEauR+aXJcep2RNCKEJK81M+9KfhxZlJbRDgbtNIpVoYI5jDweDlmEPiZf1NIX0nuIt54AnhLQRGpb8HBH6ZC+nET7mlzwPdllv2PgJOmVQ6NdWUoa+lBdjT1DZo+c89evNntUzXreht50I/pnT6nL5GsmQdDu37GxvmoFJd+e0AzVsyGlRXc+ISfsqPia6bzD8kY+kFbHsZLD3nZD+r3dCCtxdfjmEYBlKQ8TKc5QpE9DG6JoYyV92EEzNA2U38Cl25pr8Eom+H4na4LNPK8doU17h8ESG3C3BCGfgkCyjWLdUDdOdCRxgQt17EBN9u9pFgPDYiqDXWkjhSU5Fbi2YJ0ymjz6s= legion@SkyNet" >> /home/legion/.ssh/authorized_keys
chown -R legion:legion /home/legion/.ssh
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
systemctl restart ssh
sudo apt install -y docker-ce
systemctl start docker
systemctl enable docker
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
usermod -a -G rvm docker root
"""
config = pulumi.Config()
instance_name = config.require('instance_name')
zone = config.require('zone_name')
instance_type = config.require('instance_type')
#instance_image = config.require('instance_image')
instance_disk_size = config.require('instance_disk_size')
#instance_disk_size = 300
instance_addr = compute.address.Address("address")
compute_instance = compute.Instance(
    "instance",
    name=instance_name,
    machine_type=instance_type,    # "n1-standard-2",
    boot_disk={
        "initializeParams": {
            "image": "debian-cloud/debian-10-buster-v20200805",
            "size" : instance_disk_size,
        }
    },
    tags=[
        "instance",
        instance_name,
    ],
    network_interfaces=[
        {
            "network": compute_network.id,
            "accessConfigs": [{
                "nat_ip": instance_addr.address
            }]
        }],
    service_account={
        "scopes": ["https://www.googleapis.com/auth/cloud-platform"],
    },
    zone=zone,
    opts=ResourceOptions(depends_on=[compute_firewall]),
    metadata_startup_script=script,
)

pulumi.export("instanceName", compute_instance.name)
pulumi.export("instanceStatus", compute_instance.current_status)
pulumi.export("instanceInstanceId", compute_instance.instance_id)
pulumi.export("instance_network", compute_instance.network_interfaces)
pulumi.export("instance_external_ip", instance_addr.address)
pulumi.export("instance_external_ip", instance_addr.address)
pulumi.export("cpu_platform", compute_instance.cpu_platform)
pulumi.export("compute_firewall", compute_firewall.id)


