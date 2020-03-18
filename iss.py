#!/usr/bin/env python

__author__ = 'Rob Spears (GitHub: Forty9Unbeaten)'

import requests
import argparse
import sys
from datetime import datetime


def get_astros():
    '''Make request to API and return the names of
     astronauts currently in space and the craft they are
     currently on board...'''

    r = requests.get('http://api.open-notify.org/astros.json')
    astro_info = r.json()['people']

    return astro_info


def print_astro_info(astro_info):
    '''Accepts data about the astronauts currently in space
     and prints their name, the spacecrat they are on board and
     the number of astronauts in space'''

    print('\n\tAstronaut Information:\n')
    for astro in astro_info:
        print('\tName:\t{}'.format(astro['name']))
        print('\tSpacecraft:\t{}\n'.format(astro['craft']))
    print('\tTotal astronauts in space:\t{}\n'.format(len(astro_info)))


def get_iss_location():
    '''Make call to API and return location data for the
     International Space Station'''

    r = requests.get('http://api.open-notify.org/iss-now.json')
    loc_info = r.json()
    time = datetime.fromtimestamp(loc_info['timestamp'])
    return {
        'lat': loc_info['iss_position']['latitude'],
        'lon': loc_info['iss_position']['longitude'],
        'time': time.strftime('%B %d, %Y *** %I:%M:%S %p')
    }


def print_iss_loc(loc_data):
    '''Accepts data about the location of the International
     Space Station and prints the latitude, longitude and
     the time'''
    print('\n\tInternational Space Station Location:\n')
    print('\tLatitude:\t{}'.format(loc_data['lat']))
    print('\tLongitude:\t{}'.format(loc_data['lon']))
    print('\tTime:\t{}\n'.format(loc_data['time']))


def create_parser():
    '''Creates and returns a command-line argument parser'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--astronauts',
                        action='store_true',
                        dest='astros',
                        help='Show information about all ' +
                        'astronauts in space')
    parser.add_argument('-l', '--location',
                        action='store_true',
                        dest='loc',
                        help='Show location data for the ' +
                        'International Space Station')
    return parser


def main(args):

    # create argument parser and namespace of parsed
    # shell arguments
    parser = create_parser()
    ns = parser.parse_args()

    # if no arguments provided, show help prompt
    if not args:
        parser.print_help()
        sys.exit()

    if ns.astros:
        astronauts = get_astros()
        print_astro_info(astronauts)
    if ns.loc:
        location = get_iss_location()
        print_iss_loc(location)


if __name__ == '__main__':
    main(sys.argv[1:])
