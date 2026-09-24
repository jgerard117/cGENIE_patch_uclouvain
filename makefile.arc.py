import config as cfg 

path = cfg.path
file = path+"/makefile.arc"

f = open(file, 'r')
data = f.readlines()
f.close()

for i in range(len(data)):
    if data[i] == "PYTHON = python\n":
        data[i] = "PYTHON = python2\n"
    if data[i] == "  FFLAGS += -Wall -fimplicit-none\n":
        data[i] = "  FFLAGS += -Wall -fimplicit-none -fallow-argument-mismatch\n"
        data[i+1] = "  FFLAGS += -fopenmp\n"
    if data[i] == "###  LDFLAGS += -fopenmp\n":
        data[i] = "  LDFLAGS += -fopenmp\n"
        for line in range(18):
            data[i+line+1] = ""
    if data[i] == "    #FFLAGS += -Wextra\n":
        data[i] = "    FFLAGS += -Wextra\n"
    if data[i] == "    FFLAGS += -fconserve-stack\n":
        data[i] = "    #FFLAGS += -fconserve-stack\n"
    if data[i] == "  endif\n" and data[i+1] == "  ifeq ($(BUILD),TEST)\n" and data[i+2] == "    FFLAGS += -g -ffpe-trap=zero,overflow,invalid -O0 -Wall -fbounds-check\n":
        for line in range(10):
            data[i+line] = ""
    if data[i] == "NETCDF= $(LIB_SEARCH_FLAG)$(PATH_QUOTE)$(NETCDF_DIR)/lib$(PATH_QUOTE) $(LIB_FLAG)$(NETCDF_NAME) $(LIB_FLAG)$(NETCDF_NAMEF)\n":
        data[i] = "NETCDF_NAMEC=$(NETCDF_NAME)_c++\nNETCDF= $(LIB_SEARCH_FLAG)$(PATH_QUOTE)$(NETCDF_DIR)/lib$(PATH_QUOTE) $(LIB_FLAG)$(NETCDF_NAME) $(LIB_SEARCH_FLAG)$(PATH_QUOTE)$(NETCDFF_DIR)/lib$(PATH_QUOTE) $(LIB_FLAG)$(NETCDF_NAMEF) $(LIB_SEARCH_FLAG)$(PATH_QUOTE)$(NETCDFC_DIR)/lib$(PATH_QUOTE) $(LIB_FLAG)$(NETCDF_NAMEC)\n"
    if data[i] == "NETCDF_INC=$(INC_FLAG)$(PATH_QUOTE)$(NETCDF_DIR)/include$(PATH_QUOTE)\n":
        data[i] = "NETCDF_INC=$(INC_FLAG)$(PATH_QUOTE)$(NETCDF_DIR)/include$(PATH_QUOTE) $(INC_FLAG)$(PATH_QUOTE)$(NETCDFF_DIR)/include$(PATH_QUOTE) $(INC_FLAG)$(PATH_QUOTE)$(NETCDFC_DIR)/include$(PATH_QUOTE)\n"


f = open(file, 'w')
f.writelines(data)
f.close()
