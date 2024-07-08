# Converting from volume mixing ratio (vmr) to no density

- WACCM output is volume mixing ratio (mol/mol) as standard (mol of species per mol of air)

-	dens = ( vmr * 1e-6 * 1e2 * lev ) / ( kb * temp)
    
    - vmr is the volume mixing ratio (mol/mol)
    - x1e-6 is to go from m-3 to cm-3
    - x1e2 is to convert from Pa to hPa
    - lev is WACCM pressure in hPa
    - kb = Boltzmans constant = 1.380503e-23 JK-1
    - temp = WACCM temp (K)
