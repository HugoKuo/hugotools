#!/bin/bash

cd /etc/swift

rm -f *.builder *.ring.gz backups/*.builder backups/*.ring.gz

swift-ring-builder object.builder create 18 3 1
swift-ring-builder object.builder add z1-192.168.1.1:6000/sdb 100
swift-ring-builder object.builder add z2-192.168.1.2:6000/sdb 100
swift-ring-builder object.builder add z3-192.168.1.3:6000/sdb 100
swift-ring-builder object.builder add z4-192.168.1.4:6000/sdb 100
swift-ring-builder object.builder add z5-192.168.1.5:6000/sdb 100
swift-ring-builder object.builder add z6-192.168.1.6:6000/sdb 50
swift-ring-builder object.builder rebalance
swift-ring-builder container.builder create 18 3 1
swift-ring-builder container.builder add z1-192.168.1.1:6001/sdb 100
swift-ring-builder container.builder add z2-192.168.1.2:6001/sdb 100
swift-ring-builder container.builder add z3-192.168.1.3:6001/sdb 100
swift-ring-builder container.builder add z4-192.168.1.4:6001/sdb 100
swift-ring-builder container.builder add z5-192.168.1.5:6001/sdb 100
swift-ring-builder container.builder add z6-192.168.1.6:6001/sdb 50
swift-ring-builder container.builder rebalance
swift-ring-builder account.builder create 18 3 1
swift-ring-builder account.builder add z1-192.168.1.1:6002/sdb 100
swift-ring-builder account.builder add z2-192.168.1.2:6002/sdb 100
swift-ring-builder account.builder add z3-192.168.1.3:6002/sdb 100
swift-ring-builder account.builder add z4-192.168.1.4:6002/sdb 100
swift-ring-builder account.builder add z5-192.168.1.5:6002/sdb 100
swift-ring-builder account.builder add z6-192.168.1.6:6002/sdb 50
swift-ring-builder account.builder rebalance
