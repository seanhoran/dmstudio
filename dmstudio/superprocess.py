'''
Coming soon
'''
from dmstudio import initialize
from dmstudio import dmcommands
import numpy as np
try:
    import pyrpa.io as io
except:
    print("pyrpa module not found, only available to SLR employees")

oScript = initialize.studio(version=None)
dmc = dmcommands.init()

def dxf_to_dm(dxf_i, out_o, zone_f=None, zone_p=None):

    '''

    :param dxf_i: File in dxf format. The dxfin can alos be provided as a full path
    :param out_o: Name of output file without the tr and pt suffix
    :param zone_f: zone field to be created in wireframe file
    :param zone_p: zone value - can be numeric or alphanumeric
    :return: returns a datamine tr and pt file
    '''

    assert np.str.split(dxf_i, ".")[-1] == 'dxf', "Input file is not a dxf"

    dmc.oScript.ActiveProject.Data.LoadFile(dxf_i)
    obj3d = oScript.ActiveProject.Data.LastObjectAdded

    if zone_f==None:
        obj3d.SaveAsDatamineFile(out_o, oScript.ActiveProject.ExtendedPrecision, True, "")
        obj3d.Unload()

    else:
        obj3d.SaveAsDatamineFile('_t1', oScript.ActiveProject.ExtendedPrecision, True, "")
        obj3d.Unload()

        # check if zone_value is numeric or alphanumeric

        if type(zone_p) is float or type(zone_p) is int:
            expression = " '" + zone_f + "=" + str(zone_p) + " '"
        else:
            expression = " '" + zone_f + ";a24=" + '"' + zone_p + '"' + " '"

        dmc.extra('_t1tr', out_o + 'tr', expression=expression)
        dmc.copy('_t1pt', out_o + 'pt')
        dmc.delete(in_i='_t1tr')
        dmc.delete(in_i='_t1pt')

def display_ellipsoids(in_i="required", out_o="required",
                       x_f='XPT', y_f='YPT', z_f='ZPT', trdipdir_f='TRDIPDIR', trdip_d='TRDIP', plunge_f="optional",
                       sdist1_p=100., sdist2_p=50., sdist3_p=25.,
                       num_ellipsoids_p=10, plunge_p=-90, invert_range_p=[90, 270]):
    try:
        assert  in_i != "required", "in_i is required"
        assert out_o != "required", "out_i is required"
        df = io.read_datamine(in_i + ".dm")
        choice = np.random.choice(df.index, num_ellipsoids_p)
        df_choice = df.loc[choice, :].copy().reset_index(drop=True)
        dm = dmcommands.init()

        if plunge_f == "optional":
            df['_PLUNGE'] = plunge_p
            plunge_f = '_PLUNGE'

        for i in range(len(df_choice)):

            plunge = df_choice.loc[i, plunge_f]

            if df_choice.loc[i, trdipdir_f] > invert_range_p[1] or df_choice.loc[i, trdipdir_f] < invert_range_p[0]:
                plunge *= -1

            dm.ellipse(
                wiretr_o='_1tr',
                wirept_o='_1pt',
                sangle1_p=df_choice.loc[i, trdipdir_f],
                sangle2_p=df_choice.loc[i, trdip_d],
                sangle3_p=plunge,
                saxis1_p=3,
                saxis2_p=1,
                saxis3_p=3,
                sdist1_p=sdist1_p,
                sdist2_p=sdist2_p,
                sdist3_p=sdist3_p,
                xcentre_p=df_choice.loc[i, x_f],
                ycentre_p=df_choice.loc[i, y_f],
                zcentre_p=df_choice.loc[i, z_f])

            if i == 0:
                dm.copy('_1tr', '_2tr')
                dm.copy('_1pt', '_2pt')
            else:
                dm.addtri(
                    wiretr1_i='_1tr',
                    wirept1_i='_1pt',
                    wiretr2_i='_2tr',
                    wirept2_i='_2pt',
                    wiretrou_o='_3tr',
                    wireptou_o='_3pt')
                dm.copy('_3tr', '_2tr')
                dm.copy('_3pt', '_2pt')
        dm.copy('_2tr', out_o=out_o + "tr")
        dm.copy('_2pt', out_o=out_o + "pt")

        dm.delete('_1tr')
        dm.delete('_1pt')
        dm.delete('_2tr')
        dm.delete('_2pt')
        dm.delete('_3tr')
        dm.delete('_3pt')

    except:
        print("Display ellipsoids is only available to SLR employees as it requires a propietary module")
