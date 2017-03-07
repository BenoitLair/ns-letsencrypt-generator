#
#
#   APPLICATION DE GENERATION DE REPOSITORY NS-LETSENCRYPT
#   AUTHOR : LAIR BENOIT
#   CREATION : 07/03/2017
#
#
from shutil import copytree
import sys
import os

#source file
print (sys.argv[1])
src_repository=sys.argv[1]
#dest file
print (sys.argv[2])
dest_repository=sys.argv[2]


#print(os.path.isdir("/home/el"))
#print "test1 : ";
#print(os.path.exists(src_repository))
#print "test2 : ";
#print(os.path.exists(dest_repository))


if os.path.exists(src_repository) == True and os.path.exists(dest_repository) == False:
    #copyfile(src_repository, dest_repository)
    copytree(src_repository, dest_repository)

