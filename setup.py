from setuptools import setup, find_packages

setup(
    name = "reporting",
    version = '0.1',
    packages = find_packages(),
    install_requires = [
        "pandas"
    ],
    description = "test package for integrating with google colab",
    author = "Elaine French",
    author_email = "elainekfrench@gmail.com",
    url = "https://github.com/ekfrench17/test_colab"
)