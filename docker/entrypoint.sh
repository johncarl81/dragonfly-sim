#!/bin/bash
set -e

source /opt/ros/melodic/setup.bash
source /workspace/install/setup.bash

exec "$@"
