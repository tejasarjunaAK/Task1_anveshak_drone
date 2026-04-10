from setuptools import find_packages, setup

package_name = 'publisher_subscription'

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
    zip_safe=True,
    maintainer='tejasarjuna',
    maintainer_email='tejasarjuna009@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['alt_pub= publisher_subscription.alt_pub:main',
'altitude_monitor= publisher_subscription.altitude_monitor:main'
        ],
    },
)
