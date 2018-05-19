import win32com.client
import sys
import glob
import numpy as np

def _scriptinit(studio_object):
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

    return win32com.client.Dispatch(studio_object);

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

def _make_dmdir():

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



