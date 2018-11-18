try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "author name here...",
    "url": "url to get it at",
    "download_url": "Where to download it",
    "author_email": "email here...",
    "version": "0.1",
    "install_requires": ["cocos2d", "nose"],
    "packages": ["invaders"],
    "scripts": ["bin/invaders"],
    "name": "invaders"
}

setup(**config)
