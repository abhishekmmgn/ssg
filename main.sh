#!/bin/bash

# Create a conda env (site) for this project
# conda create -n site python=3.10.12
python3 src/main.py

# Start the web server after generating the site
python3 server.py