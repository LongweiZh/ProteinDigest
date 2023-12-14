# README

The project is a simple web-server application using TurboGears (Version: 2.4.3) to carry out an *in sillico* enzymatic digest of a user provided protein sequence.

## Requirements:

- Users should be able to specify min and max length, min and max molecular weight, # of missed cleavages, and specific enzyme.
- Output should be a table of peptides, with their length, molecular weight, # of missed cleavages, and amino acids to left and right of each peptide in the protein sequence.

## Installation and Setup

Install `ProteinDigest` using the setup.py script::

    $ cd ProteinDigest
    $ python setup.py develop

Create the project database for any model classes defined::

    $ gearbox setup-app

Start the paste http server::

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ gearbox serve --reload --debug

Then you are ready to go.

## Web Design

index.xhtml: handle the front page
master.xhtml: provide common degisn elements on every page
