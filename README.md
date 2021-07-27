 # The program is writtin mostly in `Jupyter Notebook`
 
 
 creating all possible permutations from excel file and loading it into pandas data stracture.
 takes CarsData to start permutation,
 returns carsPrices.xlsx with calcuted car prices and carsCleaned to test the data.
 
 to run the docker file i converted the #juptyer file to python file (using the command `jupyter nbconvert --to script [YOUR_NOTEBOOK].ipynb`)
 
 1. to build a docker image `docker build -t taskauto .`
 2. to run the docker with a volume ( output files would be writin to the voulme) `docker run -d -v <SOURCE_DIR>:/home taskauto` where source_dir is the folder with code.
 ** to run manually inside a container `docker run -it taskauto bash`

