from setuptools import setup, find_packages

setup(
    name="SampleA",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["sample_command = sample.sample:sample_command"]
    }
)