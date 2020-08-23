#!/usr/bin/env bash

git clone https://github.com/openware/opendax.git
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
source /home/legion/.rvm/scripts/rvm
rvm install "ruby-2.6.5"
rvm reinstall ruby-2.6.5
cd opendax
#You must use Bundler 2 or greater with this lockfile.
gem update --system
gem install bundler
bundler update --bundler
bundle install
rake -T
sudo groupadd docker
sudo usermod -aG docker $USER
#Log out and log back in so that your group membership is re-evaluated.
docker info
sudo nano /etc/hosts
#we login again in terminal
cd opendax
rake service:all
