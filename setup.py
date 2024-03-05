from setuptools import setup, find_packages

setup(
    name='webtokentracker',
    version='1.0.0',
    description='Aplikasi web untuk melacak dan menganalisis portofolio token ETH Anda',
    author='AbdulRochimDev',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-CORS',
    ],
    entry_points={
        'console_scripts': [
            'webtokentracker = nama_modul_anda:app.run',
        ],
    },
)
