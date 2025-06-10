from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in campaign_tracking/__init__.py
from campaign_tracking import __version__ as version

setup(
    name="campaign_tracking",
    version=version,
    description="Campaign and UTM Link Tracking for Frappe",
    author="Chinmay Bhatk",
    author_email="chinmay@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)