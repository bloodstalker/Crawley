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

def dump1(locotta, key, data_file):
    data_file.write(locotta[0:len(key)])
    data_file.write(",")
    data_file.write(locotta[len(key)+2:-1])
    data_file.write("\n")

def dump11(locotta, key, data_file):
    data_file.write(locotta[len(key)+2:-1])
    data_file.write(",")

def dump111(locotta, key, data_file):
    return(locotta[len(key)+2:-1])

def dump2(locotta, key, data_file):
    data_file.write(locotta[0:len(key)])
    data_file.write(",")
    data_file.write(locotta[len(key)+1:])
    data_file.write("\n")

def dump22(locotta, key, data_file):
    data_file.write(locotta[len(key)+1:])
    data_file.write(",")

def dump222(locotta, key, data_file):
    return(locotta[len(key)+1:])

def csv_dump_page1(url, data_file):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    res = soup.select("script")

    tbody =  soup.select("td")
    print(soup)

    for body in res:
        for string in body.stripped_strings:
            loco = string.split(",")
            for locotta in loco:
                #print(locotta)
                if locotta.startswith("InstrumentID"):
                    dump1(locotta, "InstrumentID", data_file)
                if locotta.startswith("PSGelStaMax"):
                    dump1(locotta, "PSGelStaMax", data_file)
                if locotta.startswith("PSGelStaMin"):
                    dump1(locotta, "PSGelStaMin", data_file)
                if locotta.startswith("MinWeek"):
                    dump1(locotta, "MinWeek", data_file)
                if locotta.startswith("MaxWeek"):
                    dump1(locotta, "MaxWeek", data_file)
                if locotta.startswith("MinYear"):
                    dump1(locotta, "MinYear", data_file)
                if locotta.startswith("MaxYear"):
                    dump1(locotta, "MaxYear", data_file)
                if locotta.startswith("EstimatedEPS"):
                    dump1(locotta, "EstimatedEPS", data_file)
                if locotta.startswith("SectorPE"):
                    dump1(locotta, "SectorPE", data_file)
                if locotta.startswith("BaseVol"):
                    dump2(locotta, "BaseVol", data_file)
                if locotta.startswith("ZTitad"):
                    dump1(locotta, "ZTitad", data_file)
                if locotta.startswith("QTotTran5JAvg"):
                    dump1(locotta, "QTotTran5JAvg", data_file)
                if locotta.startswith("KAjCapValCpsIdx"):
                    dump1(locotta, "KAjCapValCpsIdx", data_file)
                if locotta.startswith("Title"):
                    dump1(locotta, "Title", data_file)
                if locotta.startswith("PdrCotValue"):
                    dump1(locotta, "PdrCotValue", data_file)
                if locotta.startswith("PClosing"):
                    dump1(locotta, "PClosing", data_file)
                if locotta.startswith("PriceMin"):
                    dump2(locotta, "PriceMin", data_file)
                if locotta.startswith("PriceMax"):
                    dump2(locotta, "PriceMax", data_file)
                #if locotta.startswith("PriceYesterday"):
                    #dump2(locotta, "PriceYesterday", data_file)

