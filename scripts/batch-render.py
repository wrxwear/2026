# Blender Batch Render Script

"""
This script is designed to perform batch rendering in Blender.
Usage:
  - Place this script in the Blender scripts directory.
  - Call the script with a Python environment that has access to Blender.
"""

import bpy
import os

# Set your rendering settings
output_directory = "//render_output/"
file_extension = ".png"

# Check if the output directory exists, if not, create it
if not os.path.exists(bpy.path.abspath(output_directory)):
    os.makedirs(bpy.path.abspath(output_directory))

# Set the scene to render and file format
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Initialize rendering
for frame in range(1, bpy.context.scene.frame_end + 1):
    bpy.context.scene.frame_set(frame)
    bpy.context.scene.render.filepath = os.path.join(output_directory, f"render_{frame}{file_extension}")
    bpy.ops.render.render(write_still=True)
