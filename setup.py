import setuptools


__packagename__ = 'malaya-speech'


def readme():
    with open('README-pypi.rst', 'rb') as f:
        return f.read().decode('UTF-8')


setuptools.setup(
    name = __packagename__,
    packages = setuptools.find_packages(),
    version = '0.0.1.1',
    python_requires = '>=3.6.*',
    description = 'Speech-Toolkit for bahasa Malaysia, powered by Deep Learning Tensorflow.',
    long_description = readme(),
    author = 'huseinzol05',
    author_email = 'husein.zol05@gmail.com',
    url = 'https://github.com/huseinzol05/malaya-speech',
    download_url = 'https://github.com/huseinzol05/malaya-speech/archive/master.zip',
    keywords = ['nlp', 'bm'],
    install_requires = [
        'tensorflow>=1.14,<2.0',
        'numpy',
        'librosa',
        'soundfile',
        'herpetologist',
        'dataclasses',
        'python_speech_features',
        'tqdm',
    ],
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
