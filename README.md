# Content of the CRDS server for TMT/IRIS

Checkout this repository locally:

    git clone https://github.com/oirlab/tmt-crds-cache

The largest files are not on Github, get them from Galactica at:

    /home/azonca/crds_cache/references/tmt/iris

and copy them to the `crds_cache/references/tmt/iris` folder.
Alternatively use Git LFS, see below.
    
Configure CRDS to use this folder and the TMT configuration file:

```
export CRDS_PATH="/ABSOLUTE/PATH/TO/tmt-crds-cache"
export CRDS_CONTEXT="tmt_0001.pmap"
export CRDS_SERVER_URL="https://crds-serverless-mode.stsci.edu"
```

Make sure you are using the CRDS customized for TMT from <https://github.com/oirlab/tmt-crds>

## Development

This repository uses [Git LFS](https ://git-lfs.github.com/) to store the FITS reference files.
You need to install the `git-lfs` client and then clone the repository normally to download
the FITS files.

