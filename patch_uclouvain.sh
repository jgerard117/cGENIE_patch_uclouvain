# Main file for cGENIE patch 

# Path of the genie-main repo
path=$(python3 config_bash.py)

# Make a backup of all the files that will be modified
for file in runmuffin.sh genie.job makefile.arc user.sh user.mak
do 
  if ! test -f $path/"$file"_backup 
  then
    echo "$path/"$file"_backup does not exist and has been 'backuped'."
    cp $path/$file $path/"$file"_backup
  else
    echo "$path/$file has already been 'backuped'."
  fi
done

# Execute python scripts to modify all the required files
python3 runmuffin.sh.py
python3 genie.job.py
python3 makefile.arc.py
python3 user.sh.py
python3 user.mak.py
