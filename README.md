# nudeScraper
Gather all pictures from different sites using a simple python code

# Requirements
Python3

**requests** and **urllib3**
```shell
pip install requests
pip install urllib3
```

# Usage

**FOR THE CODE TO WORK PROPERLY MAKE SURE lib.dat IS WITHIN THE SAME code.py DIRECTORY SINCE THE CODE CHECKS IF THE LIBRARY EXISTS OR NOT**

**Library names can be found within lib.dat**

```shell
python code.py [library_name] [inbound] [outbound]
```

# Examples

For gathering all pictures from all the libraries:
```shell
python code.py
```
For gathering all pictures from playboyplus.com library from folder 1 to 10:
```shell
python code.py playboyplus.com 1 10
```

For gathering all pictures from playboyplus.com library in folder 4:
```shell
python code.py playboyplus.com 4
```

# Changes

## 1.0.0
- First release
