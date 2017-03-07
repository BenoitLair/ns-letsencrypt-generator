#
#
#   APPLICATION DE GENERATION DE REPOSITORY NS-LETSENCRYPT
#   AUTHOR : LAIR BENOIT
#   CREATION : 07/03/2017
#
#
from shutil import copyfile
import sys

#source file
print (sys.argv[0])
src_repository=sys.argv[0]
#dest file
print (sys.argv[1])
dest_repository=sys.argv[1]


#copyfile(src_repository, dest_repository)
copy(src_repository, dest_repository)