def csv_dump_page2(url, data_file):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    res = soup.select("script")

    data_file.write("InstrumentID,")
    data_file.write("PSGelStaMax,")
    data_file.write("PSGelStaMin,")
    data_file.write("MinWeek,")
    data_file.write("MaxWeek,")
    data_file.write("MinYear,")
    data_file.write("MaxYear,")
    data_file.write("EstimatedEPS,")
    data_file.write("SectorPE,")
    data_file.write("BaseVol,")
    data_file.write("ZTitad,")
    data_file.write("QTotTran5JAvg,")
    data_file.write("KAjCapValCpsIdx,")
    #data_file.write("Title,")
    data_file.write("PdrCotValue,")
    data_file.write("PClosing,")
    data_file.write("PriceMin,")
    data_file.write("PriceMax,")
    #data_file.write("PriceYesterday")
    data_file.write("\n")

    InstrumentID = str()
    PSGelStaMax = float()
    PSGelStaMin = float()
    MinWeek = str()
    MaxWeek = str()
    MinYear = str()
    MaxYear = str()
    EstimatedEPS = str()
    SectorPE = str()
    BaseVol = str()
    ZTitad = str()
    QTorTran5JAvg = str()
    KAjCapValCpsIdx = str()
    #Title = str()
    PdrCotValue = str()
    PClosing = str()
    PriceMin = str()
    PriceMax = str()

    tbody =  soup.select("td")
    #print(soup)

    for body in res:
        for string in body.stripped_strings:
            loco = string.split(",")
            for locotta in loco:
                #print(locotta)
                if locotta.startswith("InstrumentID"):
                    InstrumentID = dump111(locotta, "InstrumentID", data_file)
                if locotta.startswith("PSGelStaMax"):
                    PSGelStaMax = dump111(locotta, "PSGelStaMax", data_file)
                if locotta.startswith("PSGelStaMin"):
                    PSGelStaMin = dump111(locotta, "PSGelStaMin", data_file)
                if locotta.startswith("MinWeek"):
                    MinWeek = dump111(locotta, "MinWeek", data_file)
                if locotta.startswith("MaxWeek"):
                    MaxWeek = dump111(locotta, "MaxWeek", data_file)
                if locotta.startswith("MinYear"):
                    MinYear = dump111(locotta, "MinYear", data_file)
                if locotta.startswith("MaxYear"):
                    MaxYear = dump111(locotta, "MaxYear", data_file)
                if locotta.startswith("EstimatedEPS"):
                    EstimatedEPS = dump111(locotta, "EstimatedEPS", data_file)
                if locotta.startswith("SectorPE"):
                    SectorPE = dump111(locotta, "SectorPE", data_file)
                if locotta.startswith("BaseVol"):
                    BaseVol = dump222(locotta, "BaseVol", data_file)
                if locotta.startswith("ZTitad"):
                    ZTitad = dump111(locotta, "ZTitad", data_file)
                if locotta.startswith("QTotTran5JAvg"):
                    QTorTran5JAvg = dump111(locotta, "QTotTran5JAvg", data_file)
                if locotta.startswith("KAjCapValCpsIdx"):
                    KAjCapValCpsIdx = dump111(locotta, "KAjCapValCpsIdx", data_file)
                #if locotta.startswith("Title"):
                    #Title = dump111(locotta, "Title", data_file)
                if locotta.startswith("PdrCotValue"):
                    PdrCotValue = dump111(locotta, "PdrCotValue", data_file)
                if locotta.startswith("PClosing"):
                    PClosing = dump111(locotta, "PClosing", data_file)
                if locotta.startswith("PriceMin"):
                    PriceMin = dump222(locotta, "PriceMin", data_file)
                if locotta.startswith("PriceMax"):
                    PriceMax = dump222(locotta, "PriceMax", data_file)
                #if locotta.startswith("PriceYesterday"):
                    #dump222(locotta, "PriceYesterday", data_file)
    data_file.write(InstrumentID)
    data_file.write(",")
    data_file.write(PSGelStaMax)
    data_file.write(",")
    data_file.write(PSGelStaMin)
    data_file.write(",")
    data_file.write(MinWeek)
    data_file.write(",")
    data_file.write(MaxWeek)
    data_file.write(",")
    data_file.write(MinYear)
    data_file.write(",")
    data_file.write(MaxYear)
    data_file.write(",")
    data_file.write(EstimatedEPS)
    data_file.write(",")
    data_file.write(SectorPE)
    data_file.write(",")
    data_file.write(BaseVol)
    data_file.write(",")
    data_file.write(ZTitad)
    data_file.write(",")
    data_file.write(QTorTran5JAvg)
    data_file.write(",")
    data_file.write(KAjCapValCpsIdx)
    data_file.write(",")
    #data_file.write(repr(Title) + ",")
    #data_file.write(",")
    data_file.write(PdrCotValue)
    data_file.write(",")
    data_file.write(PClosing)
    data_file.write(",")
    data_file.write(PriceMin)
    data_file.write(",")
    data_file.write(PriceMax)
    data_file.write("\n")

def premain(argparser):
    signal.signal(signal.SIGINT, SigHandler_SIGINT)
    ###########################################################################
    data_file = open("data.csv", "w")
    for url in argparser.args.url:
        csv_dump_page2(url, data_file)
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
