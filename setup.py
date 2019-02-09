from setuptools import find_packages, setup


setup(
    name="pyaudioreconstruction",
    version="0.1",
    description="",
    author="Ramsey Barghouti",
    license="GPL3",
    packages=find_packages(),
    setup_requires=["numpy"],
    install_requires=[
        "numpy",
        "librosa",
        "imageio",
        "lws",
    ],
    entry_points={
        "console_scripts": [
            "pyra=pyaudioreconstruction.cli:main"
        ]
    },
    zip_safe=False
)
