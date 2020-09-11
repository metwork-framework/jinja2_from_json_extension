from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n')
        if (line and not line.startswith('--')) and (";" not in line)]

setup(
    name="jinja2_from_json_extension",
    version="0.0.1",
    license="BSD",
    url="https://github.com/metwork-framework/jinja2_from_json_extension",
    packages=find_packages(),
    install_requires=install_requires
)
