'''
Future addition:
For reading and writing datamine files, converting between files etc...
'''


import numpy as np
import pandas as pd
import struct
import os
import initialize

# constant to avoid redundant COM connections which slow down processing
OSCRIPTCON = None

class init(object):

    def __init__(self, version=None):

        '''
        commands.__init__
        ------------------


        Commands initialization. After the commands class is initialized  for the first time the object will
         be set to the datamine studio object. This property will avoid redundant initializaiton

        Parameters:
        -----------

        version: str
            optional datamine studio versions ('Studio3', 'StudioRM', 'StudioEM') If no version given, the initializtion
            will try different versions starting with StudioRM then Studio3 and finally StudioEM.

        '''
        self.oScript = OSCRIPTCON
        self.version = version
        if self.oScript is None:
            self.oScript = initialize.studio(self.version)

    def run_command(self, command):
        '''
        run_command
        -----------

        Uses the studio Parsecommand method to execute a datamine script.

        Parameters:
        -----------

        command: str
            datamine command string to be parsed
        '''

        try:
            self.oScript.Parsecommand(command)
        except:
            print("Unexpected error:")

    def parse_infields_list(self, prefix, fields):
        '''
        parse_infields_list
        -------------------

        Intenal function for parsing a list of *fields to a string for use in studio commands e.g. *F1, *F2, etc..

        Parameters
        ----------

        prefix: str
            starting letter or letters for the field e.g. 'F' for *F1.
        fields: list of str
            list of input fields

        Returns:
        --------

        field_string: str
            concatenated string formated for input in datamine commands

        '''

        field_string = ""
        for i, field in enumerate(fields):
            field_string += " *" + prefix + str(i + 1) + "=" + field + " "

        return field_string;

    def comres(self,
               reserve_o='required',
               zone_f='optional',
               arguments='optional'):

        """
        COMRES
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        reserve: Undefined
            The output file generated, for use in subsequent scheduling processes, such as PRODSH. It will
            the following fields, in addition to all of the grade fields in the RESULTS file(s). UNIT A,8
            containing the name of each production unit. PNUM N Any blocks being scheduled may be
            according to a primary and secondary classification. The PNUM field contains the primary
            The values held in this field will depend on the type of primary classification selected. SNUM N
            classification number. The values held in this field will depend on the type of secondary
            selected. If ore/waste secondary classification is selected, it will contain values of 1 for
            ore units, and values of 2 for all waste units. NY N Implicit field, defining the total number of
            units in the file, equal to the number of records. PRATE N Notional production rate at which each
            unit is to be mined. This may contain absent data values, as individual production rates may be
            or changed during operation of PRODSH. TONNES N Reserve tonnage for each production unit.
            Required=Yes

        Fields:
        -------

        zone: Undefined : Undefined
            Optional numeric zone identifier field that has been used to define individual wireframe
            This field need only be defined if reserve classification by wireframe zone is required.
            Default=Undefined
            Required=No

        Parameters:
        -----------

        """

        command = "comres "

        # Required output error check

        if reserve_o == "required":
            raise ValueError("reserve_o is required.")

        command += " &reserve=" + reserve_o

        if zone != "optional":
            command += " *zone=" + zone_f

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def fdin(self,
             arguments='optional'):

        """
        FDIN
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------


        Fields:
        -------


        Parameters:
        -----------

        """

        command = "fdin "

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def fxin(self,
             out_o='required',
             arguments='optional'):

        """
        FXIN
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Undefined
            Output model file.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "fxin "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def inpddf(self,
               out_o='required',
               print_p=0,
               arguments='optional'):

        """
        INPDDF
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            Database file to be created. If OUT is a catalogue file, then all files in the catalogue will be

            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "inpddf "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def inpfil(self,
               out_o='required',
               print_p=0,
               arguments='optional'):

        """
        INPFIL
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "inpfil "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += " " + arguments + " "

        self.run_command(command)

    def inpfml(self,
               out_o='required',
               print_p=0,
               arguments='optional'):

        """
        INPFML
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        print:
            >=1 to display each record (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "inpfml "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def inputc(self,
               out_o='required',
               arguments='optional'):

        """
        INPUTC
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "inputc "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def inputd(self,
               out_o='required',
               arguments='optional'):

        """
        INPUTD
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            File to be created.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "inputd "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def link(self,
             out_o='required',
             arguments='optional'):

        """
        LINK
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Table
            Database file name.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "link "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def picdir(self,
               out_o='required',
               file_f='optional',
               append_p=0,
               print_p=0,
               sort_p=0,
               longname_p=0,
               arguments='optional'):

        """
        PICDIR
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Catalogue
            Output catalogue file, giving list of files.
            Required=Yes

        Fields:
        -------

        file: Character : OUT
            Optional name for the field that is to contain the file names. The default is "'FILENAM", i.e.
            will produce a catalogue file.
            Default=FILENAM
            Required=No

        Parameters:
        -----------

        append:
            If set to 1 then selected field names will be appended to the OUT file, provided it exists and has a
            DD (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        print:
            Option Description 0 No display of matching file names >0 Display file names as they are
            (0)
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        sort:
            If set to 1 then the output file will be sorted after all file names have been written to it (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        longname:
            If set to 1 then the fields LOGICAL (5A4) and SYSTEM (32A4) will be added to the output
            is the full, logical (long) name of the file.SYSTEM contains the full path name of the file.The
            for LONGNAME is (0).
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "picdir "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if file != "optional":
            command += " *file=" + file_f

        if append_p != "optional":
            command += " @append=" + str(append_p)

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if sort_p != "optional":
            command += " @sort=" + str(sort_p)

        if longname_p != "optional":
            command += " @longname=" + str(longname_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def protom(self,
               out_o='required',
               rotmod_p=0,
               arguments='optional'):

        """
        PROTOM
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Block Model Prototype
            Output prototype model.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        rotmod:
            Option Description 1 For rotated model.(0). No 0 0,1 0,1
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "protom "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if rotmod_p != "optional":
            command += " @rotmod=" + str(rotmod_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def protop(self,
               out_o='required',
               arguments='optional'):

        """
        PROTOP
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Plot Prototype
            Plot prototype file to be created.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "protop "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def quig(self,
             arguments='optional'):

        """
        QUIG
        ----
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------


        Fields:
        -------


        Parameters:
        -----------

        """

        command = "quig "

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def scrfmt(self,
               out_o='optional',
               text_f='optional',
               arguments='optional'):

        """
        SCRFMT
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Undefined
            Output database file.
            Required=No

        Fields:
        -------

        text: Character : OUT
            Optional name for the field that is to contain the formatted text. The default is "TEXT".
            Default=TEXT
            Required=No

        Parameters:
        -----------

        """

        command = "scrfmt "

        if out != "optional":
            command += " &out=" + out_o

        if text != "optional":
            command += " *text=" + text_f

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def secdef(self,
               out_o='required',
               arguments='optional'):

        """
        SECDEF
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: Undefined
            Output file of section definitions, containing the fields SVALUE, XCENTRE, YCENTRE,
            SDIP, SAZI, VAZI, VDIP, HSIZE, VSIZE, DPLUS, DMINUS, SCALE, TEXT, COUNT
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        """

        command = "secdef "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def sudttr(self,
               wiretr_o='required',
               wirept_o='required',
               sid_p=-1,
               arguments='optional'):

        """
        SUDTTR
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        wiretr: Wireframe Triangle
            Wireframe triangle data file with the fields TRI-NO,PT1,PT2,PT3.
            Required=Yes
        wirept: Wireframe Points
            Wireframe point data file with the fields PTN,XP,YP,ZP.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        sid:
            Surface identifier with a lower surface having the value -1, and a top surface the value +1 (-1).
            Range=-1,1
            Values=Undefined
            Default=-1
            Required=Yes
        """

        command = "sudttr "

        # Required output error check

        if wiretr_o == "required":
            raise ValueError("wiretr_o is required.")

        command += " &wiretr=" + wiretr_o

        # Required output error check

        if wirept_o == "required":
            raise ValueError("wirept_o is required.")

        command += " &wirept=" + wirept_o

        # Required parameter error check

        if sid_p == "required":
            raise ValueError("sid is required.")

        command += " @sid=" + str(sid_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def sustp2(self,
               arguments='optional'):

        """
        SUSTP2
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------


        Fields:
        -------


        Parameters:
        -----------

        """

        command = "sustp2 "

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def sustpe(self,
               out_o='required',
               direct_p=1,
               arguments='optional'):

        """
        SUSTPE
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------

        out: String
            Output perimeter file with the standard fields PVALUE,PTN,XP,YP,ZP.
            Required=Yes

        Fields:
        -------


        Parameters:
        -----------

        direct:
            Parameter to specify the plane of the STRing file: 1=XY, 2=XZ, 3=YZ.
            Range=1,3
            Values=1,2,3
            Default=1
            Required=Yes
        """

        command = "sustpe "

        # Required output error check

        if out_o == "required":
            raise ValueError("out_o is required.")

        command += " &out=" + out_o

        # Required parameter error check

        if direct_p == "required":
            raise ValueError("direct is required.")

        command += " @direct=" + str(direct_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def picted(self,
               arguments='optional'):

        """
        PICTED
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------


        Fields:
        -------


        Parameters:
        -----------

        """

        command = "picted "

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)

    def loadcf(self,
               print_p=0,
               level_p=0,
               encrypt_p=0,
               arguments='optional'):

        """
        LOADCF
        ------
        This is auto-generated documentation. For more command information visit the Datamine help file.

        Input Files:
        ------------


        Output Files:
        -------------


        Fields:
        -------


        Parameters:
        -----------

        print:
            Macro line display (0). =0 Do not display.=1 Display each line of the macro file as loaded.
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        level:
            Level of menu compilation . =0 Standard compilation. =1 'Optimise' for !SCREEN processing

            Range=0,1
            Values=0,1
            Default=0
            Required=No
        encrypt:
            Encryption level (0). =0 None. =1 Macro is encrypted
            Range=0,1
            Values=0,1
            Default=0
            Required=No
        """

        command = "loadcf "

        if print_p != "optional":
            command += " @print=" + str(print_p)

        if level_p != "optional":
            command += " @level=" + str(level_p)

        if encrypt_p != "optional":
            command += " @encrypt=" + str(encrypt_p)

        if arguments != "optional":
            command += "{" + arguments + "}"

        self.run_command(command)










