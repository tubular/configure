from setuptools import setup

version = "0.6.0-dev0"

with open('README') as f:
    long_description = f.read()

setup(
    name="configure",
    version=version,
    description="configuration toolkit based on YAML",
    long_description=long_description,
    author="Andrey Popp",
    author_email="8mayday@gmail.com",
    url='https://github.com/andreypopp/configure',
    py_modules=["configure"],
    test_suite="tests",
    install_requires=["pyyaml"],
    zip_safe=False)
