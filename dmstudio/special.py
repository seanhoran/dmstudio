'''
dmstudio.special
----------------

Python package with modified studio processes. The package is designed to make processes such as inpfil easier to use
and to facilitate more readable code.



'''

import dmfiles
import dmcommands
import pandas

# -----------------------------------------------------------------------------------#
# Special fields
#------------------------------------------------------------------------------------#
# certain fields are required to be 8 characters
CHAR8_FIELDS = ['VALUE_IN', 'VALUE_OU', 'NUMSAM_F', 'SVOL_F', 'VAR_F', 'MINDIS_F']

#  fields that are always implicit
IMPLICIT_FIELDS = ['XMORIG', 'YMORIG', 'ZMORIG', 'NX', 'NY', 'NZ']

#------------------------------------------------------------------------------------#

dmf = dmfiles.init()
dmc = dmcommands.init()

class dmfile_def(object):

    '''
    dmfile_def
    ----------

    Class for interactively creating a datamine file definition as a pandas dataframe. The file definition is to be
    used for an input for processes such as special.inpfil.

    Object Properties:
    ------------------

    dmfile_def.definition: pandas dataframe
        Dataframe to hold datamine file definition


    '''

    def __init__(self, definition=None):

        columns = ['Field Name', 'Field Type', 'Length', 'Keep', 'Default']

        if definition is None:
            self.definition = pd.DataFrame(columns=columns)
        else:
            for col in columns:
                if col not in definition.columns:
                    raise "Column "  + col + " not found in definition. Columns 'Field Name', 'Field Type', 'Length'," \
                                             " 'Keep', 'Default' are required"
            self.definition = definition


    def add_field(self, field_name, field_type, length='', keep='Y', default=''):

        data = {'Field Name': field_name, 'Field Type': field_type, 'Length': length, 'Keep': keep,
                'Default': default}

        dmtemp = pd.DataFrame(data)
        field_order = ['Field Name', 'Field Type', 'Length', 'Keep', 'Default']
        dmtemp = dmtemp[field_order]
        self.definition = self.definition.append(dmtemp).reset_index(drop=True)


def csv_to_dm(csv=None, out_o=None, definition=None):

    if definition is None:
        definition = csv_to_definition(csv)

    arguments = " 'csvfile' "
    for i in range(len(definition)):

        for char8 in char8_fields:
            if definition['Field Name'].iloc[i] == char8:
                definition['Field Type'].iloc[i] = 'A'
                definition['Length'].iloc[i] = 8

        for impf in implicit_fields:
            if definition['Field Name'].iloc[i] == impf:
                definition['Field Type'].iloc[i] = 'N'
                definition['Keep'].iloc[i] = 'N'
                definition['Default'].iloc[i] = df[impf].iloc[0]

        for column in definition.columns:
            arguments += " '" + (str(definition[column].iloc[i])).strip() + "' "

    arguments += "'!' 'Y' " + infile

    dmf.inpfil(out_o=out_o, arguments=arguments)

def csv_to_definition(csv):

    df = pd.DataFrame(csv)

    return pd_to_definition(df);

def pd_to_definition(df):

    field_names = []
    an = []
    length = []

    for column in df.columns:

        field_names.append(column)

        if df[column].dtype=='float64' or df[column].dtype=='int64':
            an.append('N')
            length.append('')
        else:
            an.append('A')
            if column in char8_fields:
                length.append(8)
            else:
                length.append(int((df[column].str.len().max()-1)/4+1)*4)

    definition = pd.DataFrame({'Field Name': field_names, 'Field Type': an, 'Length': length})
    definition['Keep']='Y'
    definition['Default']=''

    return definition;
    
    



