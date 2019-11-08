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

Create the `config.txt` file or edit the existent one
```
[configuration]
API = [virus total api key]
```
Without square brackets

# Usage

```
usage: discover.py [-h] (-a HASH | -i IP) [-m]

IP/Domain discovery tool and Hash search on VirusTotal

optional arguments:
  -h, --help            show this help message and exit
  -a HASH, --hash HASH  search hash on virustotal
  -i IP, --ip IP        IP or domain to lookup
  -m, --machinae        also use machinae
```
