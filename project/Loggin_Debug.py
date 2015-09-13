__author__ = 'Alessio'

from project import app
import logging.handlers
from logging import FileHandler, Formatter

from datetime import *



class Logging(logging.FileHandler):

    @classmethod
    def __init__(self,user_connect_=None):

        self.user_connect = user_connect_
        self.application = app\


    @classmethod
    def create_login_info(self,user,time,url):
        self.logging = FileHandler('icollect_info.log')
        self.logging.setLevel(logging.DEBUG)
        self.logging.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.application.logger.addHandler(self.logging)
        create_dict_to_loggin_info = dict({'user_connect':user,'time':time,'url':url})
        self.application.logger.info('Info LogIn' + ":" + str(create_dict_to_loggin_info))

    @classmethod
    def create_logout_info(self,user,time):
        self.logging = FileHandler('icollect_info.log')
        self.logging.setLevel(logging.DEBUG)
        self.logging.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.application.logger.addHandler(self.logging)
        create_dict_to_loggin_info = dict({'user_connect':user,'time':time})
        self.application.logger.info('Info Logout' + ":" + str(create_dict_to_loggin_info))

if __name__ == '__main__':
        pass