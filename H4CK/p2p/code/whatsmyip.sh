#!/bin/bash
ifconfig | grep 'netmask 255.255.255.0' | cut -b 14-28
#EOF
