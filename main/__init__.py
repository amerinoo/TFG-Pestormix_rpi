# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import traceback
import optparse
import time
import datetime
import socket

from main.json_parser import JsonParser

__author__ = 'Albert'


def setup():
    global sock, options
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 1110  # Reserve a port for your service.
    sock.bind((host, port))  # Bind to the port
    sock.listen(1)


def mainloop():
    global sock, options
    print "Start loop"
    try:
        while True:
            conn, addr = sock.accept()
            json_message = conn.recv(512)[2:]  # Removed init trash
            json_parser = JsonParser(json_message)
            json_parser.parse()
    finally:
        sock.close()


def main():
    global options, args
    setup()
    mainloop()


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()["__doc__"])
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_option('-p', '--port', action='store', default=1110, help='Listening port, default 1110')
        (options, args) = parser.parse_args()
        if len(args) > 0:
            parser.error('bad args, use --help for help')

        if options.verbose:
            print time.asctime()

        main()

        now_time = time.time()
        if options.verbose:
            print time.asctime()
        if options.verbose:
            print 'TOTAL TIME:', (now_time - start_time), "(seconds)"
        if options.verbose:
            print '          :', datetime.timedelta(seconds=(now_time - start_time))
        sys.exit(0)
    except KeyboardInterrupt, e:  # Ctrl-C
        raise e
    except SystemExit, e:  # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
