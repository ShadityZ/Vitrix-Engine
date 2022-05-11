# do imports here so I can do a single line import
import sys
from pathlib import Path
from textwrap import dedent
import time
import random
from copy import copy, deepcopy
from math import floor, ceil, inf

<<<<<<< HEAD
from ursina.window import instance as window
from ursina.camera import instance as camera
from ursina.mouse import instance as mouse
from ursina.main import Ursina
from ursina.ursinamath import *
from ursina.ursinastuff import *
from ursina import input_handler
from ursina.input_handler import held_keys, Keys
from ursina.string_utilities import *
from ursina.mesh_importer import load_model, load_blender_scene
from ursina.texture import Texture
from ursina.texture_importer import load_texture
from ursina import color
from ursina.color import Color, hsv, rgb
from ursina.sequence import Sequence, Func, Wait
from ursina.entity import Entity
from ursina.collider import *
from ursina.raycaster import raycast, boxcast
from ursina.trigger import Trigger
from ursina.audio import Audio
from ursina.duplicate import duplicate
from panda3d.core import Quat
from ursina.vec2 import Vec2
from ursina.vec3 import Vec3
from ursina.vec4 import Vec4
from ursina.shader import Shader
from ursina.lights import *

from ursina.text import Text
from ursina.mesh import Mesh, MeshModes

from ursina.prefabs.sprite import Sprite
from ursina.prefabs.button import Button
from ursina.prefabs.panel import Panel
from ursina.prefabs.animation import Animation
from ursina.prefabs.frame_animation_3d import FrameAnimation3d
from ursina.prefabs.animator import Animator
from ursina.prefabs.sky import Sky
from ursina.prefabs.cursor import Cursor

from ursina.models.procedural.quad import Quad
from ursina.models.procedural.plane import Plane
from ursina.models.procedural.circle import Circle
from ursina.models.procedural.pipe import Pipe
from ursina.models.procedural.cone import Cone
from ursina.models.procedural.cube import Cube
from ursina.models.procedural.cylinder import Cylinder
from ursina.models.procedural.grid import Grid
from ursina.models.procedural.terrain import Terrain

from ursina.scripts.terraincast import terraincast
from ursina.scripts.smooth_follow import SmoothFollow
from ursina.scripts.position_limiter import PositionLimiter
from ursina.scripts.noclip_mode import NoclipMode, NoclipMode2d
from ursina.scripts.grid_layout import grid_layout
from ursina.scripts.scrollable import Scrollable
from ursina.scripts.colorize import get_world_normals

from ursina.prefabs.tooltip import Tooltip
from ursina.prefabs.text_field import TextField
from ursina.prefabs.input_field import InputField, ContentTypes
from ursina.prefabs.draggable import Draggable
from ursina.prefabs.slider import Slider, ThinSlider
from ursina.prefabs.button_group import ButtonGroup
from ursina.prefabs.window_panel import WindowPanel, Space
from ursina.prefabs.button_list import ButtonList
from ursina.prefabs.file_browser import FileBrowser
# from ursina.prefabs import primitives

from ursina.prefabs.debug_menu import DebugMenu
from ursina.prefabs.editor_camera import EditorCamera
from ursina.prefabs.hot_reloader import HotReloader
=======
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
>>>>>>> 9219278 (Big engine stuff)
