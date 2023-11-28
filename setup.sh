#!/bin/bash
echo "Setup ReconPider"
pip install -r requernment.txt
mkdir ~/.reconpider
mkdir ~/.reconpider/binfile
echo "Make directory for tool"
cp file/subfinder ~/.reconpider/binfile
cp reconpider.py ~/.reconpider
pip install -r requirement.txt