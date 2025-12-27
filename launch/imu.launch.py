import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('tm_imu'),
        'config',
        'params.yaml'
    )

    publish_gravity_frame_arg = DeclareLaunchArgument(
        'publish_gravity_frame',
        default_value='true',
        description='Publish gravity frame'
    )

    acceleration_scale_arg = DeclareLaunchArgument(
        'acceleration_scale',
        default_value='9.794',
        description='Scale factor to convert acceleration from g to m/s^2'
    )

    imu_node = Node(
        package="tm_imu",
        executable="tm_imu_node",
        name="tm_imu_node",
        output="screen",
        parameters=[
            config,
            {'publish_gravity_frame': LaunchConfiguration('publish_gravity_frame')},
            {'acceleration_scale': LaunchConfiguration('acceleration_scale')}
        ],
    )

    return LaunchDescription([
        publish_gravity_frame_arg,
        acceleration_scale_arg,
        imu_node
    ])