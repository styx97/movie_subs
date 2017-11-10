# movie_subs
**Download movie subtitles from subscene**

## Execution

### Linux
Make the python script executable by adding the shebang line, which is `#!` + `full/pathway/to/your/python/interpreter`. 
You can get it by typing `which python`

I use python from anaconda, so in my case , the shebang line is `#!/home/user_name/miniconda3/bin/python`


Lastly, put it in a directory on your PATH. 

`cd ~/bin/`  
`ln -s ~/some/path/to/myscript/arbitraryname`

More on PATH and making python files executable [here](https://stackoverflow.com/questions/15587877/run-a-python-script-in-terminal-without-the-python-command)

### Windows

Use the package pyinstaller to make it executable. If you have Python added to your PATH environment variable, you can use the pyinstaller module from Python package index. Then in command line, enter - 
                      
  `pip install pyinstaller`
 

  `pyinstaller movie_subs.py`
  
#### Python version

All code is written in Python3
