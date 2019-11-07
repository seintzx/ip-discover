# discover

Tool for IP/Domain Information discovery

# Installation

`pip install -r requirements.txt`

You will also need [machinae](https://github.com/HurricaneLabs/machinae)
installed and in the path so add
```
export PATH="${HOME}/.local/bin/machinae:${PATH}"
```
to your `bashrc` or `zshrc` or whatever

## Configuration file

Edit the `config.txt` with your API key
```
[configuration]
API = [virus total api key]
```

# Usage

```
usage: discover.py [-h] (-a HASH | -i IP) [-m]

IP/Domain information discovery tool

optional arguments:
  -h, --help            show this help message and exit
  -a HASH, --hash HASH  search hash on virustotal
  -i IP, --ip IP        IP address or domain to lookup
  -m, --machinae        also use machinae
```
