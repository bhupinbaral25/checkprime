from setuptools import setup
setup(
    name="primecheck",                     
    version="0.0.1",                        
    author= "Bhupin Baral",                    
        
    description="This nodules checks wheather your number is prime or not ",
      
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',               
    py_modules=["primecheck"],           
    package_dir={'':'primecheck/src'},   
    install_requires=[]                    
)