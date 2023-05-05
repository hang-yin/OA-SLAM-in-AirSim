from setuptools import setup

package_name = 'visualizer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'config/visualize.rviz', 'launch/visualize.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yh6917',
    maintainer_email='yinhang0226@gmail.com',
    description='Visualization package for visual odometry',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
