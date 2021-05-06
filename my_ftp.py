import client, server
import sys

def checkIP(IP):
    try: 
        IP_Sliced = IP.split('.')
        if len(IP_Sliced)!=4 :
            return False
        else:
            for x in IP_Sliced:
                if int(x)>225:
                    return False
    except:
        return False
            
    return True

def main(args, PORT_NUM, BUFFER_SIZE = 4096):
    '''
    Usage for recieving file:
    python3 my_ftp.py recv
    Usage for sendind file:
    python3 my_ftp.py send [IP of reciever] [File address od the file to be sent.]
    Note:- For larger files please Increase the Buffer size. BY default it is always 4KiB = 4096 Bytes
    '''
    assert len(args) > 1
    if args[1].lower() == 'send':
        assert len(args) == 4 and checkIP(args[2])
        file_name = args[3]
        IP = args[2]
        cl = client.Client((IP, PORT_NUM),file_name,buffsize=BUFFER_SIZE)
        renspose = cl.send()
        print(renspose)
    elif args[1].lower() == 'recv':
        while True:
            file_name = input('Enter file name of the recived File:')
            if file_name == '': 
                print('Exiting Server!!')
                return
            sv = server.Server(address=(server.get_ip(), PORT_NUM), file_name=file_name ,buffsize=BUFFER_SIZE)
            sv.listen()
            sv.close()

if __name__ == "__main__":

    PORT_NUM = 6969# change according to need
    BUFFER_SIZE = 1024*1024*5 # change according to need: in BYTES
    main(sys.argv,PORT_NUM)