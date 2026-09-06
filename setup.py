from setuptools import setup

setup(
    name='travelling-salesman-problem-solver',
    version='1.0',
    packages=['app'],
    install_requires=['networkx', 'numpy'],
    entry_points={'console_scripts': ['app = app:main']}
)