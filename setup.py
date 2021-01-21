import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wofi-projects",
    version="1.0.01",
    license="MIT",
    author="Sean Collings",
    author_email="sean@seanrcollings.com",
    description="Wofi Projects Menu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={"console_scripts": ["wofi-projects = wofi_projects.__main__:main"]},
)
