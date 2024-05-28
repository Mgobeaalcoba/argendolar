from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='argendolar',
    version='1.1.2',
    packages=find_packages(),
    install_requires=['pandas', 'requests'],
    author='Mariano Gobea Alcoba',
    author_email='gobeamariano@gmail.com',
    description='A package to get the exchange rates of the different types of dollars and others currencies in Argentina.',
    long_description=long_description,  # Usa el contenido del README.md como descripción larga
    long_description_content_type="text/markdown",  # Especifica el tipo de contenido como markdown
    url='https://github.com/Mgobeaalcoba/argendolar',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.8',
)