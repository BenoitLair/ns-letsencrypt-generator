#
#
#   APPLICATION DE GENERATION DE REPOSITORY NS-LETSENCRYPT
#   AUTHOR : LAIR BENOIT
#   CREATION : 07/03/2017
#
#   REQUIRES : 
#   pip install python-crontab
#
#try:
#    import pymysql
#    pymysql.install_as_MySQLdb()
#except ImportError:
#    pass
from shutil import copytree
import sys
import os
import sys
import subprocess



#source file
print (sys.argv[1])
src_repository=sys.argv[1]
#dest file
print (sys.argv[2])
dest_repository=sys.argv[2]

#
# Append location of Pki_letsencrypt.py to PYTHONPATH
#

#print (sys.argv[1])
#try:
        #sys.path.append(sys.argv[1])
#except Exception as e:
        #print("Exception: "+str(e.args))

#print(os.environ['PYTHONPATH'])
#print(sys.path)
#from PkiLetsencrypt import Pki_letsencrypt

try:
        from Pki_letsencrypt import Pki_letsencrypt
except:
        print("Exception: Please provide correct directory path for pki_letsencrypt2 module")
        sys.exit()

#import python-crontab
try:
        from crontab import CronTab
except:
        print("Exception: Please provide correct directory path for python-crontab module")
        sys.exit()
# reste a importer python cronjobs pour gerer ls cronjobs de root.

current_directory_pwd=os.getcwd()
#set source ns-letsencrypt
current_source=os.getcwd()+"/letsencrypt-src/ns-letsencrypt/"
#print "current source : "+current_source

#print(os.path.isdir("/home/el"))
#print "test1 : ";
#print(os.path.exists(src_repository))
#print "test2 : ";
#print(os.path.exists(dest_repository))

#print os.getcwd()
mon_pki_le = Pki_letsencrypt(current_directory_pwd)
#mon_pki_le.set_homedir('/home')
#mon_pki_le.get_homedir()
#mon_pki_le.del_homedir()
mon_pki_le.get_homedir()

if os.path.exists(src_repository) == True and os.path.exists(dest_repository) == False:
    #copyfile(src_repository, dest_repository)
    copytree(src_repository, dest_repository)
    

