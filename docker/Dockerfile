FROM osrf/ros:melodic-desktop-full

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

ENV DEBIAN_FRONTEND noninteractive
ENV WORKSPACE=/workspace

RUN apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -qq install apt-utils build-essential vim python-catkin-tools

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install Dependencies
RUN apt-get -qq install python-dev python-opencv python-wxgtk3.0 \
    python-pip python-matplotlib python-pygame python-lxml python-yaml \
    ros-melodic-mavros ros-melodic-mavros-extras libgazebo9-dev

# Install MavProxy
RUN pip install MAVProxy

# Clear apt cache to save on space
RUN rm -rf /var/lib/apt/lists/*

# Setup Geographic dataset
RUN mkdir -p $WORKSPACE/data && \
    cd $WORKSPACE/data && \
    wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh && \
    chmod 700 ./install_geographiclib_datasets.sh && \
    ./install_geographiclib_datasets.sh

# Install simulation
RUN cd $WORKSPACE && \
    git clone --recurse-submodules -j8 https://github.com/ArduPilot/ardupilot.git

RUN cd $WORKSPACE && \
    git clone --recurse-submodules -j8 https://github.com/SwiftGust/ardupilot_gazebo.git

RUN cd $WORKSPACE/ardupilot && \
    ./waf configure && ./waf copter

RUN cd $WORKSPACE/ardupilot_gazebo && \
    mkdir build && cd build && cmake .. && make -j4 && make install

RUN mkdir $WORKSPACE/gazebo

COPY ./gazebo $WORKSPACE/gazebo

RUN source /opt/ros/melodic/setup.bash && \
    cd $WORKSPACE/gazebo && \
    catkin_make && \
    catkin_make install

COPY ./templates $WORKSPACE/templates

# Setup Entrypoint
COPY ./docker/entrypoint.sh /
COPY ./docker/entrypoint.py /

ENTRYPOINT ["/entrypoint.py"]