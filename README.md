# Patch cGENIE UCLouvain

This is a small patch developped to modify files of the genie-main directory so that the model can compile on UCLouvain clusters (tipycally manneback). This patch modifies the folowing files:
- runmuffin.sh
- genie.job
- makefile.arc
- user.sh
- user.mak 

### How to use

##### Fresh install

From a fresh install of cGENIE, simply edit the homedir variable in the "config.py" file to indicate in what repo you have put the "cgenie.muffin" folder. Then simply run
```
bash patch_uclouvain.sh
```
and it will modify all needed files to be compatible with UCLouvain clusters. The patch automatically creates backup of all modified files *_backup*. If you want to come back to the original version of the files, then simply run
```
bash invert_patch.sh
```
to get rid of all changes. 

##### Update (like git pull)

From an update, the only difference is to start with a 
```
bash invert_patch.sh
```
to ensure that the files modification goes according to plan. Then simply act as if the model originates from a fresh install. 

### Compatibility

This patch is working on the latest available version of cGENIE v0.9.49 (11/03/2024). Newer versions could require additional modifications!
