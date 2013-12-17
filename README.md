cinnamon-rhythmbox-tray
=======================

Hide rhythmbox to systray when the quit button is clicked. Do not create systray icon, integrate nicely into cinnamon.

###Usage

First, clone the project to your local machine:
```
git clone https://github.com/paprykut/cinnamon-rhythmbox-tray.git
```

Create the rhythmbox plugins directory if it does not exist and move the project folder there:
```
mkdir -p ~/.local/share/rhythmbox/plugins
mv cinnamon-rhythmbox-tray ~/.local/share/rhythmbox/plugins
```

Start/restart rhythmbox, go into settings -> plugins and activate the Cinnamon Rhythmbox Tray entry. Now, when you close the program by clicking x in the top right corner, it will simply go into background. No additional, ugly icon is created on the system tray, so your theme is not messed up. Yet, rhythmbox can still be accessed by clicking the note icon (in the default theme).
