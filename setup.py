from setuptools import setup


setup(
    name='Terminal Time Tracker',
    version='0.1',
    py_modules=['ttt'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ttt=ttt:cli
    ''',
)
