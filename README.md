This is a quick hack to support keyboard navigation for remarkable 2 for page flips. I might add more functionality like file or folder navigation later. This is just to show a proof of concept.

To use it, you need to have python installed on Remarkable 2, then just run "Python main.py". When it's running you can use left or right arrow key to flip pages. Or you can use 'j' or 'k' key to flip pages.

Press Esc to return to document list


I need to write some detailed user instructions:

# Installation

1. ssh root@10.11.99.1 (Your RM2)

2. install opkg: wget https://bin.entware.net/armv7sf-k2.6/installer/generic.sh and sh generic.sh, this will install opkg package manager under /opt/

3. here is a tricky part, since RM2 has limited space at /, I had to move /opt/ to ~/opt/ and use 'ln' to link the two folder (ln -s ~/opt /opt)

4. install python by 'opkg install python3'

5. After python installation, you can now run my code using 'python main.py' (need to by python 3.11 or above)
