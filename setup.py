from setuptools import setup

setup(
    name='gpt_translator',
    version='0.0.1',
    py_modules=['gpt_translator'],
    install_requires=[
        'langchain',
        'langchain_community',
        'langchain_core',
        'langchain_openai',
        'tqdm',
        'argparse',
    ],
    entry_points={
        'console_scripts': ['gpt_translator=gpt_translator.main:main'],
    },
)
