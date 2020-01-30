# ML-dash
A dashborad for visualizing and predicting data.

## Requirements
Requires python > 3.4 < 3.7.4 and pip >= 19.0

```bash
python3 --version
pip3 --version
virtualenv --version
```

## Installation
This dashboard run python. It's taken that you already have python installed on your system.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements
It's recommended to use virtual environment to use this project

```bash
sudo apt update
sudo apt install python3-dev python3-pip
sudo pip3 install -U virtualenv  # system-wide install
```

```bash
virtualenv --system-site-packages -p python3 ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```
