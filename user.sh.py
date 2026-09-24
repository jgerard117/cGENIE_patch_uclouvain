import config as cfg 

path = cfg.path
file = path+"/user.sh"

f = open(file, 'r')
data = f.readlines()
f.close()

for i in range(len(data)):
    if data[i] == "CODEDIR=~/cgenie.muffin\n":
        data[i] = "HOMEDIR="+cfg.homedir+"\n\nCODEDIR=${HOMEDIR}/cgenie.muffin\n"
    if data[i] == "OUTROOT=~/cgenie_output\n":
        data[i] = "OUTROOT=${HOMEDIR}/cgenie_output\n"
    if data[i] == "ARCHIVEDIR=~/cgenie_archive\n":
        data[i] = "ARCHIVEDIR=${HOMEDIR}/cgenie_archive\n"
    if data[i] == "LOGDIR=~/cgenie_log\n":
        data[i] = "LOGDIR=${HOMEDIR}/cgenie_log\n"

f = open(file, 'w')
f.writelines(data)
f.close()
