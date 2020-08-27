# pulumi-opendax
## Demo deployment system with pulumi

```bash
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
```

  #####  I try to provision , but I can not and then  failed because we must configure  python modules (it is depends from clouds)
```bash
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
```

 ##### At this moment I can configure provisions using commands:
```bash
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
```

 ##### I execute provision to GCP by default (it is Pulumi.dev.yaml), in shortly for better we can used pulumi up -y
```bash
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
```

 ##### we can change default parameters by adding 
 ```bash
pulumi config set instance_name opendax
pulumi config set instance_disk_size 300
pulumi config set instance_type n1-standard-2
pulumi config set gcp-debian-opendax:zone_name us-central1-a
```

##### made provision to GCP
```bash             
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
```  
  
  
##### go to gcp Compute Engine and find our instance and in point ssh take commands

```bash
gcloud beta compute ssh --zone "us-central1-a" "opendax" --project "chef-216716"
```

```bash
legion@SkyNet:~$ gcloud beta compute ssh --zone "us-central1-a" "opendax" --project "chef-216716"
Warning: Permanently added 'compute.7080754009159871488' (ECDSA) to the list of known hosts.
Linux opendax 4.19.0-10-cloud-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
legion@opendax:~$ sudo su
root@opendax:/home/legion# passwd 
New password: 
Retype new password: 
passwd: password updated successfully
root@opendax:/home/legion# exit
exit
legion@opendax:~$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-08-27 20:11:07 UTC; 14min ago
     Docs: https://docs.docker.com
 Main PID: 8016 (dockerd)
    Tasks: 10
   Memory: 42.2M
   CGroup: /system.slice/docker.service
           └─8016 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Aug 27 20:11:06 opendax dockerd[8016]: time="2020-08-27T20:11:06.779220562Z" level=warning msg="Your kernel does not support cgroup rt 
Aug 27 20:11:06 opendax dockerd[8016]: time="2020-08-27T20:11:06.779229851Z" level=warning msg="Your kernel does not support cgroup blk
Aug 27 20:11:06 opendax dockerd[8016]: time="2020-08-27T20:11:06.779238196Z" level=warning msg="Your kernel does not support cgroup blk
Aug 27 20:11:06 opendax dockerd[8016]: time="2020-08-27T20:11:06.779461821Z" level=info msg="Loading containers: start."
Aug 27 20:11:07 opendax dockerd[8016]: time="2020-08-27T20:11:07.234341367Z" level=info msg="Default bridge (docker0) is assigned with 
Aug 27 20:11:07 opendax dockerd[8016]: time="2020-08-27T20:11:07.363038092Z" level=info msg="Loading containers: done."
Aug 27 20:11:07 opendax dockerd[8016]: time="2020-08-27T20:11:07.425608856Z" level=info msg="Docker daemon" commit=48a66213fe graphdriv
Aug 27 20:11:07 opendax dockerd[8016]: time="2020-08-27T20:11:07.425767947Z" level=info msg="Daemon has completed initialization"
Aug 27 20:11:07 opendax systemd[1]: Started Docker Application Container Engine.
Aug 27 20:11:07 opendax dockerd[8016]: time="2020-08-27T20:11:07.524012585Z" level=info msg="API listen on /var/run/docker.sock"

legion@opendax:~$ sudo systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2020-08-27 20:10:35 UTC; 15min ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 6297 (sshd)
    Tasks: 1 (limit: 4915)
   Memory: 2.8M
   CGroup: /system.slice/ssh.service
           └─6297 /usr/sbin/sshd -D

Aug 27 20:10:35 opendax systemd[1]: Starting OpenBSD Secure Shell server...
Aug 27 20:10:35 opendax sshd[6297]: Server listening on 0.0.0.0 port 22.
Aug 27 20:10:35 opendax sshd[6297]: Server listening on :: port 22.
Aug 27 20:10:35 opendax systemd[1]: Started OpenBSD Secure Shell server.
Aug 27 20:23:51 opendax sshd[15633]: Accepted publickey for legion from 46.211.25.147 port 62278 ssh2: RSA SHA256:EV2OwMX9kfSFSZZhniCof
Aug 27 20:23:51 opendax sshd[15633]: pam_unix(sshd:session): session opened for user legion by (uid=0)
lines 1-17/17 (END)
legion@opendax:~$ docker-compose -v
docker-compose version 1.26.2, build eefe0d31
legion@opendax:~$ rvm -v
rvm 1.29.10 (latest) by Michal Papis, Piotr Kuczynski, Wayne E. Seguin [https://rvm.io]
legion@opendax:~$ 
```
              
##### and we can also use other terminal for logging by ssh not using native tools of GCP  that give us possibility use Ansible or Salt Stack 

