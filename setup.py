from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='bond-home',
      version='0.0.4',
      description='Python library for controlling BOND Home Hub',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/nguyer/bond-home',
      author='Nicko Guyer',
      author_email='nguyer@gmail.com',
      license='MIT',
      packages=['bond'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
