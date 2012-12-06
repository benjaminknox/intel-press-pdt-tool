
import os, sys, logging, errno, select
import socket, optparse, json
from libs.Converter import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Main')
logger.setLevel(logging.DEBUG)
BACKLOG = 5
converter = Converter.Instance()

def pdf_conversion(message):
    ''' 
        Attempt to convert a pdf into a supplied format
    '''
    try:
        if message['out-format'] in converter.TYPES:
            converter.convert_file(message)
            logger.debug("Queued File!")
    except Exception:
        logger.error("Error attempting to convert pdf")
        raise


def parse_message(bytes):
    '''
        Example Message:
        {
            type : 'convert',
            in-format : 'pdf',
            out-format : 'epub',
            file-location : '/path/to/the/pdf.pdf',
            pdf-id : '1'
        }\n
    '''
    message = None
    try:
        #Attempt to load the json object
        message = json.loads(bytes)
        logger.error(message)
    except:
        #invalid json perhaps
        logger.error("Invalid message format")
    #If we loaded something
    if message != None:
        try:
            #confirm that we have the supported type
            if message['type'].lower() == "convert":
                #Attempt to run a conversion
                if message['in-format'].lower() == "pdf":
                    #Do PDF Conversion
                    pdf_conversion(message)    
        except:
            #Lazy validation that we have all of the keys
            logger.error("Message was missing nesicary components")

def serve_forever(host, port):
    # create, bind. listen
    lstsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # re-use the port
    lstsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # put listening socket into non-blocking mode
    lstsock.setblocking(0)

    lstsock.bind((host, port))
    lstsock.listen(BACKLOG)

    print 'Listening on port %d ...' % port

    # read, write, exception lists with sockets to poll
    rlist, wlist, elist = [lstsock], [], []

    while True:
        # block in select
        readables, writables, exceptions = select.select(rlist, wlist, elist)

        for sock in readables:
            if sock is lstsock: # new client connection, we can accept now
                try:
                    conn, client_address = lstsock.accept()
                    logger.debug("Connection from %s", client_address)
                except IOError as e:
                    code, msg = e.args
                    if code == errno.EINTR:
                        continue
                    else:
                        raise
                # add the new connection to the 'read' list to poll
                # in the next loop cycle
                rlist.append(conn)
            else:
                # read a line that tells us how many bytes to write
                bytes = sock.recv(1024)
                if not bytes: # connection closed by client
                    logger.debug("Connection closed by %s", client_address)
                    sock.close()
                    rlist.remove(sock)
                else:
                    parse_message(bytes)

def main():
    parser = optparse.OptionParser()
    parser.add_option(
        '-i', '--host', dest='host', default='0.0.0.0',
        help='Hostname or IP address. Default is 0.0.0.0'
        )

    parser.add_option(
        '-p', '--port', dest='port', type='int', default=2000,
        help='Port. Default is 2000')

    options, args = parser.parse_args()

    serve_forever(options.host, options.port)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.error("[!] User Shutdown!")