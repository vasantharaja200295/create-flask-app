from setuptools import setup, find_packages

setup(
    name='create_flask_app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'create-flask-app = create_flask_app.main:main',
        ],
    },
)
