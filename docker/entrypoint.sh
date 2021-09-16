#!/bin/bash
set -e

source /usr/share/gazebo-11/setup.sh
source /opt/ros/foxy/setup.bash
source /workspace/gazebo/install/setup.bash

export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:"/workspace/gazebo/src/dragonfly_sim/models"
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:"/workspace/ardupilot_gazebo/build"
export GAZEBO_MODEL_PATH=/workspace/ardupilot_gazebo/models:${GAZEBO_MODEL_PATH}
export GAZEBO_MODEL_PATH=/workspace/ardupilot_gazebo/models_gazebo:${GAZEBO_MODEL_PATH}
export GAZEBO_RESOURCE_PATH=/workspace/ardupilot_gazebo/worlds:${GAZEBO_RESOURCE_PATH}
export GAZEBO_PLUGIN_PATH=/workspace/ardupilot_gazebo/build:${GAZEBO_PLUGIN_PATH}

exec "$@"
