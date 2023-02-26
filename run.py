"""
run.py

This file combines all necessary steps in order
to start the Python server with its associated
TypeScript static file.
"""
# We use os in oder to perform console commands
import os

# Transpile the TypeScript file to JavaScript
os.system("tsc ./static/script.ts")

# Now, with the corrected JavaScript file,
# start the server.
os.system("python ./basic_server.py")
