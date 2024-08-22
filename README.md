## Basic-Physics-Engine
This project is a basic physics engine built with Pygame that simulates the behavior of different shapes (circles, rectangles, and triangles) under gravity. The engine includes a simple GUI to add and remove shapes. It's still a work in progress, with some issues like circles drifting to the left.


# Features

Shape Simulation: Add circles, rectangles, and triangles to the environment.

Gravity: Objects are affected by gravity and will bounce when they hit the ground.

Collision Detection: Shapes collide with each other, though collision handling is basic.

Interactive GUI: Add or remove shapes using buttons.

# Known Issues

Drifting Circles: Circles tend to drift to the left.

Basic Collision Handling: Collision handling is not perfect, especially for non-circular shapes.

Limited Bounce Control: Rectangles and triangles have limited or no bouncing behavior.

# Installation

Clone the repository:

    git clone https://github.com/your-username/physics-engine.git
    cd physics-engine

# Install required packages:



    pip install pygame pygame_gui

# Run the program:


    python physics_engine.py

# Controls

Add Circle: Adds a circle to the environment.

Add Rectangle: Adds a rectangle to the environment.

Add Triangle: Adds a triangle to the environment.

Remove All: Removes all shapes from the environment.

# Future Improvements

Fix the issue with circles drifting to the left.

Improve collision detection and response for all shapes.

Add more shapes and interactive features.
