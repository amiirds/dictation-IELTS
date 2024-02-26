from setuptools import setup

APP = ['main.py']  # Replace 'main.py' with the name of your main script

OPTIONS = {
    'packages': ['random', 'PyDictionary', 'gtts', 'pygame', 'tkinter'],  # Add 'tkinter' here
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
