#!/bin/bash
cd /etc/swift
rm -f *.ring.gz
scp 10.0.0.1:/etc/swift/*.gz ./
chown -R swift:swift /etc/swift/*
