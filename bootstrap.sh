#!/bin/bash
pyenv install 3.10.4
pyenv virtualenv 3.10.4 frontmatter_switcher_3.10.4
"$(pyenv which pip)" install -U pip
"$(pyenv which pip)" install -r requirements.txt
