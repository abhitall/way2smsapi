from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='way2smsapi',
      version='0.1',
      description='Python module for using Way2Sms free SMS services as API',
      long_description='',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
      ],
      keywords='way2smsapi way2sms smsapi',
      url='https://github.com/abhitall/way2smsapi',
      author='Abhijit Talluri',
      author_email='talluri.abhijit@gmail.com',
      license='MIT',
      packages=['way2smsapi'],
      install_requires=[
          'requests', 'bs4,'
      ],
      include_package_data=True,
      zip_safe=False)
