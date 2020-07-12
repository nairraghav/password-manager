from ron_password_manager import VERSION
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ron-password-manager",
    version=VERSION,
    author="Raghav Nair",
    author_email="nairraghav@hotmail.com",
    description="A password manager package meant for CLI use to generate and store passwords on your local machine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nairraghav/ron-password-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['ron_password_manager=ron_password_manager:main'],
    }
)
