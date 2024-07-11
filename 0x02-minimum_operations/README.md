**Short Specializations** <br>

# 0x02. Minimum Operations

`Algorithm` `Python`

## General Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* Files first line exactly shebang `#!/usr/bin/python3`
* `README.md` file mandatory
* Code documented and using `PEP 8` style (version 1.7.x)
* Files must be executable

## For testing your algorithm

```python
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$

```
