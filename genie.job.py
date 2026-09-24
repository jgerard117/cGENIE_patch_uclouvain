import config as cfg 

path = cfg.path
file = path+"/genie.job"

f = open(file, 'r')
data = f.readlines()
f.close()

for i in range(len(data)):
    if data[i] == "TRANSLATE_CONFIG=\"python ./translate_config.py\"\n":
        data[i] = "TRANSLATE_CONFIG=\"python2 ./translate_config.py\"\n"


f = open(file, 'w')
f.writelines(data)
f.close()
