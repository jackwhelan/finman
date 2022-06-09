'''
Module to load configuration options from
the application.ini file.
'''
import os
import configparser

class ConfigHandler:
    '''
    Class to handle the reading in and parsing
    of configuration files.
    '''
    def __init__(self, config_file_path='src/etc/application.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
        self.__set_config_profile()

    def __set_config_profile(self):
        '''
        Method to set the config profile based on
        the DATA_ACCESS_CONFIG_PROFILE env var.
        '''
        config_profile = os.getenv('DATA_ACCESS_CONFIG_PROFILE')
        if not config_profile:
            self.config = self.config['DEFAULT']
        else:
            self.config = self.config[config_profile]

    def __getitem__(self, key):
        if key in self.config:
            return self.config[key]
        raise Exception(f'{key} not set in configuration.')
