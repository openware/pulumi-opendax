# pulumi-opendax
Demo deployment system with pulumi

legion@SkyNet:~$ mkdir TEST
legion@SkyNet:~$ cd TEST
legion@SkyNet:~/TEST$ git clone https://github.com/mehanic/pulumi-opendax.git
Cloning into 'pulumi-opendax'...
remote: Enumerating objects: 66, done.
remote: Counting objects: 100% (66/66), done.
remote: Compressing objects: 100% (56/56), done.
remote: Total 66 (delta 27), reused 32 (delta 8), pack-reused 0
Unpacking objects: 100% (66/66), 29.68 KiB | 646.00 KiB/s, done.
legion@SkyNet:~/TEST$ ls
pulumi-opendax
legion@SkyNet:~/TEST$ cd pulumi-opendax/
legion@SkyNet:~/TEST/pulumi-opendax$ ls
first.txt               __main__.py  playbook         Pulumi.yaml       script.sh   ssh-configure.txt
install_from_github.sh  network.py   Pulumi.dev.yaml  requirements.txt  second.txt
legion@SkyNet:~/TEST/pulumi-opendax$ pulumi up
                       
                       /// --   I try to provision , but have failed becouse need install python modules
legion@SkyNet:~/TEST/pulumi-opendax$ pulumi up   
Please choose a stack, or create a new one:  [Use arrows to move, enter to select, type to filter]
> dev
  <create a new stack>
Please choose a stack, or create a new one: dev
Previewing update (dev):
     Type                 Name                    Plan     Info
     pulumi:pulumi:Stack  gcp-debian-opendax-dev           1 error
 
Diagnostics:
  pulumi:pulumi:Stack (gcp-debian-opendax-dev):
    error: The 'virtualenv' option in Pulumi.yaml is set to "venv", but "/home/legion/TEST/pulumi-opendax/venv" doesn't exist; run the following commands to create the virtual environment and install dependencies into it:
    
        1. python3 -m venv /home/legion/TEST/pulumi-opendax/venv
        2. /home/legion/TEST/pulumi-opendax/venv/bin/python -m pip install --upgrade pip setuptools wheel
        3. /home/legion/TEST/pulumi-opendax/venv/bin/python -m pip install -r requirements.txt
    
    
    For more information see: https://www.pulumi.com/docs/intro/languages/python/#virtual-environments
 
              /// -- At this moment I can configure provisions
legion@SkyNet:~/TEST/pulumi-opendax$ python3 -m venv /home/legion/TEST/pulumi-opendax/venv
legion@SkyNet:~/TEST/pulumi-opendax$ /home/legion/TEST/pulumi-opendax/venv/bin/python -m pip install --upgrade pip setuptools wheel
Collecting pip
  Using cached pip-20.2.2-py2.py3-none-any.whl (1.5 MB)
Collecting setuptools
  Using cached setuptools-49.6.0-py3-none-any.whl (803 kB)
Collecting wheel
  Using cached wheel-0.35.1-py2.py3-none-any.whl (33 kB)
Installing collected packages: pip, setuptools, wheel
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Uninstalling pip-20.0.2:
      Successfully uninstalled pip-20.0.2
  Attempting uninstall: setuptools
    Found existing installation: setuptools 46.1.3
    Uninstalling setuptools-46.1.3:
      Successfully uninstalled setuptools-46.1.3
Successfully installed pip-20.2.2 setuptools-49.6.0 wheel-0.35.1
legion@SkyNet:~/TEST/pulumi-opendax$ /home/legion/TEST/pulumi-opendax/venv/bin/python -m pip install -r requirements.txt
Collecting pulumi<3.0.0,>=2.0.0
  Using cached pulumi-2.9.0-py2.py3-none-any.whl (107 kB)
Collecting pulumi-gcp<4.0.0,>=3.0.0
  Downloading pulumi_gcp-3.21.1.tar.gz (1.0 MB)
     |████████████████████████████████| 1.0 MB 559 kB/s 
