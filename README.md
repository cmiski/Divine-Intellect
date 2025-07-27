# Divine-Intellect

This is python script which runs a pre-specified video everytime you boot-up / start your system. (You can customize it accordingly)

Things you need to do regardless:

First you need to change the the 'video_path' and the 'vlc_path' (or use any other media player of your choice but put he path of that media player's .exe in this variable) in the script accordingly. 

Then,

  For the script/.exe to run you need to (assuming you are on windows os):
    1) press "Win + r"
    2) type "shell:startup"
  this will open the startup folder easily,
  then drop the .exe shortcut from the ./dist to the startup folder.


note: you can change the icon of the executable file if u want but need to rebuild the exe using pyinstaller.
