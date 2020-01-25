# I love python packaging... Joking
# You don't have to modify anything here, it's just set to be able to work with different files using python <3
# https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#multiple-file-dependencies
import setuptools

setuptools.setup(
    name='1_pipeline_parts_pipeline_package',
    version='0.1',
    install_requires=[
        'apache-beam',
        'apache-beam[gcp]'
    ],
    packages=setuptools.find_packages(),
)
