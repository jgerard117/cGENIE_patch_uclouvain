import config as cfg

path = cfg.path
file = path+"/runmuffin.sh"

f = open(file, 'r')
data = f.readlines()
f.close()

for i in range(len(data)):
    if data[i][0:7] == "HOMEDIR":
        data[i] = "HOMEDIR="+cfg.homedir+"\n"
    if data[i][0:6] == "export" and data[i] != "export OMP_NUM_THREADS\n":
        data[i] = "#"+data[i]
    if data[i] == "echo ma_expid_name=$RUNID >> $CONFIGPATH/$CONFIGNAME\n":
        data[i] = ""


f = open(file, 'w')
f.writelines(data)
f.close()
