About
=====

Small exporter utility for Urban Airship. Currently it can export channels, iOS and Android devices. Exported fields are hardcoded in code but a next update should refactor it. The output files are in CSV format.

Requirements
============

Please see README.rst

Usage
=====

First, head to ``exporter/listwriterconfig.py`` and open it. Check the different fields that are configurable. In short:
* key: The key for the UA account you want to export
* secret: The secret for the UA account you want to export
* base_output_dir = The base output directory (defaults to ``export_files/``)
* file_channel = The file name for the channels list (defaults to ``devices_channel.csv``)
* file_ios = The file name for the iOS list (defaults to ``devices_ios.csv``)
* file_android = The file name for the Android list (defaults to ``devices_android.csv``)


In short, you can do the following:

    >>> sudo python setup.py install
    >>> python exporter/main.py

In summary ``main.py`` shows all that can be done with this fork. Modify it at your own will... as with the rest of the code.

