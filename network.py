from pulumi_gcp import compute

compute_network = compute.Network(
    "network",
    auto_create_subnetworks=True,
    project="chef-216716"
)


compute_firewall = compute.Firewall(
    "firewall",
    network=compute_network.self_link,
    allows=[{
        "protocol": "tcp",
        "ports": ["22", "80", "443"],
    }]
)

