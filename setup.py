import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uspto_patent_data_parser", # Replace with your own username
    version="0.0.1",
    author="Charles Foster",
    author_email="cfoster0m@gmail.com",
    description="Modified parser from TamerKhraisha for USPTO grants.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bs4',
        'pandas',
        'numpy',
        'requests',
    ],
)
