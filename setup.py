from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='py_selen',
    version='0.0.1',
    license='MIT License',
    author='Yuri Gomes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='yurialdegomes@gmail.com',
    keywords='selenium',
    description=u'Biblioteca de macros para selenium',
    packages=['py_selen'],
    install_requires=['requests'],)