Collecting protobuf>=3.6.0
  Using cached protobuf-3.13.0-cp38-cp38-manylinux1_x86_64.whl (1.3 MB)
Collecting grpcio!=1.30.0,>=1.9.1
  Using cached grpcio-1.31.0-cp38-cp38-manylinux2014_x86_64.whl (3.4 MB)
Processing /home/legion/.cache/pip/wheels/93/7f/7d/78ec535a4340ef2696aad8b17fe8bb063d56301bd62881b069/dill-0.3.2-py3-none-any.whl
Collecting parver>=0.2.1
  Using cached parver-0.3.0-py2.py3-none-any.whl (15 kB)
Collecting semver>=2.8.1
  Using cached semver-2.10.2-py2.py3-none-any.whl (12 kB)
Requirement already satisfied: setuptools in ./venv/lib/python3.8/site-packages (from protobuf>=3.6.0->pulumi<3.0.0,>=2.0.0->-r requirements.txt (line 1)) (49.6.0)
Collecting six>=1.9
  Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting attrs>=17.4.0
  Using cached attrs-20.1.0-py2.py3-none-any.whl (49 kB)
Collecting arpeggio~=1.7
  Using cached Arpeggio-1.9.2-py2.py3-none-any.whl (57 kB)
Building wheels for collected packages: pulumi-gcp
  Building wheel for pulumi-gcp (setup.py) ... done
  Created wheel for pulumi-gcp: filename=pulumi_gcp-3.21.1-py3-none-any.whl size=1733637 sha256=38512ccce6cd9c7074bd54c943cf8a8c6f9c5bec77ced7bf28de3ebad1e88a41
  Stored in directory: /home/legion/.cache/pip/wheels/f8/29/7b/a516881b72429ed1faf2a7b409ddb120b10de656f47e0b0f39
Successfully built pulumi-gcp
Installing collected packages: six, protobuf, grpcio, dill, pulumi, attrs, arpeggio, parver, semver, pulumi-gcp
Successfully installed arpeggio-1.9.2 attrs-20.1.0 dill-0.3.2 grpcio-1.31.0 parver-0.3.0 protobuf-3.13.0 pulumi-2.9.0 pulumi-gcp-3.21.1 semver-2.10.2 six-1.15.0

                    /// -- I execute provision to GCP by default (it is Pulumi.dev.yaml)
legion@SkyNet:~/TEST/pulumi-opendax$ pulumi up
Previewing update (dev):
     Type                     Name                    Plan       
 +   pulumi:pulumi:Stack      gcp-debian-opendax-dev  create     
 +   ├─ gcp:compute:Address   address                 create     
 +   ├─ gcp:compute:Network   network                 create     
 +   ├─ gcp:compute:Firewall  firewall                create     
 +   └─ gcp:compute:Instance  instance                create     
 
Resources:
    + 5 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details

               /// -- we can change default parameters by adding 
pulumi config set instance_name opendax
pulumi config set instance_disk_size 300
pulumi config set instance_type n1-standard-2
pulumi config set gcp-debian-opendax:zone_name us-central1-a

             /// -- made provision to GCP
             
Updating (dev):
     Type                     Name                    Status      
 +   pulumi:pulumi:Stack      gcp-debian-opendax-dev  created     
 +   ├─ gcp:compute:Address   address                 created     
 +   ├─ gcp:compute:Network   network                 created     
 +   ├─ gcp:compute:Firewall  firewall                created     
 +   └─ gcp:compute:Instance  instance                created     
 
Outputs:
    compute_firewall    : "projects/chef-216716/global/firewalls/firewall-17c0cad"
    cpu_platform        : "Intel Haswell"                                                                                              
    instanceInstanceId  : "7080754009159871488"                                                                                        
    instanceName        : "opendax"                                                                                                    
    instanceStatus      : "RUNNING"                                                                                                    
    instance_external_ip: "35.226.214.8"                                                                                               
  
  
  
              
              
              
              
              
              
              
              
              
              
              
