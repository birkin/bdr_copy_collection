"""
Download from production script.
"""

import logging, os, shutil, subprocess

## envars -----------------------------------------------------------
LOG_PATH = os.environ['COPY_COLL__LOG_PATH']
LOG_LEVEL = os.environ['COPY_COLL__LOG_LEVEL']


## set up logging ---------------------------------------------------
level_dict = { 'DEBUG': logging.DEBUG, 'INFO': logging.INFO }
desired_level = level_dict[ LOG_LEVEL ]
logging.basicConfig( 
    filename=LOG_PATH,
    level=desired_level,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', 
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)
log.debug( 'log set' )


def run_manager():
    """ Manages download flow.
        Called by dundermain. """
    
    ## gather args --------------------------------------------------
    
    ## end def run_manager()


## helper functions -------------------------------------------------


## dudermain --------------------------------------------------------

if __name__ == '__main__':
    log.debug( '\n\nstarting dundermain...' )
    run_manager()
    log.debug( 'processing complete' )
