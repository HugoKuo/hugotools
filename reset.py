#!/usr/bin/python
"""
Author : Hugo Kuo
Usage: 
Date: 2012-01-13
"""
import sys
import commands
from subprocess import *
from swift.common.manager import Server, Manager, UnknownCommandError
from parse_uuid import *



#parse Storage device UUID
devsorts = parse_uuid()

#stop all swift servers
servers=['all']
manager = Manager(servers)
status = manager.run_command('stop')

#umount 
umountstat = commands.getstatusoutput('umount /srv/node/*')
if umountstat[0] == 0 :
    print "=====Umount all storage successful====="
else:
    print umountstat[1]

#Make filesystem & set UUID
for disks in devsorts.keys():
    print "Make XFS on :" , disks
    commands.getstatusoutput('mkfs.xfs -f -i size=1024 /dev/%s' % disks)
    #set UUID to disk
    print ("Set UUID: %s  for " % devsorts[disks]) , disks 
    commands.getstatusoutput('xfs_admin -U %s %s' % (devsorts[disks],disks))  
commands.getstatusoutput('mount -a')
print "======Success to mount disks=======" 

commands.getstatusoutput('chown -R swift:swift /srv/*')
servers=['main']
manager = Manager(servers)
status = manager.run_command('start') 
