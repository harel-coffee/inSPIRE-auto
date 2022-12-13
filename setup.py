
from setuptools import setup

setup(
    name='inspirems',
    version=1.4,
    description='Helping to integrate Spectral Predictors and Rescoring.',
    author='John Cormican, Juliane Liepe',
    author_email='juliane.liepe@mpinat.mpg.de',
    packages=[
        'inspire',
        'inspire.input',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'inspire',
        'inspire.input',
    ],
    entry_points={
        'console_scripts': [
            'inspire=inspire.run:main'
        ]
    },
    python_requires='>=3.8',
    install_requires=[
        'absl-py==0.15.0',
        'astunparse==1.6.3',
        'biopython==1.79',
        'Bottleneck==1.3.4',
        'cachetools==5.2.0',
        'charset-normalizer==2.1.0',
        'click==8.1.3',
        'cycler==0.11.0',
        'flatbuffers==1.12',
        'fonttools==4.36.0',
        'gast==0.4.0',
        'google-auth==2.10.0',
        'google-auth-oauthlib==0.4.6',
        'google-pasta==0.2.0',
        'greenlet==1.1.2',
        'grpcio==1.34.1',
        'h5py==3.1.0',
        'idna==3.3',
        'importlib-metadata==4.12.0',
        'joblib==1.1.0',
        'kaleido==0.2.1',
        'keras-nightly==2.5.0.dev2021032900',
        'Keras-Preprocessing==1.1.2',
        'kiwisolver==1.4.4',
        'llvmlite==0.39.0',
        'lxml==4.9.1',
        'Markdown==3.4.1',
        'MarkupSafe==2.1.1',
        'mokapot==0.8.3',
        'matplotlib==3.5.3',
        'ms2pip==3.9.0',
        'numba==0.56.0',
        'numexpr==2.8.3',
        'numpy==1.19.5',
        'oauthlib==3.2.0',
        'opt-einsum==3.3.0',
        'packaging==21.3',
        'pandas==1.4.3',
        'Pillow==9.2.0',
        'plotly==5.10.0',
        'protobuf==3.19.4',
        'psutil==5.9.1',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pyparsing==3.0.9',
        'PyPDF2==2.10.2',
        'pyteomics==4.5.4',
        'python-dateutil==2.8.2',
        'pytz==2022.2.1',
        'PyYAML==6.0',
        'requests==2.28.1',
        'requests-oauthlib==1.3.1',
        'rsa==4.9',
        'scikit-learn==1.1.2',
        'scipy==1.9.0',
        'six==1.15.0',
        'sklearn==0.0',
        'spectrum-utils==0.3.5',
        'SQLAlchemy==1.4.40',
        'tables==3.7.0',
        'tenacity==8.0.1',
        'tensorboard==2.9.1',
        'tensorboard-data-server==0.6.1',
        'tensorboard-plugin-wit==1.8.1',
        'tensorflow==2.5.0',
        'tensorflow-estimator==2.5.0',
        'termcolor==1.1.0',
        'threadpoolctl==3.1.0',
        'tomlkit==0.11.0',
        'tqdm==4.64.0',
        'triqler==0.6.2',
        'typing-extensions==3.7.4.3',
        'urllib3==1.26.9',
        'Werkzeug==2.1.2',
        'wrapt==1.12.1',
        'xgboost==1.6.1',
        'zipp==3.8.1',
    ],
    project_urls={
        'Homepage': 'https://github.com/QuantSysBio/inSPIRE',
        'Tracker': 'https://github.com/QuantSysBio/inSPIRE/issues',
    },
)
