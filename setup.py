from setuptools import setup

broker_name = 'GovAuction'
pkg_name = 'robot_tests.broker.{}'.format(broker_name)

setup(name=pkg_name,
      version='0.0.dev1',
      description='{} broker for Prozorro Robot tests'.format(broker_name),
      author='',
      author_email='',
      url='https://github.com/ProzorroUKR/{}'.format(pkg_name),
      )
