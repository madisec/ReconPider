# ReconPider

An automation Python tool for subdomain enumeration and other features. ( For university presentation )

## Install

```bash
git clone https://github.com/madisec/ReconPider.git
cd ReconPider
chmod +x setup.sh
./setup.sh
python3 reconpider.py -h
```

---

### You can add to bashrc or zshrc.

```
ReconPider(main)$ python3 reconpider.py -h 
usage: reconpider

An automation python tool for subdoamin enumeration and other features. ( For university presentation )

options:
  -h, --help  show this help message and exit
  -d DOMAIN   Doamin for finding all subdomains
  -i INPUT    Input for utilize other feature's
  -s          Search ASN for finding CIDR
  -c CIDR     convert CIDR to IP
  -w          make a wordlist
  -o OUTPUT   Save result to file
  -S          Show minimal result
  -V          Show version of program
```
