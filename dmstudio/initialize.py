import win32com.client
import sys

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

    print 'Connected to Datamine:', oScript

    return oScript;



