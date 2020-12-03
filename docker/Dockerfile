FROM osrf/ros:melodic-desktop-full

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

RUN apt-get update && apt-get install -y apt-utils build-essential psmisc vim-gtk

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -q -y python-catkin-tools
RUN apt-get update && apt-get install -q -y ros-melodic-hector-gazebo-plugins

# Install simulation
ENV WORKSPACE=/workspace

COPY ./gazebo $WORKSPACE

RUN source /opt/ros/melodic/setup.bash && \
    cd $WORKSPACE && \
    catkin_make && \
    catkin_make install

EXPOSE 11345

# Setup Entrypoint
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]
