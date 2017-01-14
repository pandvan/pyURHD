#!/usr/bin/env python

""" DOCS
"""

import sys
import argparse
import re
import requests
import json
from bs4 import BeautifulSoup


DESCRIPTION = "Get stream links from www.urhd.tv"
URL = "http://www.urhd.tv"


def get_ch_list(url=URL):
    """ DOCS
    """

    rs = requests.Session()
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    channels_tag = soup.find_all("channels")
    result = []
    for tag in channels_tag:
        json_str = tag.attrs[":channels"]
        channel_list = json.loads(json_str)

        # add a channel number for each channel
        # this allow to load channel later
        #i = 0
        #for el in channel_list:
        #    i += 1
        #    el.update({"num": i})

        result.extend(channel_list)

    return result


def print_ch_list(ch_list):
    """ DOCS
    """

    for idx, ch in enumerate(ch_list, 1):
        if ch["alive"]:
            active = "ACTIVE"
        else:
            active = "INACTIVE !!!"

        display_name = ch["display_name"]
        #slug = ch["slug"]
        #num = ch["num"]

        str = "{}) {} [{}]".format(idx, display_name, active)
        print(str)


def get_channel_link(url):
    """ DOCS
    """

    rs = requests.Session()
    response = rs.get(url)
    #soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    pattern = re.compile("file:\s*'([^',]+)")
    match = pattern.search(response.text)

    if match:
        print(match.group(1))
        return match.group(1)

    return None


def main():
    """ DOCS
    """

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("ch_num", type=int, nargs="?",
                        help="Channel number")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        #
        # no args supplied
        #

        # obtain links
        ch_list = get_ch_list()

        # show them
        print_ch_list(ch_list)
    elif args.ch_num:
        #
        # channel arg supplied
        #
        ch_list = get_ch_list()
        get_channel_link(URL + ch_list[args.ch_num]["slug"])


    else:
        print("Something got wrong")


if __name__ == '__main__':
    sys.exit(main())
