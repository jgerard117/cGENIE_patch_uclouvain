import config as cfg 

path = cfg.path
file = path+"/user.mak"

f = open(file, 'r')
data = f.readlines()
f.close()

for i in range(len(data)):
    if data[i] == "GENIE_ROOT        = $(HOME)/cgenie.muffin\n":
        data[i] = "GENIE_ROOT        = "+cfg.homedir+"/cgenie.muffin\n"
    if data[i] == "OUT_DIR           = $(HOME)/cgenie_output\n":
        data[i] = "OUT_DIR           = "+cfg.homedir+"/cgenie_output\n"
    if data[i] == "NETCDF_DIR=/usr/local\n":
        data[i] = "# NETCDF_DIR=/usr/local\nNETCDFC_DIR=$(EBROOTNETCDFMINCPLUSPLUS4)\nNETCDFF_DIR=$(EBROOTNETCDFMINFORTRAN)\nNETCDF_DIR=$(EBROOTNETCDF)\n\n"
        data[i+1] = "### domino ###\n"

f = open(file, 'w')
f.writelines(data)
f.close()
