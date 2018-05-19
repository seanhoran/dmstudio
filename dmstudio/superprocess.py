'''
Coming soon
'''
from dmstudio import initialize
from dmstudio import dmcommands

oScript = initialize.studio(version=None)
dmc = dmcommands.init()

def dxf_to_dm(dxf_i, out_o, zone_f=None, zone_p=None):

    '''

    :param dxfin: File in dxf format. The dxfin can alos be provided as a full path
    :param outfile: Name of output file without the tr and pt suffix
    :param zone: zone field to be created in wireframe file
    :param zone_value: zone value - can be numeric or alphanumeric
    :return: returns a datamine tr and pt file
    '''

    oScript.ActiveProject.Data.LoadFile(dxf_i)
    obj3d = oScript.ActiveProject.Data.LastObjectAdded

    # are we going to write a zone field to wireframe?

    if zone_f==None:

        obj3d.SaveAsDatamineFile(outfile, oScript.ActiveProject.ExtendedPrecision, True, "")

    else:

        obj3d.SaveAsDatamineFile('_t1', oScript.ActiveProject.ExtendedPrecision, True, "")

        # check if zone_value is numeric or alphanumeric

        if type(zone_p) is float or type(zone_p) is int:

            expression = " '" + zone_f + "=" + str(zone_p) + " '"

        else:

            expression = " '" + zone_f + ";a24=" + '"' + zone_p + '"' + " '"

        dmc.extra('_t1tr', out_o + 'tr', expression=expression)
        dmc.copy('_t1pt', out_o + 'pt')
        dmc.delete(in_i='_t1tr')
        dmc.delete(in_i='_t1pt')

