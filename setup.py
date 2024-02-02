import setuptools

name = "quackify"
version = "1.0.0"
description = "Quackify es una biblioteca para Python que emula diversas funciones del duckyscript."
author = "Euronymou5"
url = "https://github.com/Euronymou5/Quackify"
license = "Mozilla Public License 2.0"
install_requires = ["pyautogui", "pynput"]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    url=url,
    license=license,
    packages=["quackify"],
    author=author,
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)
