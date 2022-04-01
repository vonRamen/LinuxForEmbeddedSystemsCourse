#!/bin/bash
#find network interface
#INET= $(ip route | grep default | sed -e "s/^.*dev.//" -e "s/.proto.*//")
#echo $(ip route | grep default | sed -e "s/^.*dev.//" -e "s/.proto.*//")
# setup network routing
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o $(ip route | grep default | sed -e "s/^.*dev.//" -e "s/.proto.*//") -j MASQUERADE