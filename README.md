# compiled-streamlit-custom-components

This project facilitates analysis of streamlit bidirectional custom components. 

There are two major components:
* `fetch.py` - a script to fetch wheels and unzip them into downloaded_package.
* `downloaded_package` - a directory containing wheels and assets. 

## Usage
```sh
# package name in kebab-case:
./fetch.py streamlit-options-menu
```
