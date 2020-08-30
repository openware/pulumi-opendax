from pulumi_gcp import compute, servicenetworking
from pulumi_gcp.config import project

compute_network = compute.Network(
    "network",
    auto_create_subnetworks=True,
    project=project
)


compute_firewall = compute.Firewall(
    "firewall",
    network=compute_network.self_link,
    allows=[{
        "protocol": "tcp",
        "ports": ["22", "80", "443"],
    }]
)