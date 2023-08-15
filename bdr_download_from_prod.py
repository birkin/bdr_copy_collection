"""
Download from production script.
"""

import argparse, logging, os, pprint, shutil, subprocess, sys


## envars -----------------------------------------------------------
LOG_PATH = os.environ['COPY_COLL__LOG_PATH']
LOG_LEVEL = os.environ['COPY_COLL__LOG_LEVEL']
BDR_TOOLS_DIR_PATH = os.environ['COPY_COLL__BDR_TOOLS_DIR_PATH']   

sys.path.append( BDR_TOOLS_DIR_PATH )
import bdr_tools as bt


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
    
    ## find top pid -------------------------------------------------
    
    ## end def run_manager()


## helpers ----------------------------------------------------------

def find_top (pid):
    current_item = bt.Item(pid)
    api = current_item.api()
    relationships = api['relations']
    parents = [i['pid'] for i in relationships['isPartOf']]
    if parents:
        return [find_top(i) for i in parents]
    else:
        return pid





## caller handlers --------------------------------------------------

def parse_args() -> tuple:
    """ Parses arguments when module called via __main__ """
    description = '''Downloads items from the production BDR to be copied onto the dev instance (using a separate companion script).
    
    Usage examples:

        first...

        $ cd /path/to/bdr_copy_collection_project
        $ source ../env/bin/activate
        $ source ../settings_env.sh

        ...then...

        $ python ./bdr_download_from_prod.py --pid bdr:1234

        ...or...

        $ python ./bdr_download_from_prod.py --pid bdr:1234 --level thumbnail

        ...or, when implemented...

        $ python ./bdr_download_from_prod.py --collection_pid bdr:5678 --subcollection_pids bdr:9012,bdr:3456
        -------'''
    parser = argparse.ArgumentParser( description=description, formatter_class=argparse.RawTextHelpFormatter )
    parser.add_argument( '-p', '--pid', help='BDR item-pid; will download that item and all necessary connections (parent/child/etc).', type=str )
    parser.add_argument( '-c', '--collection_pid', help='(not yet implemented) BDR collection-pid; will download all items in that collection (BE CAREFUL! Some collections are extremely large!).', type=str )
    parser.add_argument( '-l', '--level', default='thumbnail', help='Specifies what resolution of images to download, or metadata only. Options are "metadata", "thumbnail" (default), or "full".', type=str )
    args: dict = vars( parser.parse_args() )
    log.debug( f'args, ```{args}```' )
    assert type(args) == dict, type(args)
    assert type(parser) == argparse.ArgumentParser, type(parser) 
    return ( parser, args )

def validate_args( args ) -> bool:
    """ Validates arguments when module called via __main__ """
    if args['collection_pid']:
        msg = '\nThis mode is not yet implemented; quitting\n'
        log.warning( msg )
        print( msg )
        valid = False
    elif args['pid'] and args['collection_pid']:
        err_msg = '\nonly one of `pid` or `collection_pid` should be specified; quitting\n'
        log.error( err_msg )
        print( err_msg )
        valid = False
    elif not args['pid'] and not args['collection_pid']:
        err_msg = '\none of `pid` or `collection_pid` must be specified; quitting\n'
        log.error( err_msg )
        print( err_msg )
        valid = False
    else:
        valid = True
    log.debug( f'valid, `{valid}`' )
    assert type(valid) == bool, type(valid)
    return valid

## dudermain --------------------------------------------------------

if __name__ == '__main__':
    log.debug( '\n\nstarting script' )
    ( parser, args ) = parse_args()
    args_valid: bool = validate_args( args )
    if not args_valid:
        parser.print_help()
        sys.exit( 0 )
    pid: str = args['pid']
    collection: str = args['collection_pid']
    level: str = args['level']
    run_manager( pid, collection, level )
    log.debug( 'script complete' )
