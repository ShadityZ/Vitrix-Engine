# Vitrix Engine
A port of Ursina Engine especially designed for [Vitrix](https://github.com/ShadityZ/Vitrix)!

## Getting Started
1) Install Python 3.6 or newer. https://www.python.org/downloads/
2) Open cmd/terminal and type:

```
pip install git+https://github.com/ShadityZ/Vitrix-Engine.git
```


If you want to easily edit the source, it's recommended to clone the git
repo and install as develop like this. Make sure you have git installed. https://git-scm.com/

```
git clone https://github.com/ShadityZ/Vitrix-Engine.git
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

📁ursina                # the actual ursina module.
    📁audio                 # built-in audio clips.
    📁editor                # the 3d level editor for ursina.
    📁fonts                 # built-in fonts.
    📁models                # .blend files, source files, for built-in 3d models.
        📁procedural            # classes for generating 3d models, like Cylinder, Quad and Terrain.
    📁models_compressed     # .blend files converted to .ursinamesh.
    📁prefabs               # higher level classes like Draggable, Slider, Sprite, etc.

    📃__init__.py
    📃application.py
    📃audio.py
    ...
        # ursina base modules, like code for Entity, input_handler, Text, window and so on.

```
