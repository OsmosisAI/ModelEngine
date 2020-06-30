import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open('VERSION', 'r') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='model_engine',
    version=version,
    packages=setuptools.find_packages(),
    url='https://github.com/osmosisai/modelengine',
    license='',  # TBD
    author='OsmosisAI, Inc.',
    author_email='contact@osmosisai.com',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'tensorflow>=2.2.0'
    ]
)
