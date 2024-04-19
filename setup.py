from setuptools import setup, find_packages

setup(
    name='gpt_trans',
    version='0.0.4',
    py_modules=['gpt_trans'],
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langchain_community',
        'langchain_core',
        'langchain_openai',
        'tqdm',
        'argparse',
    ],
    entry_points={
        'console_scripts': ['gpt_trans=gpt_trans.main:main'],
    },
    description='None',
    author='zc',
    author_email='277584121@qq.com',
    url='https://github.com/zc277584121/GPTTranslator',

)
