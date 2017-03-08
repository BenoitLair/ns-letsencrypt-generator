from shutil import copytree
import sys
import os
import sys
import subprocess

class Pki_letsencrypt:
    '''Classe definissant la manipulation des applications permettant de generer des certificats letsencrypt'''
    
    def __init__(self,home_certs_dir):
        """Par defaut, notre surface est vide"""
        self.homedir = home_certs_dir
    
    def get_homedir(self):
        """Cette methode se charge de lire le homedir."""
        print(self.homedir)
    
    def del_homedir(self):
        """Cette methode permet d'effacer le homedir."""
        self.homedir = ""
        
    def set_homedir(self,parametre):
        """Cette methode permet de set le homedir."""
        self.homedir = parametre
        
    def get_list_of_certificates_in_prod(self):
        """Cette methode permet de retourner un tableau avec la liste des certificats"""
        #on va get la liste des cronjobs pour identifier les certificats en prod.
        
    def create_app_certificate(self,src_dir,dest_dir):
        """Cette methode sert a crer une nouvelle entite de certificat"""
        if os.path.exists(src_dir) == True and os.path.exists(dest_dir) == False:
            #copyfile(src_repository, dest_repository)
            print "creation nouveau directory"
            copytree(src_dir, dest_dir)
            return True
        else:
            return False
        
    def delete_app_certificate(self,force=False):
        """Cette methode sert a supprimer une entite de certificat"""
        if force == True:
            print "delete_app_certificate:<force=true>.\n"
            try:
                os.rmdir(app_dir)
            except OSError as ex:
                print(ex)
        elif force== False:
            print "delete_app_certificate:<force=false>.\n"
            
        
        
        
        
#def ecrire(self, message_a_ecrire):
        #"""Methode permettant d'ecrire"""
        ##if self.surface != "":
        ##    self.surface += "\n"
        ##self.surface += message_a_ecrire