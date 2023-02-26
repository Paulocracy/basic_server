# basic_server

*A basic configuration for a Flask Python server with JSON-based Socket.IO communication and TypeScript-derived JavaScript.*

## Installation

```
# 1st: Install node.js, e.g., from https://nodejs.org/
#      and add node.js to your system's PATH (you may select this option the
#      graphical installer)
# 2nd: Install and test TypeScript *as root/sudo/administrator* via:
npm install -g typescript
tsc
# 3rd: Install Anaconda or Miniconda via, e.g., https://www.anaconda.com/products/individual
# 4th: Install basic_server
git clone https://github.com/Paulocracy/basic_server
cd basic_server
conda env create -n basic_server -f environment.yml
conda activate basic_server
# 5th: Run basic_server with
python run.py
# Optional further test: Check if you can access
# the server from other devices in your local network.
# If this is not the case, you have to allow the basic_server
# conda enivronment's Python binary to go through your
# system's firewall for private networks. Make sure that
# your local network is marked as a private network.
```

## Future ideas

* HTTPS integration protocol?
