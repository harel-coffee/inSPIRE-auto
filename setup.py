
from setuptools import setup

setup(
    name='inspirems',
    version='2.0rc01',
    description='Helping to integrate Spectral Predictors and Rescoring.',
    author='John Cormican, Juliane Liepe, Martin Pasen',
    author_email='juliane.liepe@mpinat.mpg.de',
    packages=[
        'inspire',
        'inspire.input',
        'inspire.quant',
        'inspire.epitope',
        'inspire.plot_spectra',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'inspire',
        'inspire.input',
        'inspire.quant',
        'inspire.epitope',
        'inspire.plot_spectra',
    ],
    entry_points={
        'console_scripts': [
            'inspire=inspire.run:run_inspire'
        ]
    },
    python_requires='==3.11',
    install_requires=[
        'absl-py==2.0.0',
		'astunparse==1.6.3',
		'biopython==1.81',
		'cachetools==5.3.2',
		'certifi==2023.11.17',
		'charset-normalizer==3.3.2',
		'contourpy==1.2.0',
		'cycler==0.12.1',
        'docker==7.0.0',
		'flatbuffers==23.5.26',
		'fonttools==4.45.1',
		'gast==0.5.4',
		'google-auth==2.23.4',
		'google-auth-oauthlib==1.1.0',
		'google-pasta==0.2.0',
		'grpcio==1.59.3',
		'h5py==3.10.0',
		'idna==3.4',
		'joblib==1.3.2',
        'kaleido==0.2.1',
		'keras==2.15.0',
		'kiwisolver==1.4.5',
		'libclang==16.0.6',
		'lxml==4.9.3',
		'Markdown==3.5.1',
		'MarkupSafe==2.1.3',
		'matplotlib==3.8.2',
		'ml-dtypes==0.2.0',
		'numpy==1.26.2',
		'oauthlib==3.2.2',
		'opt-einsum==3.3.0',
		'packaging==23.2',
		'pandas==2.1.3',
		'patsy==0.5.3',
		'Pillow==10.1.0',
		'plotly==5.18.0',
		'polars==0.19.15',
		'protobuf==4.23.4',
        'pyarrow==14.0.1',
		'pyasn1==0.5.1',
		'pyasn1-modules==0.3.0',
		'pyparsing==3.1.1',
		'PyPDF2==3.0.1',
		'pyteomics==4.6.3',
		'python-dateutil==2.8.2',
		'pytz==2023.3.post1',
		'PyYAML==6.0.1',
		'requests==2.31.0',
		'requests-oauthlib==1.3.1',
		'rsa==4.9',
		'scikit-learn==1.3.2',
		'scipy==1.11.4',
		'seaborn==0.13.0',
		'six==1.16.0',
		'statsmodels==0.14.0',
		'tenacity==8.2.3',
		'tensorboard==2.15.1',
		'tensorboard-data-server==0.7.2',
		'tensorflow==2.15.0',
		'tensorflow-estimator==2.15.0',
		'termcolor==2.3.0',
		'threadpoolctl==3.2.0',
		'typing_extensions==4.8.0',
		'tzdata==2023.3',
		'urllib3==2.1.0',
		'Werkzeug==3.0.1',
		'wrapt==1.14.1',
		'xgboost==2.0.2',
        'xlsxwriter==3.1.9',
    ],
    project_urls={
        'Homepage': 'https://github.com/QuantSysBio/inSPIRE',
        'Tracker': 'https://github.com/QuantSysBio/inSPIRE/issues',
    },
)
