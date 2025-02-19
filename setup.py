from setuptools import setup

setup(
    name='word-detector',
    version='1.0.0',
    description='Word Detector',
    author='Raman',
    packages=['word_detector'],
    url="https://github.com/0x0raman/ScriptScribe",
    install_requires=['numpy', 'sklearn', 'opencv-python'],
    python_requires='>=3.7'
)
