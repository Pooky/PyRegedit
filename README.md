# PyRegedit

Project for GUI editor of Windows Registry hives.
This project aim to allow users to access their data from Linux platform,
without using any Microsoft proprietary API.

## Supported operations

* Show directory structure like tree view
* Show list of keys -> values foreach node
* Add new node to node tree
* Remove node from node tree
* Edit registry key value
* Add new registry key value
* Deleting single key

## Installation

### Install package

* download debian package - pyregedit_1.0-1.deb
* install it by `dpkg -i pyregedit_1.0-1.deb`
* after install run `pyregedit`

### Install from source

* clone content of this repository
* run it by `python pyregedit.py`

## Testing

| Operation | Windows XP | Windows 7 Professional | Windows 8.1 |
| ------------- |:-----------:|:-------------:|:-----------:|
| Create 3 top keys by Regedit32 and read them by PyRegedit. | Yes | Yes | Yes | Yes |
| Create 3 subkeys by Regedit32 and read them by PyRegedit.	 | Yes | Yes | Yes | Yes |
| Create 2 new values in key  – REG_SZ, REG_DWORD and read them by PyRegedit. | Yes | Yes | Yes | Yes |
| Change 2 values by PyRegedit and read them by Regedit32. | Yes | Yes | Yes | Yes |
| Remove one key from hive by PyRegedit and check result in Regedit32 | Yes | Yes | Yes | Yes |

## FAQ

### Is changes directly saved to hive?

No. All changes which you made on current hive are not saved until you
manually saved it. Also, after first save is made a backup copy - which
should help, when something happend with original file.

### How is performed changes of hive?

About all low-end operations with hive is responsible library hivex,
this library is designed to change values directly in binary structure of
any hive.

### Is there any limitations?

Yes, this editor is only interface for cumunication with library hivex. If
hivex doesn't support any type of operation it's not possible to do that. For
more please see this - http://libguestfs.org/hivex.3.html

### Why I should use this and not hivex directly?

This editor should only make esier access to hive for users, which are not
so technical advanced to use hivex directly from command line or program their
own solution.




## Requirements

* hivex 1.3.7
* wxPython
* python 2.7

## Screenshot
![alt Screenshot](screenshot.png)


## Resources & Links

* http://gitweb.samba.org/?p=samba.git;a=tree;f=source/lib/registry;h=21934b5f658009ff0383f6aed41b102013b5b046;hb=v4-0-stable.
* http://sentinelchicken.com/research/registry_format/
* http://www.beginningtoseethelight.org/ntsecurity/index.php+
* http://libguestfs.org/hivex.3.html
