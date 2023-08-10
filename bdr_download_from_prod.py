"""
Download from production script.
"""

import argparse, logging, os, pprint, shutil, subprocess, sys

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


def run_manager( pid: str, collection: str, level: str ) -> None:
    """ Manages download flow.
        Called by dundermain. """
    
    ## gather args --------------------------------------------------
    
    ## end def run_manager()


class Runner():

    def __init__(self) -> None:
        self.pid = ''
        self.collection_pid = ''
        self.level = ''


## dudermain --------------------------------------------------------

# if __name__ == '__main__':
#     log.debug( '\n\nstarting dundermain...' )
#     run_manager()
#     log.debug( 'processing complete' )


# parser = argparse.ArgumentParser(description='Downloads items from the production BDR to be copied onto the dev instance (using a companion script in a separate step).')
# parser.add_argument("-p", "--pid", help="Provide a BDR pid to download that item and all necessary connections (parent/child/etc).", type=str)
# parser.add_argument("-c", "--collection", help="Provide a BDR collection pid to download all items in that collection (BE CAREFUL! Some collections are extremely large!).", type=str)
# parser.add_argument("-l", "--level", default='thumbnail', help="Specifies what resolution of images to download, or metadata only. Options are 'metadata', 'thumbnail' (default), or 'full'.", type=str)
# args = parser.parse_args()
# collection_to_grab = args.collection
# if collection_to_grab:
#     print('This mode is not yet implemented.')
#     sys.exit(0)
# pid_to_grab = args.pid
# print(pid_to_grab)
# level = args.level



# -------------------------------------------------------------------
# caller handlers
# -------------------------------------------------------------------


def parse_args() -> dict:
    """ Parses arguments when module called via __main__ """
    parser = argparse.ArgumentParser( description='Downloads items from the production BDR to be copied onto the dev instance (using a companion script in a separate step).' )
    parser.add_argument( '--pid', '-p', help='Provide a BDR pid to download that item and all necessary connections (parent/child/etc).', type=str )
    parser.add_argument( '--collection', '-c', help='Provide a BDR collection pid to download all items in that collection (BE CAREFUL! Some collections are extremely large!).', type=str )
    parser.add_argument( '--level', '-l', default='thumbnail', help='Specifies what resolution of images to download, or metadata only. Options are "metadata", "thumbnail" (default), or "full".', type=str )
    args: dict = vars( parser.parse_args() )
    log.debug( f'args, ```{pprint.pformat(args)}```' )
    return args

def validate_args( args ) -> None:
    """ Validates arguments when module called via __main__ """
    if not args['pid'] and not args['collection']:
        err_msg = 'no pid or collection-pid specified; quitting'
        log.error( err_msg )
        print( err_msg )
        sys.exit( 0 )
    pass

if __name__ == '__main__':
    args: dict = parse_args()
    args_valid = validate_args( args )
    pid: str = args['pid']
    collection: str = args['collection']
    level: str = args['level']
    run_manager( pid, collection, level )
