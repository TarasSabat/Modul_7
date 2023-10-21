from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_STV',
    version='0.0.1',
    description='Very useful code',
    author='Taras Sabat',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder_STV.clean:start']}
)
