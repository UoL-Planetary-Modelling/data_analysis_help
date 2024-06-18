# Run a python script on ARC4 that uses dask for parallel computations e.g. using the xarray library

Dask is a Python library for parallelised data manipulation. Xarray, a popular Python library for manipulating geoscience data and working with NetCDF files, has Dask built in. 

Opening datasets using ds = xarray.open_mfdataset(path + files\*2010\*), e.g. reading in monthly mean NetCDF files (files_2010-01.nc, files_2010-02.nc, etc...) for the full year of 2010, will automatically call dask to split the datasets into chunks which are then processed separately. E.g. if the full dataset is too big to fit into memory at once.

There are many nuances with using dask, so for more comprehensive documentation, see:

- https://docs.xarray.dev/en/stable/user-guide/dask.html
- https://examples.dask.org/xarray.html
- Blog post introduction by Stephan Hoyer - https://stephanhoyer.com/2015/06/11/xray-dask-out-of-core-labeled-arrays/

The most basic example of its use is:

```python
1 from dask.distributed import Client
2 import xarray as xr
3
4 if __name__='__main__':
5    client = Client()
6
7   # Perform computations using xarray
8
9    client.close()
```

line 1 imports the Client function that later grabs available resources and makes them usable from the script.

line 4 tells python where to start executing the code. This doesn't need to be there for simple scripts that are executed serially, but if you want to use dask, it does.

line 5 tells the script what the available resources are and grabs them for use in the script via a 'client' (e.g. 40 cores and 192 GB of memory if running this code on a single ARC4 node).

Any code with dask integrated in it will now use the available resources for computation. These are usually performed exactly the same as if you were not using dask, but there are some nuances which can be found in the documentation.

line 9 frees up the resources and gracefully closes the client.

If the code is in a file called dask_file.py, it can then be submitted to via a standard job submission script, e.g.

```bash
#!/bin/bash -f
#$ -V
#$ -cwd
#$ -l h_rt=01:00:00
#$ -j y
#$ -l nodes=1
#$ -l h_vmem=4G
module load anaconda # Makes conda available to load your environments
source activate my_env # Activate your environment that has xarray and dask installed
python dask_file.py # Run python file
```





