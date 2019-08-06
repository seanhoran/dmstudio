import win32com.client
import sys
import glob
import numpy as np

def _scriptinit(dm_object):
    '''
    _scriptinit
    -----------

    Initialize the Studio COM object. Internal function.

    Parameters:
    -----------

    studio_object: str
        Datamine studio COM object to initialize

    Returns:
    --------

    ActiveX connection
    '''

    return win32com.client.Dispatch(dm_object);

def studio(version):
    '''
    studio
    ------

    Datamine Studio Initialization. Versions Studio3, StudioRM and StudioEM supported

    Parameters:
    -----------

    version: str
        Datamine studio version

    Tries to connect to studio RM first.
    Need a better way to do this.
    '''

    oScript = None

    _make_dmdir()

    if version == 'StudioRM':
        oScript = _scriptinit("Datamine.StudioRM.Application")
    elif version == 'Studio3':
        oScript = _scriptinit("Datamine.Studio.Application")
    elif version == 'StudioEM':
        oScript = _scriptinit("Datamine.StudioEM.Application")
    else:
        # no version given, will try to find a valid version
        try:
            oScript = _scriptinit("Datamine.StudioRM.Application")
        except:
            try:
                oScript = _scriptinit("Datamine.Studio.Application")
            except:
                try:
                    oScript = _scriptinit("Datamine.StudioEM.Application")
                except:
                    assert False, "No valid Studio version is active"

    # print 'Connected to Datamine:', oScript

    return oScript;

def dmFile():

    print("here")
    # assert oDmFile = _scriptinit("DmFile.DmTableADO"), "Could not initialize dmTableADO"


def _make_dmdir():
    
    '''
    _make_dmdir
    -----------
    
    Internal function which creates a local ``_init_.py`` and python file ``dmdir.py`` which contains a list of dm files in the local 
    Datamine project directory passed to variables with name of file without dm file extension and leading and trailing underscores. 
    
    The purpose of the local python file is to facilitate importing the filenames as variables which can be referenced directly in the
    scripts. 
    
    Usage:
    ------
    
    >>>import dmdir as f
    >>>print f._someDmFile_
    someDmFile
    
    The imported variables can be used as inputs in scripts:
    
    >>>from dmstudio import dmcommands
    >>> dmc = dmcommands.init()
    >>> dmc.copy(in_i=f._someDmFile_, out_o='someDmFile2')
    
    '''

    dmdir_init = open('__init__.py', 'w')
    dmdir_init.write("'''\n")
    dmdir_init.write("Initialization file to enable importing of dmdir.py\n")
    dmdir_init.write("'''\n")
    dmdir_init.close()

    dmdir_f = open('dmdir.py', 'w')
    dmdir_f.write("'''\n")
    dmdir_f.write("List of datamine files in active datamine project directory\n")
    dmdir_f.write("\n")
    dmdir_f.write("This file will populate after initializing the script for the first time and will update after each command.\n")
    dmdir_f.write("\n")
    dmdir_f.write("Usage:\n")
    dmdir_f.write("------\n")
    dmdir_f.write("\n")
    dmdir_f.write(">>import dmdir as f\n")
    dmdir_f.write(">>print f._someDmFile_\n")
    dmdir_f.write("someDmFile\n")
    dmdir_f.write("\n")
    dmdir_f.write("'''\n")
    dmdir_f.write("\n")

    for infile in glob.glob("*.dm"):
        outname = np.str.split(infile, '.')[0]
        dmdir_f.write('_'+ outname + "_='" + outname + "'\n")

    dmdir_f.close()



