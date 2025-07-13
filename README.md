# 🦑 The X-Ray Categorization Challenge: A Game of Precision (Windows Edition)

## Welcome, Player. Your Mission, Should You Choose to Accept It.

In this game, precision is paramount. You are tasked with categorizing X-Ray images, a critical mission that demands your full attention and accuracy. Fail, and the consequences... well, let's just say they're not pleasant. Succeed, and you contribute to a vital medical endeavor. Are you ready to play?

## The Tools of the Trade: Installation Protocol

Before you begin, ensure your environment is prepared. These are the essential components for your survival in this categorization challenge.

### Python Dependencies: The Green Light

To ensure the smooth operation of your categorization tool, you must install the necessary Python libraries. Open your Command Prompt (CMD) or PowerShell and execute the following commands. Consider this your first test of obedience.

```cmd
REM Install Python (if not already installed) from python.org or Microsoft Store
REM Ensure 'Add Python to PATH' is checked during installation.

pip install Pillow requests
```

*   **Python and Tkinter**: Tkinter is usually included with standard Python installations. If you encounter issues, ensure you have a full Python installation (not just `python.exe`). You can download Python from [python.org](https://www.python.org/downloads/windows/).
*   `Pillow`: This library handles image processing, allowing you to view and manipulate the X-Ray images. It's your window into the challenge.
*   `requests`: This library is crucial for downloading the image batches from the GitHub repository. It's your lifeline to the game's resources.

## The Arena Setup: Preparing Your Battlefield

Every game requires a meticulously prepared arena. Follow these steps precisely to set up your working environment. Deviate, and face elimination.

### Step 1: The Initial Enclosure

Create a new folder on your machine. Name it `Image Segregator`. This will be your primary operational base.

```cmd
md "Image Segregator"
```

### Step 2: The Inner Sanctums

Within your `Image Segregator` folder, create two sub-folders: `image_folder` and `Categorized_XRays`. These are your staging and archiving zones.

```cmd
cd "Image Segregator"
md image_folder Categorized_XRays
```

### Step 3: The Command Center

Open the `Image Segregator` folder in your VS Code environment. This is where you will execute your commands and monitor your progress.

### Step 4: The Data Retrieval Mechanism

Inside the `Image Segregator` folder, create a new file named `download.py`.

```cmd
type nul > download.py
```

### Step 5: The Source of Truth

Navigate to the GitHub repository within our organization. Locate the `Image-Segregator-App` repository. This is where the game's instructions and resources reside.

### Step 6: The Blueprint Transfer

From the `Image-Segregator-App` repository, open the `download.py` file. Copy its entire code content and paste it into your newly created `download.py` file in VS Code.

### Step 7: The Batch Assignment: Your Unique Challenge

In your `download.py` file, you will find a line similar to this:

```python
api_url = "https://api.github.com/repos/Neural-Network-Research-Paper/Image-Batches/contents/batch1"
```

Observe the `batch1` at the end of the URL. Replace this with the specific batch number assigned to you. This is your unique challenge, your designated trial.

### Step 8: The Data Influx

Execute the `download.py` script. This will initiate the download of your assigned X-Ray image batch.

```cmd
python download.py
```

### Step 9: The Verification Protocol

After the script completes, check your `image_folder`. Verify that your new images have been successfully downloaded. This is your first checkpoint.

### Step 10: The Main Event Blueprint

Now, within your `Image Segregator` folder, create a new file named `Main.py`.

```cmd
type nul > Main.py
```

### Step 11: The Core Program Transfer

From the GitHub repository, copy the code from the `Main.py` file and paste it into your `Main.py` file in VS Code. This is the heart of your categorization tool.

### Step 12: The Game Commences

Run the `Main.py` script. The application window will appear, marking the official start of your challenge.

```cmd
python Main.py
```

### Step 13: The Categorization Trial

Within the application, you will see each X-Ray image displayed, accompanied by buttons representing different categories. Your task is to accurately categorize each image by clicking the correct button. Choose wisely, for your fate depends on it.

### Step 14: The Victor's Acknowledgment

Once all images have been categorized, an achievement message will appear, signifying your successful completion of this round. You may now close the application.

### Step 15: The Next Round: A Continuous Challenge

To embark on a new batch, return to Step 7. Modify the `api_url` in `download.py` with the next batch number you wish to categorize. The game never truly ends.

### Step 16: The Relentless Pursuit

After downloading the new batch, run your `Main.py` application again and continue the process of segregation. The challenge awaits, always.


