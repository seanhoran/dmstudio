DMSTUDIO
========

Python package for Datamine Studio scripting. 

Originally created by Sean Horan, Principal Geologist/Geostatistician, RPA Consulting.

The package provides an easy to use interface between Python and Datamine Studio packages for the creation of concise, highly readable, and powerful Datamine scripts. The package is setup such that it should (hopefully) be intuitive for people familiar with Datamine commands and scripts but also offers a comparitevly easy entry for those looking to learn Datamine scripting.

The ``dmstudio`` package requires an active Datamine Studio project and therefore requires a valid Datamine license to be of any use. Visit the [Datamine Software](http://www.dataminesoftware.com) website for more information on products, licenses and downloads. Scripts created using the ``dmstudio`` package can be executed in a number of ways including the command line, IDEs such as [Pycharm](https://www.jetbrains.com/pycharm/), [Jupyter Notebook](http://jupyter.org/) and just about any way you can think of.

The python code was auto-generated from the ``StudioRM.chm`` help file located at: ``C:\Program Files\Datamine\StudioRM\Help\StudioRM.chm``. It is guaranteed that there will be a small amount of bugs in the code given that the help file is not 100% consistent. These bugs will be resolved in time and for now the code is provided **"AS IS"**. See the [MIT](https://github.com/seanhoran/dmstudio/blob/master/LICENSE.txt) license. Please log [issues](https://github.com/seanhoran/dmstudio/issues) in github or email [Sean Horan](mailto:sean.horan@rpacan.com).

For additional help on the actual Datamine Studio commands, consult the Datamine help file available by pressing F1 while in an active Studio project or locating the .chm file in the Datamine folder on your C drive.

Versions supported are:

* Datamine Studio version 3
* Datamine Studio version RM
* Datamine Studio version EM

The package is made up of the following modules:

* ``dmcommands`` a complete set of of Studio commands that require input files as they appear in the StudioRM.chm help file.
* ``dmfiles`` the remaining Studio commands that do not use input files and are mainly used for generating datamine files
* ``special`` some special functions which are adaptations of Studio commands (coming soon)
* ``superprocess`` special function that involve a string a Studio commands

License
-------

Copyright (c) 2018 Sean D. Horan

See LICENSE.txt for [MIT](https://github.com/seanhoran/dmstudio/blob/master/LICENSE.txt) license.

Datamine Commands
-----------------

An exhaustive set of Datamine Studio commands is available in the ``dmstudio.dmcommands`` and the ``dmstudio.dmfiles`` modules. The variables consist of four parts:

* Input files
* Output files 
* Fields
* Parameters

The python input variables are identical to the variable names used by Datamine with the following exceptions:

* All variables are lowercase
* Input files have the suffix "_i", output files have the suffix "_o", fields have the suffix "_f" and parameters have the suffix "_p".
* Multiple field selection is entered as a list instead of multiple variables for some commands e.g f1, f2, f3 => fields=[f1, f2, f3]

The ``dmstudio.dmfiles`` module is for commands such as ``INPFIL`` which requires an output file and a string of arguments. The purpose of the ``dmstudio.special`` module is to simplify the usage of some processes such as ``dmstudio.dmfiles.inpfil``. This module is currently a work in progress.

Default values are used when they were specified by the StudioRM.chm help file. In order to provide guidance as to required versus optional inputs, outputs fields and parameters, python variables without a default specified but which are required are given a default string ``"required"`` while those which are optional are given the default ``"optional"``. This particularly useful when using IDEs which have code completion.

Usage
-----

Using the ``dmstudio.dmcommands`` module:

    >>> from dmstudio import dmcommands
    >>> cmd = dmcommands.init(version='StudioRM')
    >>> cmd.copy(in_i='fake_model', out_o='fake_model_copy', retrieval='AU>2.0')
    
Using the ``dmstudio.dmfiles`` module:

    >>> from dmstudio import dmfiles
    >>> dmf = dmfiles.init(version='StudioRM')
    >>> arguments = "'XXXXXXXX'"
    >>> dmf.infile(out_o='points', arguments=arguments)

Initialization
--------------

The COM object is intialized using ``win32client`` package and is passed to a variable ``oScript`` which is consistent with traditional Datamine Studio javascripts or ``vbscript``. Each module is required to be initialized seperatly although in reality they are redundantly initializing the same COM object. There is only a minor impact on processing time which is noticeable only when running scripts on small data sets.

Installation
------------

For those starting out in python, the easiest option for windows is downloading [Anaconda](https://www.anaconda.com/download/) for python 3.7. This has all the basic packages that will be required.

A pip install version of dmstudio will be available shortly. For the time being a pre-release version is available on github.
