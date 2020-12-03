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

# Install MavProxy
RUN apt-get -qq install python-dev python-opencv python-wxgtk3.0 python-pip python-matplotlib python-pygame python-lxml python-yaml

RUN pip install MAVProxy

RUN apt-get -qq install ros-melodic-mavros ros-melodic-mavros-extras

# Setup Geographic dataset
RUN mkdir -p $WORKSPACE/data && \
	cd $WORKSPACE/data && \
	wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh && \
    chmod 700 ./install_geographiclib_datasets.sh && \
    ./install_geographiclib_datasets.sh

# Install simulation
COPY ./gazebo $WORKSPACE

RUN source /opt/ros/melodic/setup.bash && \
    cd $WORKSPACE && \
    catkin_make && \
    catkin_make install

EXPOSE 11345

# Setup Entrypoint
COPY ./docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]
