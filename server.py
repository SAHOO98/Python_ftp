import socket as s
import time

def get_ip():
    sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
    try:
        sock.connect(('8.8.8.8', 80))
        IP = sock.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        sock.close()
    return IP

class Server:

  def __init__(self, address = (get_ip(), 6969),file_name = 'dumbass', buffsize=4096):
    assert type(address)==tuple and len(address) == 2 and type(address[0]) == str and type(address[1]) == int and address[1]<=65535 and address[1]>1000
    assert type(file_name) == str

    self.sock_conn = s.socket(s.AF_INET, s.SOCK_STREAM)
    self.address = address
    self.timer = 0
    self.file_name = file_name
    self.buffsize = buffsize
    self.sock_conn.bind(address)
    print(f'Server binded on{address}\n')
    
  
  def process_client(self, client_socket, addr):
    self.timer = time.time()
    print(f'Connection recieved from {addr}...')
    f = open(self.file_name, 'wb')
    raw_data = client_socket.recv(self.buffsize)
    size = 0
    while raw_data:
      size+=len(raw_data)
      f.write(raw_data)
      raw_data = client_socket.recv(self.buffsize)
    f.close()
    return f'Message Recived and stored in {self.file_name}\n'+f'Download done in {time.time() - self.timer} secs.\n'+f'Size of incoming file:{size} Bytes.\n'

  def listen(self):
    self.sock_conn.listen(5)
    try:
      clientSocket, addr = self.sock_conn.accept()
      response = self.process_client(clientSocket, addr)
      print(response)
    except KeyboardInterrupt :
      print('\nServer ended manually!\n')
      self.sock_conn.close()

  def close(self):
    print('Server is closing!')
    self.sock_conn.close()
      

if __name__ == "__main__":

  sv = Server()
  sv.listen()


    
