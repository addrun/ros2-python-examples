'''
Author: shhr
Date: 2025-05-14 02:24:13
coding: utf-8
'''
from setuptools import find_packages, setup
from glob import glob

package_name = 'demo_python_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/data', glob('data/*.txt')),
    ],
    install_requires=['setuptools'],
    extras_require={'test': ['pytest']},
    zip_safe=True,
    maintainer='addrun',
    maintainer_email='141168900+addrun@users.noreply.github.com',
    description='Offline ROS 2 pub/sub and turtlesim control exercises.',
    license='Apache-2.0',
    
    entry_points={
        'console_scripts': [
            'novel_pub_node = demo_python_topic.novel_pub_node:main',  
            'novel_sub_node = demo_python_topic.novel_sub_node:main', 
            'turtle_circle = demo_python_topic.turtle_circle:main',
            'turtle_control = demo_python_topic.turtle_control:main',
        ],
    },
)
