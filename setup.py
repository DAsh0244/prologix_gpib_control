import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ['pyserial']
# with open('requirements.txt','r') as req:
#      for line in req:
#          requirements.append(line)

from src.prologix_usb import __version__ as ver

setuptools.setup(
    name="prologix_usb",
    packages=['prologix_usb'],
    package_dir={'':'src'},
    version=ver,
    author="Danyal Ahsanullah",
    author_email="danyal.ahsanullah@gmail.com",
    description="interface for controlling gpib devices via the prologix gpib-usb controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/an-oreo/prologix_gpib_control",
    # packages=setuptools.find_packages(),
    requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)