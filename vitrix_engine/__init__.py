# do imports here so I can do a single line import
import sys
from pathlib import Path
from textwrap import dedent
import time
import random
from copy import copy, deepcopy
from math import floor, ceil, inf

from vitrix_engine.window import instance as window
from vitrix_engine.camera import instance as camera
from vitrix_engine.mouse import instance as mouse
from vitrix_engine.main import Ursina
from vitrix_engine.enginemath import *
from vitrix_engine.enginestuff import *
from vitrix_engine import input_handler
from vitrix_engine.input_handler import held_keys, Keys
from vitrix_engine.string_utilities import *
from vitrix_engine.mesh_importer import load_model, load_blender_scene
from vitrix_engine.texture import Texture
from vitrix_engine.texture_importer import load_texture
from vitrix_engine import color
from vitrix_engine.color import Color, hsv, rgb
from vitrix_engine.sequence import Sequence, Func, Wait
from vitrix_engine.entity import Entity
from vitrix_engine.collider import *
from vitrix_engine.raycaster import raycast, boxcast
from vitrix_engine.trigger import Trigger
from vitrix_engine.audio import Audio
from vitrix_engine.duplicate import duplicate
from panda3d.core import Quat
from vitrix_engine.vec2 import Vec2
from vitrix_engine.vec3 import Vec3
from vitrix_engine.vec4 import Vec4
from vitrix_engine.shader import Shader
from vitrix_engine.lights import *

from vitrix_engine.text import Text
from vitrix_engine.mesh import Mesh, MeshModes

from vitrix_engine.prefabs.sprite import Sprite
from vitrix_engine.prefabs.button import Button
from vitrix_engine.prefabs.panel import Panel
from vitrix_engine.prefabs.animation import Animation
from vitrix_engine.prefabs.frame_animation_3d import FrameAnimation3d
from vitrix_engine.prefabs.animator import Animator
from vitrix_engine.prefabs.sky import Sky
from vitrix_engine.prefabs.cursor import Cursor

from vitrix_engine.models.procedural.quad import Quad
from vitrix_engine.models.procedural.plane import Plane
from vitrix_engine.models.procedural.circle import Circle
from vitrix_engine.models.procedural.pipe import Pipe
from vitrix_engine.models.procedural.cone import Cone
from vitrix_engine.models.procedural.cube import Cube
from vitrix_engine.models.procedural.cylinder import Cylinder
from vitrix_engine.models.procedural.grid import Grid
from vitrix_engine.models.procedural.terrain import Terrain

from vitrix_engine.scripts.terraincast import terraincast
from vitrix_engine.scripts.smooth_follow import SmoothFollow
from vitrix_engine.scripts.position_limiter import PositionLimiter
from vitrix_engine.scripts.noclip_mode import NoclipMode, NoclipMode2d
from vitrix_engine.scripts.grid_layout import grid_layout
from vitrix_engine.scripts.scrollable import Scrollable
from vitrix_engine.scripts.colorize import get_world_normals

from vitrix_engine.prefabs.tooltip import Tooltip
from vitrix_engine.prefabs.text_field import TextField
from vitrix_engine.prefabs.input_field import InputField, ContentTypes
from vitrix_engine.prefabs.draggable import Draggable
from vitrix_engine.prefabs.slider import Slider, ThinSlider
from vitrix_engine.prefabs.button_group import ButtonGroup
from vitrix_engine.prefabs.window_panel import WindowPanel, Space
from vitrix_engine.prefabs.button_list import ButtonList
from vitrix_engine.prefabs.file_browser import FileBrowser
# from vitrix_engine.prefabs import primitives

from vitrix_engine.prefabs.debug_menu import DebugMenu
from vitrix_engine.prefabs.editor_camera import EditorCamera
from vitrix_engine.prefabs.hot_reloader import HotReloader
