# pulumi-opendax
Demo deployment system with pulumi

## System overview

Pulumi must create :
 * a dedicated Network
 * a dedicated Firewall
 * a Virtual machine 8GB - 4 cores
 * a Cloud SQL (MySQ)
 
### Level 1:

Then install ruby, docker, docker-compose, OpenDAX
Start up the containers

### Level 2:

Do not use the docker MySQL but use the deployed Cloud SQL.
