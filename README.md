# Vitrix Engine
A port of Ursina Engine especially designed for [Vitrix](https://github.com/ShadityZ/Vitrix)!

## Getting Started
1) Install Python 3.6 or newer. https://www.python.org/downloads/
2) Open cmd/terminal and type:

```
<<<<<<< HEAD
pip install git+https://github.com/ShadityZ/Vitrix-Engine.git
=======
pip install git+https://github.com/pokepetter/vitrix_engine.git
>>>>>>> 9219278 (Big engine stuff)
```


If you want to easily edit the source, it's recommended to clone the git
repo and install as develop like this. Make sure you have git installed. https://git-scm.com/

```
<<<<<<< HEAD
git clone https://github.com/ShadityZ/Vitrix-Engine.git
=======
git clone https://github.com/pokepetter/vitrix_engine.git
>>>>>>> 9219278 (Big engine stuff)
python setup.py develop
```


**NOTE:** On some systems you might have to use pip3 instead of pip in order to use Python 3 and not the old Python 2.


## Dependencies
  * python 3.6+
  * panda3d
  * screeninfo:   for detecting screen resolution
  * pillow:       for texture manipulation
  * psd-tools:    for converting .psd files
  * blender:      for converting .blend files
  * pyperclip:    for copy/pasting


## Project Structure
```
## Project Structure
📁samples               # small example games.

📁vitrix_engine                # the actual vitrix_engine module.
    📁audio                 # built-in audio clips.
    📁editor                # the 3d level editor for vitrix_engine.
    📁fonts                 # built-in fonts.
    📁models                # .blend files, source files, for built-in 3d models.
        📁procedural            # classes for generating 3d models, like Cylinder, Quad and Terrain.
    📁models_compressed     # .blend files converted to .vitrix_enginemesh.
    📁prefabs               # higher level classes like Draggable, Slider, Sprite, etc.

    📃__init__.py
    📃application.py
    📃audio.py
    ...
        # vitrix_engine base modules, like code for Entity, input_handler, Text, window and so on.

```
