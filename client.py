import socket as s
import time
import os
import struct

class Client():
    def __init__(self, address, file_name, buffsize = 4096):
        assert type(address)==tuple and len(address) == 2 and type(address[0]) == str and type(address[1]) == int and address[1]<=65535 and address[1]>1000
        assert type(file_name) == str
        assert type(buffsize) == int

        self.sok_conn = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.sok_conn.connect(address)
        self.timer = time.time()
        self.file_name = file_name
        self.buffsize = buffsize

    def send(self):
        print(self.file_name)
        size = os.stat(self.file_name).st_size
        print(f"Size of the file to be sent(bytes) = {size}")
        size_counter = 0
        bin_size = struct.pack("!Q", size)
        with open(self.file_name, 'rb') as f:
            raw_data = bin_size

            while raw_data:
                self.sok_conn.send(raw_data)
                size_counter += len(raw_data)
                print(f'\r Percentage of file sent : {size_counter/(size+8)*100 :.2f}%', end = '\r')
                
                raw_data = f.read(self.buffsize)

        self.sok_conn.close()
        f.close()  
        return f'\n\nUpload done in {time.time()-self.timer} secs.\n'
        
if __name__ == "__main__":
    # client()
    file_name = "/home/septarmit/Downloads/Bob Coecke, Aleks Kissinger - Picturing Quantum Processes_ A First Course in Quantum Theory and Diagrammatic Reasoning-Cambridge University Press (2017).djvu"
    cl = Client(('192.168.1.9', 6969),file_name)
    print(cl.send())