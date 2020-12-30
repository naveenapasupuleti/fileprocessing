import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mouritech-file_processing_package", # Replace with your own username
    version="0.0.2",
    author="naveenap",
    author_email="pasupuletinaveena98@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naveenapasupuleti/fileprocessing",
    packages=setuptools.find_packages(),
    install_requires=['pandas','writer','json','openpyxl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)