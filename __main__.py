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
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm reinstall ruby-2.6.5
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt -y update
sudo apt install -y docker-ce
systemctl start docker
systemctl enable docker
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
usermod -aG docker $USER
"""

instance_disk_size = 300
instance_addr = compute.address.Address("address")
compute_instance = compute.Instance(
    "instance",
    name="opendax",
    machine_type="n1-standard-2",
    boot_disk={
        "initializeParams": {
            "image": "ubuntu-os-cloud/ubuntu-1804-bionic-v20200414",
            "size" : instance_disk_size,
        }
    },
    tags=[
        "instance",
        "opendax",
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
    zone="us-central1-a",
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


master = gcp.sql.DatabaseInstance("master",
                                  database_version="MYSQL_5_7",
                                  project="chef-216716",
                                  region="us-central1",
                                  settings={
                                      "tier": "db-f1-micro",
                                  })

pulumi.export("master_private_ip_address", master.private_ip_address)
pulumi.export("master_public_ip_address", master.public_ip_address)
pulumi.export("master", master.connection_name)

