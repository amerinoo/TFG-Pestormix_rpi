# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import optparse
import os
import socket
import sys
import time
import traceback

from json_parser import JsonParser

__author__ = 'Albert'


def setup():
    global sock, options
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 1110  # Reserve a port for your service.
    sock.bind((host, port))  # Bind to the port
    sock.listen(1)


def main_loop():
    global sock, options
    print "Start loop"
    try:
        while True:
            conn, addr = sock.accept()
            json_message = conn.recv(512)[2:]  # Removed init trash
            print json_message
            json_parser = JsonParser(json_message)
            json_parser.parse()
    finally:
        sock.close()


def main_loop_mock():
    json_message = "{\"glass\":\"Glass 0\"," \
                   "\"v0\":{\"use\":true,\"name\":\"Coca Cola\",\"alcohol\":true}," \
                   "\"v1\":{\"use\":true,\"name\":\"Coca Cola\",\"alcohol\":true}," \
                   "\"v2\":{\"use\":true,\"name\":\"Lemonade\",\"alcohol\":true}," \
                   "\"v3\":{\"use\":true,\"name\":\"Orangeade\",\"alcohol\":false}}"
    json_parser = JsonParser(json_message)
    cocktail = json_parser.parse()
    cocktail.serve()


def main_mock():
    global options, args
    main_loop_mock()


def main():
    global options, args
    setup()
    main_loop()


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

        main_mock()

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
