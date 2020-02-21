from setuptools import setup

setup(
   name='get-bittrex-tick',
   version='1.0',
   description='A useful module',
   author='Shadowist',
   author_email='shadowist@protonmail.com',
   packages=['.'],  #same as name
   install_requires=["requests"], #external packages as dependencies
)