from launch import LaunchDescription
from launch.actions import GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    # Spawn model
    spawn_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        respawn='false',
        output='screen',
        arguments=[
            '-file', LaunchConfiguration('fcu_url'),
            '-x', LaunchConfiguration('fcu_url'),
            '-y', LaunchConfiguration('fcu_url'),
            '-model', LaunchConfiguration('fcu_url')
        ],
    )

    # Arducopter
    arducopter_node = Node(
        package='dragonfly_sim',
        executable='arducopter.sh.py',
        respawn='false',
        output='screen',
        arguments=[
            '-file', LaunchConfiguration('fcu_url'),
            '-x', LaunchConfiguration('fcu_url'),
            '-y', LaunchConfiguration('fcu_url'),
            '-model', LaunchConfiguration('fcu_url')
        ],
    )

    # MAVROS
    apm_node = GroupAction(
        actions=[
            # push-ros-namespace to set namespace of included nodes
            PushRosNamespace(LaunchConfiguration('name')),
            Node(
                package='mavros',
                executable='mavros_node',
                namespace='mavros',
                respawn='true',
                output='screen',
                parameters=[{
                    'fcu_url': LaunchConfiguration('fcu_url'),
                    'gcs_url': '',
                    'target_system_id': LaunchConfiguration('tgt_system'),
                    'target_component_id': 1,
                    'fcu_protocol': 'v2.0',
                }]
            )
        ]
    )

    return LaunchDescription([
        spawn_node,

        apm_node,
    ])

# processes.append(subprocess.Popen(f"/entrypoint.sh ros2 run gazebo_ros spawn_entity.py -file {model_sdf.name} -x {row} -y {column} -entity dragonfly{i + 1}", shell=True))
# processes.append(subprocess.Popen(f"/entrypoint.sh ros2 run dragonfly_sim arducopter.sh {i} dragonfly{i+1}{i+1} {juav_param.name} {args.location}", shell=True))
# processes.append(subprocess.Popen(f"/entrypoint.sh ros2 launch dragonfly_sim apm.launch.py name:=dragonfly{i+1} fcu_url:=udp://127.0.0.1:{14551 + (i * 10)}@{14555 + (i * 10)} tgt_system:={i + 1}", shell=True))
