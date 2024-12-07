# Thinkpad
## NOTE: THIS PROJECT WAS BUILT BY FOLLOWING A TUTORIAL AND I DID SOME MINOR SCALING CHANGES https://youtu.be/uf1IAjxmsD4?si=ahBd6NmpOmEzRZMN
#### Overview
This Python project is a simple text editor application built using the Tkinter library. The application allows users to create, open, and save text files with a graphical user interface (GUI). It is a lightweight tool designed for basic text editing, supporting operations such as opening existing text files and saving new files in `.txt` format.

## Click to watch video

[![Watch the video](https://cloud-11afp1k4r-hack-club-bot.vercel.app/0image.png)](https://cloud-a033jaby1-hack-club-bot.vercel.app/0screencast_from_2024-11-28_19-00-52.mp4)

#### Features:
- **Open File**: Allows users to browse and open existing `.txt` files.
- **Save File**: Users can save their text content into new or existing files with `.txt` extension.
- **Text Editing**: A large text area to input, edit, and view text.
- **Lightweight GUI**: A minimalistic design with only essential controls for easy navigation.

#### Requirements:
- **Python 3.x**: This project is developed using Python 3.x.
- **Tkinter Library**: Tkinter is used to build the graphical user interface for this text editor. It is a standard Python library and should be installed by default with most Python distributions.

#### Installation:
1. Ensure that Python 3.x is installed on your system.
2. Tkinter is bundled with Python, so no separate installation is required for the GUI features.
3. To run the script, simply download or copy the Python script to your local machine.

#### How to Use:
1. **Run the Application**: Execute the Python script in your environment.
   - This will open a Tkinter window with a simple text editor interface.
   
2. **Open a Text File**: Click the "Open" button in the top-left corner. This will prompt you to select a `.txt` file to open.
   
3. **Edit Text**: After opening the file, you can make changes in the large text area.
   
4. **Save a File**: Click the "Save" button. This will open a dialog to save the content to a `.txt` file. You can choose a location and provide a file name.

#### Code Breakdown:

1. **Tkinter Window Setup**:
   - The `Tk()` class initializes the root window, and the window is configured with a light blue background and fixed dimensions (600x600 pixels).

2. **Save File Function**:
   - The `savefile()` function is called when the "Save" button is clicked. It opens a file dialog to prompt the user to save the text content into a `.txt` file. It saves the text from the `Text` widget.

3. **Open File Function**:
   - The `openfile()` function is executed when the "Open" button is clicked. It allows users to open `.txt` files and load their content into the text area for editing.

4. **Widgets**:
   - The **Text widget** is used to display and allow text editing. It is set with a font of "Arial" and wraps text at word boundaries.
   - **Buttons** are created for "Save" and "Open" functionalities, with custom labels and positioning.

#### Customizations:
- You can modify the background color of the window by changing the `toor.config(background='lightblue')` line.
- Modify the window dimensions by changing the `toor.geometry('600x600')` values.

#### Example Usage:
- You can create a new `.txt` file by clicking "Save", entering some content, and saving it.
- To view or edit an existing file, click "Open" and select a `.txt` file from your computer.

#### License:
This project is open-source and free to use. No restrictions on usage or modification.
