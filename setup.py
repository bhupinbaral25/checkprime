from setuptools import setup
setup(
    name="primecheck",                     
    version="0.0.1",                        
    author= "Bhupin Baral", 
    url = 'https://github.com/bhupinbaral25/primecheck',      
    download_url ='https://github.com/bhupinbaral25/primecheck/releases/tag/0.0.1'             
        
    description="This nodules checks wheather your number is prime or not ",
      
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',               
    py_modules=["primecheck"],           
    package_dir={'':'primecheck/primecheck'}, 
      
    install_requires=[]                    
)