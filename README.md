This is exploring variants of how to use importing (via importlib.)

Mostly for the sake of learning.

The problem faced is that an imported plugin (module) cannot reference the parent's context for importing its own things.

I want to be able to have a plugin import from ..utils, but instead we get an error that it tries to read from its parent.

Test both ways with:

    virtualenv -p python3 p3; source p3/bin/activate # if you so desire--alter args to suite
    pip3 install -r requirements.txt
    ./main.py plugs_ugly
    ./main.py plugs_b0rk
