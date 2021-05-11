# Python_ftp
This is program works in a LAN. Sharing data through LAN. 
## Usage for recieving file:
python3 my_ftp.py recv
## Usage for sendind file:
python3 my_ftp.py send [IP of reciever] [File address od the file to be sent.]

Remarks:- 
- I have'nt applied multiprocessing  yet.  
- I have given a pretty rudimentary progress bar style.


Note:- For larger files please Increase the Buffer size. BY default it is always 4KiB = 4096 Bytes

