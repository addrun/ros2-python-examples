'''
Author: shhr
Date: 2025-05-13 20:10:34
coding: utf-8
'''
from setuptools import find_packages, setup

package_name = 'demo_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    extras_require={'test': ['pytest']},
    zip_safe=True,
    maintainer='addrun',
    maintainer_email='141168900+addrun@users.noreply.github.com',
    description='Introductory ROS 2 Python nodes and offline threading examples.',
    license='Apache-2.0',
    
    entry_points={
        'console_scripts': [
        'python_node = demo_python_pkg.python_node:main',
        'learn_thread = demo_python_pkg.learn_thread:main',
        ],
    },
)
