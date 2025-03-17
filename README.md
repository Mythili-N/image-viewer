# Image Viewer

A simple image viewer application using Tkinter and PIL (Pillow) that allows users to browse and view images from a selected folder.

## Features
- Allows users to select a folder containing images.
- Displays images while maintaining aspect ratio.
- Supports navigation through images using "Previous" and "Next" buttons.
- Resizes images dynamically when the window is resized.
- Exit button to close the application.

## Requirements
Ensure you have Python installed along with the required dependencies:

```bash
pip install pillow
```

## Usage
Run the script using:

```bash
python image_viewer.py
```

## File Structure
```
.
├── image_viewer.py  # Main script for image viewer
├── README.md        # Project documentation
```

## Functions Overview
- `load_images()`: Opens a file dialog to select an image folder.
- `show_image(index)`: Displays an image from the list while maintaining aspect ratio.
- `show_next_image()`: Navigates to the next image in the list.
- `show_previous_image()`: Navigates to the previous image.
- `on_resize(event)`: Resizes the displayed image dynamically.
