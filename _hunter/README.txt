##################################
#
# README
#
##################################

1.0 Requirements

Python 2.7 or 3.4 installed
Tested using Python 2.7.6 on Linux Mint 17.1 "Rebecca"

2.0 Usage

    1. Open up a command line window.
        - On Windows:
            1. Go into the start menu.
            2. Type "cmd" (without quotations) into the search menu.
            3. Press enter.
            4. Navigate to the directory where this script is stored.
        - On Mac
            1. Hit Ctrl + Space to bring up the search menu.
            2. Type "terminal" (again without quotations) into the search menu.
            3. Press return.
            4. Navigate to the directory where this script is stored.
        - On Linux
            1. Grab a beer. You have my respect.
            2. Open up terminal. Navigate to the directory where this script is stored.

    Type into the terminal:

        python hunter.py -f <csv file name> -t <directory where you have the works stored> -o <output file name (defaults to output.txt)> -d <Delimiter(separator) used in the csv file. Defaults to tab >

    Examples:
        python hunter.py -f test.csv -t literary_works -o results.txt    # Compares the values in file.csv with the directory literary_works. Any matches go to output.txt
        python hunter.py -f file.csv -t ../                              # Looks up a directory
        python hunter.py -f file.csv -t litarary_works -d ";"         # the -d option added will use semi-colons instead of tab characters to separate the cells in the csv.

        NOTE: For Windows, a directory separator is symbolized with \\ instead of /

3.0 CSV File
    While you can separate your csv file cells with commas, periods, spaces. It is recommended for this script that you use either tabs, semi-colons, or colons.
    By default, this script will use tabs as the cell separator character.

3.1 CSV file structure
    The csv file should be structured as such.
    | Column 1 | Column 2|
    | <author> | <work>  |

    If it is not structured this way, the script will break.

4.0 Boring stuff
    Copyright 2015 Mike Poirier, poirier.mike@live.com
    Written for Riley Vlooswyk, in assisting with his work studies project.




