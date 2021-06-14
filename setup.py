import setuptools
setuptools.setup(
    name='pygcloud',
    version='1.0.0',
    author='Sacumen',
    author_email='jamie.rahman@sacumen.com',
    description='Library to connect with gcloud for file transfer.',
    license='Private',
    url='https://github.com/jamie-sacumen/',
    packages=find_packages(include=['pyaws', 'pyaws.clients']),
    package_data={"pygcloud": ["py.typed"]},
    include_package_data=True,
    install_requires=['google-cloud-storage==1.38.0'],
    setup_requires=['pytest-runner'],
    zip_safe=False,
    options={"bdist_wheel": {"universal": False}},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
    
