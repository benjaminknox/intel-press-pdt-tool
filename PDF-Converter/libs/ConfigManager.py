import os
import logging
import ConfigParser

from libs.Singleton import Singleton

@Singleton
class ConfigManager(object):
    '''  Central class which handles any user-controlled settings '''

    def __init__(self, cfg_file='.pdfconverter.cfg'):
        self.conf = os.path.abspath(cfg_file)
        if not (os.path.exists(self.conf) and os.path.isfile(self.conf)):
            logging.critical(
                "No configuration file found at: %s." % self.conf
            )
            os._exit(1)
        logging.info('Loading config from: %s' % self.conf)
        self.config = ConfigParser.SafeConfigParser()
        self.config.readfp(open(self.conf, 'r'))
        self.__server__()
        self.__version__()

    def __server__(self):
        ''' Load network configurations '''
        self.server_port = self.config.getint("Server", 'port')
        self.address = self.config.get("Server", 'address')

    def __version__(self):
        ''' Version config file '''
        self.version = self.config.get("System", 'version')