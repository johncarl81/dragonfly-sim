#!/bin/bash

cd /workspace
mkdir temp0
./ardupilot/Tools/autotest/sim_vehicle.py -v ArduCopter -f gazebo-iris -I 0 --use-dir temp0