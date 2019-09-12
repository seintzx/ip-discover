# discover

Tool for IP/Domain Information discovery

# Installation

`pip install -r requirements.txt`

You will also need [machinae](https://github.com/HurricaneLabs/machinae)
installed and in the path so add `export
PATH="${HOME}/.local/bin/machinae:${PATH}"` to your `bashrc` or `zshrc` or
whatever

# Usage

For now you can only set one IP/domain at the time

```
usage: discover.py [-h] [-m] IP

IP/Domain information discovery tool

positional arguments:
  IP              IP address to lookup

optional arguments:
  -h, --help      show this help message and exit
  -m, --machinae  Also use machinae
```