```bash
legion@SkyNet:~$ ssh root@35.226.214.8
The authenticity of host '35.226.214.8 (35.226.214.8)' can't be established.
ECDSA key fingerprint is SHA256:KBZWeTAj46GH59beEWYgK3mRb/cuGabV5K43KjC67Mk.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '35.226.214.8' (ECDSA) to the list of known hosts.
root@35.226.214.8's password: 
Linux opendax 4.19.0-10-cloud-amd64 #1 SMP Debian 4.19.132-1 (2020-07-24) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@opendax:~# su - app
app@opendax:~$ 
```

##### we have made provision pulumi infostructure and prepared for use ansible playbook  sshd_config , than

```bash
legion@SkyNet:~/TEST/pulumi-opendax$ cd playbook/
legion@SkyNet:~/TEST/pulumi-opendax/playbook$ ls
ansible.cfg  dev  facts_ansible.yaml  install_second-txt_script.yaml
legion@SkyNet:~/TEST/pulumi-opendax/playbook$ ansible-playbook -i dev facts_ansible.yaml

PLAY [show facts] *********************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
[WARNING]: Platform linux on host 35.226.214.8 is using the discovered Python interpreter at /usr/bin/python3.7, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.9/reference_appendices/interpreter_discovery.html for more information.
ok: [35.226.214.8]

TASK [Show IP Address] ****************************************************************************************************************
ok: [35.226.214.8] => {
    "msg": "10.128.0.2"
}

TASK [Show IP6 Address] ***************************************************************************************************************
ok: [35.226.214.8] => {
    "msg": [
        "fe80::4001:aff:fe80:2"
    ]
}

TASK [Show Linux distribution] ********************************************************************************************************
ok: [35.226.214.8] => {
    "msg": "Debian"
}

TASK [Show Linux distribution] ********************************************************************************************************
ok: [35.226.214.8] => {
    "msg": "10"
}

TASK [Show Linux distribution] ********************************************************************************************************
ok: [35.226.214.8] => {
    "msg": "opendax"
}

TASK [Show name of user] ******************************************************************************************************************
[WARNING]: Module remote_tmp /home/legion/.ansible/tmp did not exist and was created with a mode of 0700, this may cause issues when
running as another user. To avoid this, create the remote_tmp dir with the correct permissions manually
changed: [35.226.214.8]

TASK [my secret identity] *************************************************************************************************************
ok: [35.226.214.8] => {
    "msg": "legion"
}

TASK [copy file first.txt to remote host] *********************************************************************************************
changed: [35.226.214.8]

TASK [copy file script.sh to remote host] *********************************************************************************************
changed: [35.226.214.8]

TASK [copy file second.txt to remote host] ********************************************************************************************
changed: [35.226.214.8]

PLAY RECAP ****************************************************************************************************************************
35.226.214.8               : ok=11   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

legion@SkyNet:~/TEST/pulumi-opendax/playbook$ 
```

##### than I used ssh with command root@IP and  I can see

```bash
legion@opendax:~$ ls
first.txt  script.sh  second.txt
legion@opendax:~$ 
```



##### At this moment we are going to installing all nessacery tools and requeraments for running docker containers

```bash
legion@opendax:~$ bash script.sh 
Searching for binary rubies, this might take some time.
Found remote file https://rvm_io.global.ssl.fastly.net/binaries/debian/10/x86_64/ruby-2.6.5.tar.bz2
Checking requirements for debian.
Installing requirements for debian.
Updating system....
Installing required packages: gawk, autoconf, automake, bison, libffi-dev, libgdbm-dev, libncurses5-dev, libsqlite3-dev, libtool, libyaml-dev, pkg-config, sqlite3, zlib1g-dev, libgmp-dev, libreadline-dev, libssl-dev.................                                      
Requirements installation successful.
ruby-2.6.5 - #configure
ruby-2.6.5 - #download
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 19.8M  100 19.8M    0     0  41.8M      0 --:--:-- --:--:-- --:--:-- 41.7M

              
  *and in the end of running this script we shall see*
  
  *** LOCAL GEMS ***

bigdecimal (default: 1.4.1)
bundler-unload (1.0.2)
cmath (default: 1.0.0)
date (default: 2.0.0)
did_you_mean (1.3.0)
e2mmap (default: 0.1.0)
executable-hooks (1.6.0)
forwardable (default: 1.2.0)
gem-wrappers (1.4.0)
ipaddr (default: 1.2.2)
matrix (default: 0.1.0)
power_assert (1.1.3)
rake (12.3.2)
rubygems-update (3.1.4)
scanf (default: 1.0.0)
strscan (default: 1.0.0)
thwait (default: 0.1.0)
tracer (default: 0.1.0)
Cloning into 'opendax'...
remote: Enumerating objects: 77, done.
remote: Counting objects: 100% (77/77), done.
remote: Compressing objects: 100% (56/56), done.
remote: Total 2975 (delta 35), reused 45 (delta 21), pack-reused 2898
Receiving objects: 100% (2975/2975), 464.62 KiB | 6.11 MiB/s, done.
Resolving deltas: 100% (1749/1749), done.
legion@opendax:~$ ls
first.txt  opendax  script.sh  second.txt
legion@opendax:~$ 
```
          
              
              
