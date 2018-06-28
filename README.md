# PyRegedit

##### Table of Contents  

* [Description](#description)  
* [Supported operations](#operations)  
* [Test results](#testing)  
* [Installation](#install)  
* [Requirements](#requirements)  
* [FAQ](#faq) 
* [Screenshots](#screenshots)  
* [Resources & Links](#resources_links)  

<a name="description"/>

Description
=====================

Project for GUI editor of Windows Registry hives.
This project aim to allow users to access their data from Linux platform,
without using any Microsoft proprietary API.

<a name="screenshots"/>

Screenshots
==================
![alt Screenshot](screenshot.png)

<a name="operations"/>

Supported operations
=======================

* Show directory structure like tree view
* Show list of keys -> values foreach node
* Add new node to node tree
* Remove node from node tree
* Edit registry key value
* Add new registry key value
* Deleting single key

<a name="install"/>

Installation
===================

### Install package

* download debian package - pyregedit_1.0-1.deb
* install gdebi - `sudo apt-get update && sudo apt-get install gdebi`
* install package and dependencies `sudo gdebi pyregedit_1.0-1.deb`
* after install check manual `man pyregedit`
* run it - `pyregedit`

### Install from source

* clone content of this repository
* install dependencies - `sudo apt-get install python2.7 python-wxgtk2.8 python-hivex`
* run it by `python pyregedit.py`

<a name="requirements"/>

Requirements
================

* libhivex 1.3.6
* wxPython
* python 2.7

<a name="testing"/>

Testing
=================

There is results of various tests, that should cover basic operation. Purpouse
of this tests is prove that data is safely saved and Windows can read them correctly.


### Windows -> Linux

| Operation | Windows XP | Windows 7 Professional | Windows 8.1 |
| ------------- |:-----------:|:-------------:|:-----------:|
| Create 3 top keys by Regedit32 and read them by PyRegedit. | Yes | Yes | Yes | Yes |
| Create 3 subkeys by Regedit32 and read them by PyRegedit.	 | Yes | Yes | Yes | Yes |
| Create 2 new values in key  – REG_SZ, REG_DWORD and read them by PyRegedit. | Yes | Yes | Yes | Yes |
| Change 2 values by PyRegedit and read them by Regedit32. | Yes | Yes | Yes | Yes |
| Remove one key from hive by PyRegedit and check result in Regedit32 | Yes | Yes | Yes | Yes |

### Linux -> Windows

| Operation | Windows XP | Windows 7 Professional | Windows 8.1 |
| ------------- |:-----------:|:-------------:|:-----------:|
| Create 3 top keys by PyRegedit and read them by Regedit32. | Yes | Yes | Yes | Yes |
| Create 3 subkeys by PyRegedit and read them by Regedit32.	 | Yes | Yes | Yes | Yes |
| Create 2 new values in key  – REG_SZ, REG_DWORD and read them by Regedit32 | Yes | Yes | Yes | Yes |
| Change 2 values by Regedit32 and read them by PyRegedit | Yes | Yes | Yes | Yes |
| Remove one key from hive by Regedit32 and check result in PyRegedit | Yes | Yes | Yes | Yes |

<a name="faq">
FAQ
========

### Is changes directly saved to hive?

No. All changes which you made on current hive are not saved until you
manually saved it. Also, after first save is made a backup copy - which
should help, when something happened with original file.

### How is performed changes of hive?

About all low-end operations with hive is responsible library hivex,
this library is designed to change values directly in binary structure of
any hive.

### Is there any limitations?

Yes, this editor is only interface for communication with library hivex. If
hivex doesn't support any type of operation it's not possible to do that. For
more please see this - http://libguestfs.org/hivex.3.html

### Why I should use this and not hivex directly?

This editor should only make easier access to hive for users, which are not
so technical advanced to use hivex directly from command line or program their
own solution.

<a name="resources_links"/>

Resources & Links
===================

* http://gitweb.samba.org/?p=samba.git;a=tree;f=source/lib/registry;h=21934b5f658009ff0383f6aed41b102013b5b046;hb=v4-0-stable.
* http://sentinelchicken.com/research/registry_format/
* http://www.beginningtoseethelight.org/ntsecurity/index.php+
* http://libguestfs.org/hivex.3.html

Author
============
Martin Klíma <martin.klima@aol.com>
