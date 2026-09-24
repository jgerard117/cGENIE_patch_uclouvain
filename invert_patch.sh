path=$(python3 config_bash.py)

for file in runmuffin.sh genie.job makefile.arc user.sh user.mak
do 
  if test -f $path/"$file"_backup 
  then
    echo "$path/"$file"_backup has been copy on main files."
    mv $path/"$file"_backup $path/$file
  else
    echo "$path/"$file"_backup does not exist."
  fi  
done
