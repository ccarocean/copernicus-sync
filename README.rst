copernicus-sync
===============

Sync Copernicus (formally AVISO) SSH data.

Requirements
------------

* Python 3.7+
* python-dateutil


Usage
-----

```
usage: copsync [-h] [--user USER] [--password PASSWORD] [--dest DEST]
               [--verbose] [--delay N]
               {nrt,dt}

Sync Copernicus data.

positional arguments:
  {nrt,dt}              dataset to sync, nrt (near realtime) or dt (delayed
                        time)

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER  copernicus username
  --password PASSWORD, -p PASSWORD
                        copernicus password
  --dest DEST, -d DEST  destination directory
  --verbose, -v         increase verbosity, can be repeated twice
  --delay N             wait N seconds between files

```


