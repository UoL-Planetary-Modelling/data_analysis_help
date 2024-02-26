def fix_cam_time(ds):

    from cftime import DatetimeNoLeap
    
    months = ds.time_bnds.isel(nbnd=0).dt.month.values
    years = ds.time_bnds.isel(nbnd=0).dt.year.values
    dates = [DatetimeNoLeap(year, month, 15) for year, month in zip(years, months) ]
    ds = ds.assign_coords(time = dates)
    
    return ds