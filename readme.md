# A tool for renaming a batch of pdf files

> MIT license, Xavier Olive 2017

The addressed use case comes the frustration caused by opening tons of pdf files (mainly scientific publications) in order to copy-paste the title and rename the file accordingly.

The proposed workflow goes as follow:
```sh
$ pdfrename *.pdf
Rename '/home/xo/Downloads/1606.04838.pdf' to '/home/xo/Downloads/Optimization Methods for Large-Scale Machine Learning.pdf'? [y/n/j/s/a] > 
Choose among y(es)/n(o)/j(oin)/s(kip)/a(bort) > y
```

The script first searches the metadata, then parses each line of the first page of the file to suggest it as a file name.  
Use `j(oin)` to merge the current suggestion with next line (for papers with a two-line title).

## Installation

**Latest release**:
```sh
pip install pdfrename
```

Try `pip install --user pdfrename` if need be.  
The executable will be installed in a directory with read/write access.  
Check the directory (which depends on your Python installation) is in your `PATH` variable.  
Try `/usr/local/bin`, `$HOME/.local/bin`, ...

**From source:**
```sh
pip install git+https://github.com/xoolive/pdfrename
```

