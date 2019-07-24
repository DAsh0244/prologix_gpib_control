import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prologix-gpib-usb-control",
    version="0.0.1",
    author="Danyal Ahsanullah",
    author_email="danyal.ahsanullah@gmail.com",
    description="interface for controlling gpib devices via the prologix gpib-usb controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/an-oreo/prologix_gpib_control",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)