from setuptools import setup, find_packages

setup(
    name="terminal-tamagotchi",
    version="1.0.0",
    description="A nostalgic virtual pet that lives in your command line",
    author="Your Name",
    py_modules=["tamagotchi"],
    entry_points={
        "console_scripts": [
            "tamagotchi=tamagotchi:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)