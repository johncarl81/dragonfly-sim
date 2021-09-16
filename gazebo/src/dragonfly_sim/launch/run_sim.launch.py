import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_mavros_ros = get_package_share_directory('mavros')

    print("GAZEBO: {}".format(pkg_gazebo_ros))

    model_file = 'model.sdf'
    spawn_offset_x = '0'
    spawn_offset_y = '0'
    model_name = 'dragonfly1'

    # <node name="juav_spawner$(arg instance)" pkg="gazebo_ros" type="spawn_model"
    # args="-sdf -file $(arg model_file) -x $(arg spawn_offset_x) -y $(arg spawn_offset_y) -model $(arg name)"
    # respawn="false" output="screen" />
    #
    # <node name="juav_arducopter$(arg instance)" pkg="dragonfly_sim" type="arducopter.sh" args="$(arg instance) $(arg name)$(arg tgt_system) $(arg param_file) $(arg location)"/>
    #
    # <include file="$(find dragonfly_sim)/launch/apm.launch">
    # <arg name="name" value="$(arg name)" />
    # <arg name="tgt_system" value="$(arg tgt_system)"/>
    # <arg name="fcu_url" value="$(arg fcu_url)"/>
    # </include>

    spawn_model = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        respawn='false',
        output='screen',
        arguments=[
            '-sdf',
            '-file', model_file,
            '-x', spawn_offset_x,
            '-y', spawn_offset_y,
            '-model', model_name
        ],
    )

    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': os.path.join('worlds', 'empty_sky.world')}.items()
    )

    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    # gzserver = ExecuteProcess(
    #     cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so' 'worlds/empty_sky.world'],
    #     output='screen'
    # )
    return LaunchDescription([
        gzserver,
        gzclient,
    ])
    # return LaunchDescription([
    #     Node(
    #         package='turtlesim',
    #         namespace='turtlesim1',
    #         executable='turtlesim_node',
    #         name='sim'
    #     ),
    #     Node(
    #         package='turtlesim',
    #         namespace='turtlesim2',
    #         executable='turtlesim_node',
    #         name='sim'
    #     ),
    #     Node(
    #         package='turtlesim',
    #         executable='mimic',
    #         name='mimic',
    #         remappings=[
    #             ('/input/pose', '/turtlesim1/turtle1/pose'),
    #             ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
    #         ]
    #     )
    # ])
