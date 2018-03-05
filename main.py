#!/usr/bin/python3

import argparse
import code
import readline
import signal
import sys
import requests
from bs4 import BeautifulSoup

def SigHandler_SIGINT(signum, frame):
    print()
    sys.exit(0)

class Argparser(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--url", type=str, nargs="+", help="url to scrape")
        parser.add_argument("--dbg", action="store_true", help="debug", default=False)
        self.args = parser.parse_args()

def premain(argparser):
    signal.signal(signal.SIGINT, SigHandler_SIGINT)
    ###########################################################################
    data_file = open("data.csv", "w")
    for url in argparser.args.url:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        res = soup.select("script")
        tbody =  soup.select("td")
        for body in res:
            for string in body.stripped_strings:
                loco = string.split(",")
                for locotta in loco:
                    if locotta.startswith("PSGelStaMax"):
                        data_file.write(locotta[0:11])
                        data_file.write(",")
                        data_file.write(locotta[13:-1])
                        data_file.write("\n")
                    if locotta.startswith("PSGelStaMin"):
                        data_file.write(locotta[0:11])
                        data_file.write(",")
                        data_file.write(locotta[13:-1])
                        data_file.write("\n")
                    if locotta.startswith("MinWeek"):
                        data_file.write(locotta[0:7])
                        data_file.write(",")
                        data_file.write(locotta[9:-1])
                        data_file.write("\n")
                    if locotta.startswith("MaxWeek"):
                        data_file.write(locotta[0:7])
                        data_file.write(",")
                        data_file.write(locotta[9:-1])
                        data_file.write("\n")
                    if locotta.startswith("MinYear"):
                        data_file.write(locotta[0:7])
                        data_file.write(",")
                        data_file.write(locotta[9:-1])
                        data_file.write("\n")
                    if locotta.startswith("MaxYear"):
                        data_file.write(locotta[0:7])
                        data_file.write(",")
                        data_file.write(locotta[9:-1])
                        data_file.write("\n")
                    if locotta.startswith("EstimatedEPS"):
                        data_file.write(locotta[0:12])
                        data_file.write(",")
                        data_file.write(locotta[14:-1])
                        data_file.write("\n")
                    if locotta.startswith("SectorPE"):
                        data_file.write(locotta[0:8])
                        data_file.write(",")
                        data_file.write(locotta[10:-1])
                        data_file.write("\n")
                    if locotta.startswith("BaseVol"):
                        data_file.write(locotta[0:7])
                        data_file.write(",")
                        data_file.write(locotta[8:])
                        data_file.write("\n")
                    if locotta.startswith("ZTitad"):
                        data_file.write(locotta[0:6])
                        data_file.write(",")
                        data_file.write(locotta[7:])
                        data_file.write("\n")
                    if locotta.startswith("QTotTran5JAvg"):
                        data_file.write(locotta[0:13])
                        data_file.write(",")
                        data_file.write(locotta[15:-1])
                        data_file.write("\n")
                    if locotta.startswith("KAjCapValCpsIdx"):
                        data_file.write(locotta[0:15])
                        data_file.write(",")
                        data_file.write(locotta[17:-1])
                        data_file.write("\n")
                    if locotta.startswith("Title"):
                        data_file.write(locotta[0:5])
                        data_file.write(",")
                        data_file.write(locotta[7:-1])
                        data_file.write("\n")
    data_file.close()

def main():
    argparser = Argparser()
    if argparser.args.dbg:
        try:
            premain(argparser)
        except:
            variables = globals().copy()
            variables.update(locals())
            shell = code.InteractiveConsole(variables)
            shell.interact(banner="DEBUG REPL")
    else:
        premain(argparser)

if __name__ == "__main__":
    main()
