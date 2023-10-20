from setuptools import setup, find_namespace_packages

setup(
    name='hello_world_stv',
    version='0.0.1',
    description='Very useful code',
    author='Taras Sabat',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_stv.main:greeting']}
)
