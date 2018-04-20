dmstudio
========

Python module for Datamine scripting. Versions supported are:

* Datamine Studio version 3
* Datamine Studio version RM
* Datamine Studio version EM

The module is made up of the following packages:

* ``commands`` a complete set of of Studio commands as they appear in the StudioRM.chm help file.
* ``special`` some special functions which are adaptations of Studio commands (coming soon)
* ``superprocess`` special function that involve a string a Studio commands
* ``file`` a package specifically for reading and writing the .dm file format and in the future possible other formats

License
-------

Copyright (c) 2018 Sean D. Horan

See LICENSE.txt for MIT <https://github.com/seanhoran/dmstudio/blob/master/LICENSE.txt> license.

Datamine Commands
-----------------

An exhaustive set of Datamine Studio command is available in the dmstudio.dmcommands package. The variables consist of four parts:

* Input files
* Output files 
* Fields
* Parameters

The python input variables are identical to the variable names used by Datamine with the following exceptions:

* All variables are lowercase
* Variables which are used bu datamine bit are reserved variables in python have a trailing underscore, e.g. in=in_, print=print_
* Multiple field selection is entered as a list instead of multiple variables for some commands e.g f1, f2, f3 => fields=[f1, f2, f3]

Usage
-----

    >>> import dmstudio.dmcommands as dmc
    >>> dm = dmc.studio(version='StudioRM')
    >>> dm.copy(in_='fake_model', out='fake_model_copy', retrieval='AU>2.0')
