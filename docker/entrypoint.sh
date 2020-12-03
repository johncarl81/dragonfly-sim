#!/bin/bash
set -e

source /opt/ros/melodic/setup.bash
source /workspace/install/setup.bash

export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:"/workspace/src/dragonfly_sim/models"
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:"/workspace/ardupilot_gazebo/build"

exec "$@"
