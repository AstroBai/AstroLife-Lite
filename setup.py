from setuptools import setup, find_packages

setup(
    name="astrolife",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["main"],  
    entry_points={
        "console_scripts": [
            "astrolife=main:main_entry",
        ],
    },
    install_requires=[
        'numpy',
        'pygame',
        'pygame_gui',
        'matplotlib',
        'glob',
        'json'
    ],
)
