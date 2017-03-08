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



#dest file
print (sys.argv[1])
dest_repository=sys.argv[1]
#dest file
#print (sys.argv[2])
#dest_repository=sys.argv[2]


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
import Pki_letsencrypt

try:
        from Pki_letsencrypt import Pki_letsencrypt
except:
        print("Exception: Please provide correct directory path for pki_letsencrypt3 module")
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
current_src=os.getcwd()+"/letsencrypt-src/ns-letsencrypt/"
current_dst=os.getcwd()+"/"+dest_repository
print "current source : "+current_src

#print(os.path.isdir("/home/el"))
#print "test1 : ";
#print(os.path.exists(src_repository))
#print "test2 : ";
#print(os.path.exists(dest_repository))

#print os.getcwd()

# MAIN APPLICATION
mon_pki_le = Pki_letsencrypt(current_directory_pwd)
print "current src : "+current_src
print "current dst : "+current_dst
retour_create_certificate=mon_pki_le.create_app_certificate(current_src,current_dst)
if retour_create_certificate == True:
        print "retour cert create : True"
else:
        print "retour cert create : False"
#mon_pki_le.set_homedir('/home')
#mon_pki_le.get_homedir()
#mon_pki_le.del_homedir()
mon_pki_le.get_homedir()

#if os.path.exists(src_repository) == True and os.path.exists(dest_repository) == False:
    #copyfile(src_repository, dest_repository)
    #print "creation nouveau directory"
    #copytree(src_repository, dest_repository)
    

