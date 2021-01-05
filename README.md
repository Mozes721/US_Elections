# US_Elections

Web scrapping to get the US 2020 Election results convert it to `JSON file` then after `.csv` and ending it off graph it using in Jupyter Notebook for interactive computing(I did it with my VS code IDE in 
by installing an extention)

## Overview

The virtual env is sugjested for this project to contain needed libraries
have it installed prior
In your shell/terminal prompt:

	 $ pip install virtualenv

On macOS and Linux:

	 $ python3 -m venv env
   

On macOS and Linux:

	 $ virtualenv env
  
  
Install the `requirements.txt` Note the latest libraries do not have to be installed for it to run the script sucessfully.
 
 
You just have to install `state_code.csv` from the repo as other `.csv, .json` files will be created in `scrape_to_json.py` as state codes where not listed in scraped website 
`https://www.politico.com/2020-election/results/president/`

 
 # Jupyter Notebook
 
 The Jupyter notebook is a web-based notebook environment for interactive
computing.

## Installation
You can find the installation documentation for the
[Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html).
The documentation for advanced usage of Jupyter notebook can be found
[here](https://jupyter-notebook.readthedocs.io/en/latest/).

For a local installation, make sure you have
[pip installed](https://pip.readthedocs.io/en/stable/installing/) and run:

    $ pip install notebook

## Usage - Running Jupyter notebook

### Running in a local installation

Launch with:

    $ jupyter notebook

### Running in a remote installation

You need some configuration before starting Jupyter notebook remotely. See [Running a notebook server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html).
