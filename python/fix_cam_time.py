# A python function that subtracts 15 days from the date field - use it cautiously! 
# It can fix the issue in monthly (h0) history files where the date field is the time 
# the data are written and not the center of the averaging period. 
# So in h0s the date may be 2001-02-01 but it refers to the January mean.

def fix_cam_time(ds):

    from cftime import DatetimeNoLeap
    
    months = ds.time_bnds.isel(nbnd=0).dt.month.values
    years = ds.time_bnds.isel(nbnd=0).dt.year.values
    dates = [DatetimeNoLeap(year, month, 15) for year, month in zip(years, months) ]
    ds = ds.assign_coords(time = dates)
    
    return ds
