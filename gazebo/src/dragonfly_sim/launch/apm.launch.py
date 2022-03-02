import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    # pkg_mavros_ros = get_package_share_directory('mavros')
    #
    # apm_config = {}
    # plugins = {}
    #
    # with open(os.path.join(pkg_mavros_ros, 'launch', 'apm_pluginlists.yaml')) as file:
    #     plugins = yaml.load(file)
    #
    # with open(os.path.join(pkg_mavros_ros, 'launch', 'apm_config.yaml')) as file:
    #     apm_config = yaml.load(file)

    parameters = {
        'fcu_url': LaunchConfiguration('fcu_url'),
        'gcs_url': '',
        'target_system_id': LaunchConfiguration('tgt_system'),
        'target_component_id': 1,
        'fcu_protocol': 'v2.0',
        'plugin_blacklist': ['actuator_control', 'ftp', 'safety_area', 'hil', 'altitude', 'debug_value', 'image_pub',
                             'px4flow', 'vibration', 'vision_speed_estimate', 'wheel_odometry'],
        'startup_px4_usb_quirk': False,
        'conn': {'heartbeat_rate': 1.0, 'heartbeat_mav_type': 'ONBOARD_CONTROLLER', 'timeout': 10.0,
                 'timesync_rate': 10.0, 'system_time_rate': 1.0},
        'sys': {'min_voltage': 10.0, 'disable_diag': False},
        'time': {'time_ref_source': 'fcu', 'timesync_mode': 'MAVLINK', 'timesync_avg_alpha': 0.6},
        'tdr_radio': {'low_rssi': 40},
        'cmd': {'use_comp_id_system_control': False},
        'global_position': {'frame_id': 'map', 'child_frame_id': 'base_link', 'rot_covariance': 99999.0,
                            'gps_uere': 1.0, 'use_relative_alt': True,
                            'tf': {'send': False, 'frame_id': 'map', 'global_frame_id': 'earth',
                                   'child_frame_id': 'base_link'}},
        'imu': {'frame_id': 'base_link', 'linear_acceleration_stdev': 0.0003,
                'angular_velocity_stdev': '0.0003490659 // 0.02 degrees', 'orientation_stdev': 1.0,
                'magnetic_stdev': 0.0}, 'local_position': {'frame_id': 'map', 'tf': {'send': False, 'frame_id': 'map',
                                                                                     'child_frame_id': 'base_link',
                                                                                     'send_fcu': False}},
        'safety_area': {'p1': {'x': 1.0, 'y': 1.0, 'z': 1.0}, 'p2': {'x': -1.0, 'y': -1.0, 'z': -1.0}},
        'setpoint_accel': {'send_force': False}, 'setpoint_attitude': {'reverse_thrust': False, 'use_quaternion': False,
                                                                       'tf': {'listen': False, 'frame_id': 'map',
                                                                              'child_frame_id': 'target_attitude',
                                                                              'rate_limit': 50.0}},
        'setpoint_raw': {'thrust_scaling': 1.0}, 'setpoint_position': {
            'tf': {'listen': False, 'frame_id': 'map', 'child_frame_id': 'target_position', 'rate_limit': 50.0},
            'mav_frame': 'LOCAL_NED'}, 'setpoint_velocity': {'mav_frame': 'LOCAL_NED'},
        'mission': {'pull_after_gcs': True, 'use_mission_item_int': True}, 'distance_sensor': {
            'rangefinder_pub': {'id': 0, 'frame_id': 'lidar', 'field_of_view': 0.0, 'send_tf': False,
                                'sensor_position': {'x': 0.0, 'y': 0.0, 'z': -0.1}},
            'rangefinder_sub': {'subscriber': True, 'id': 1, 'orientation': 'PITCH_270'}},
        'image': {'frame_id': 'px4flow'},
        'fake_gps': {'use_mocap': True, 'mocap_transform': False, 'mocap_withcovariance': False, 'use_vision': False,
                     'use_hil_gps': True, 'gps_id': 4, 'geo_origin': {'lat': 47.3667, 'lon': 8.55, 'alt': 408.0},
                     'eph': 2.0, 'epv': 2.0, 'horiz_accuracy': 0.5, 'vert_accuracy': 0.5, 'speed_accuracy': 0.0,
                     'satellites_visible': 6, 'fix_type': 3,
                     'tf': {'listen': False, 'send': False, 'frame_id': 'map', 'child_frame_id': 'fix',
                            'rate_limit': 10.0}, 'gps_rate': 5.0},
        'landing_target': {'listen_lt': False, 'mav_frame': 'LOCAL_NED', 'land_target_type': 'VISION_FIDUCIAL',
                           'image': {'width': 640, 'height': 480},
                           'camera': {'fov_x': 2.0071286398, 'fov_y': 2.0071286398},
                           'tf': {'send': True, 'listen': False, 'frame_id': 'landing_target',
                                  'child_frame_id': 'camera_center', 'rate_limit': 10.0},
                           'target_size': {'x': 0.3, 'y': 0.3}}, 'mocap': {'use_tf': False, 'use_pose': True},
        'odometry': {'frame_tf': {'desired_frame': 'ned'}, 'estimator_type': 3},
        'px4flow': {'frame_id': 'px4flow', 'ranger_fov': 0.118682, 'ranger_min_range': 0.3, 'ranger_max_range': 5.0},
        'vision_pose': {
            'tf': {'listen': False, 'frame_id': 'map', 'child_frame_id': 'vision_estimate', 'rate_limit': 10.0}},
        'vision_speed': {'listen_twist': True, 'twist_cov': True}, 'vibration': {'frame_id': 'base_link'},
        'wheel_odometry': {'count': 2, 'use_rpm': False, 'wheel0': {'x': 0.0, 'y': -0.15, 'radius': 0.05},
                           'wheel1': {'x': 0.0, 'y': 0.15, 'radius': 0.05}, 'send_raw': True, 'send_twist': False,
                           'frame_id': 'map', 'child_frame_id': 'base_link', 'vel_error': 0.1,
                           'tf': {'send': True, 'frame_id': 'map', 'child_frame_id': 'base_link'}}
    }

    # apm_node = GroupAction(
    #     actions=[
    #         # push-ros-namespace to set namespace of included nodes
    #         PushRosNamespace(LaunchConfiguration('name')),
    #         Node(
    #             package='mavros',
    #             executable='mavros_node',
    #             namespace='mavros',
    #             respawn='true',
    #             output='screen',
    #             parameters=[parameters],
    #         )
    #     ]
    # )
    apm_node = Node(
        package='mavros',
        executable='mavros_node',
        namespace='dragonfly1/mavros',
        respawn='true',
        output='screen',
        parameters=[parameters],
    )

    return LaunchDescription([
        apm_node,
    ])
