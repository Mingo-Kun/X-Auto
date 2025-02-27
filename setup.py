from setuptools import setup, find_packages

setup(
    name="x-auto",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'tweepy',
        'schedule',
        'google-generativeai',
        'python-dotenv',
    ]
)
