# Run a python script on ARC4 that uses dask for parallel computations e.g. using the xarray library

Dask is a Python library for parallel computing. Xarray, a popular Python library for manipulating geoscience data and working with NetCDF files, has Dask built in. 

Opening datasets using ds = xarray.open_mfdataset(path + data\*2010\*), e.g. reading in monthly NetCDF files (data_2010-01.nc, data_2010-02.nc, etc...) for the full year of 2010, will automatically call dask to split the datasets into chunks which are then processed separately. E.g. if the full dataset is too big to fit into memory at once or you want to use many resources to manipulate the dataset faster.

There are many nuances with using dask, so for more comprehensive documentation, see:

- Xarray guide to dask - https://docs.xarray.dev/en/stable/user-guide/dask.html
- Dask guide to xarray - https://examples.dask.org/xarray.html
- Blog post introduction by Stephan Hoyer - https://stephanhoyer.com/2015/06/11/xray-dask-out-of-core-labeled-arrays/

The most basic example of its use is from a simple python script:

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

Xarray or any code using dask now use the available resources for computation. When using xarray, the code is usually the same as if you were not using dask, but there are some nuances which can be found in the documentation. E.g. computations are actually stored as instructions in 'dask.delayed' objects, and are not performed until explicitly told to (although some operations automatically trigger this too). Until then, some computations are performed on the metadata and potentially the first and last chunk, so you can inspect your dataset as you go along e.g. if you were running your code from a jupyter notebook.

line 9 frees up the resources and gracefully closes the client.

If the code is in a file called dask_file.py, it can then be submitted to ARC4 via a standard job submission script, e.g.

```bash
#!/bin/bash
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





