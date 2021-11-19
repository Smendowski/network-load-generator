#!/bin/sh

iperf -c 192.168.0.21 -p 7000 -i 1 -t 300 -f k | awk '{if (NR>3) {print int($6)}}'