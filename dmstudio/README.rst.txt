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
~~~~~~~

Copyright (c) 2018 Sean D. Horan

See LICENSE.txt for `MIT <https://github.com/seanhoran/dmstudio/blob/master/LICENSE.txt> License


To use (with caution), simply do::

    >>> import funniest
    >>> print funniest.joke()