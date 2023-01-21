# RealCugan-Ncnn-Script-With-Python
This code is a script that allows the user to rescale an image using the Real-CUGAN ncnn Vulkan tool. The script provides a user interface for selecting the image and working directory, as well as choosing the scaling ratio and noise level treatment for the rescaled image.

First, make sure you have Python 3 installed on your computer. You can download it from the official website (https://www.python.org/downloads/).

Second, have the Real-CUGAN ncnn Vulkan installed, you can download it from the official repository on github (https://github.com/nihui/realcugan-ncnn-vulkan). 

Third, have the release builds version of ffmpeg, you can download it from (https://ffmpeg.org/download.html)

For the script, the paths for FFmpeg and Real-CUGAN are: C:\realcugan-ncnn-vulkan\realcugan-ncnn-vulkan.exe, C:\ffmpeg\bin\ffmpeg.exe

Next, download the script from GitHub. You can do this by clicking on the "Clone or download" button on the repository page and then selecting "Download ZIP".

Extract the files from the downloaded ZIP file and navigate to the folder where the script is located.

Open a command prompt window and navigate to the folder where the script is located.

Type the command "python main_global.py" and press enter to run the script.

The script will prompt you to select whether you want to rescale an image or video. Choose "I" for image or "V" for video.

If you choose image, the script will prompt you to select an image file, select the folder where you want to save the rescaled image, and select a scale ratio (2, 3, or 4) and noise treatment (-1, 0, 1, 2, 3).

If you choose video, the script will prompt you to select a video file, select the folder where you want to save the rescaled video, and select a scale ratio (2, 3, or 4).

The script will then process the file and create the rescaled image or video in the specified folder.

The script will then prompt you if you want to run it again or not.

It's important to note that the script requires a specific software called ffmpeg and real-cugan-ncnn-vulkan installed in your computer, and the script is set to work on Windows, if you are using another operative system you should make some changes on the script.
