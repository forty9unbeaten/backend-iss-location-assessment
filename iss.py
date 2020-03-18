#!/usr/bin/env python

__author__ = 'Rob Spears (GitHub: Forty9Unbeaten)'

import requests
import argparse


def get_astros():
    '''Make request to API and return the names of
     astronauts currently in space and the craft they are
     currently on board...'''

    r = requests.get('http://api.open-notify.org/astros.json')
    astro_info = r.json()['people']

    return astro_info


def print_astro_info(astro_info):
    '''Accepts JSON data about the astronauts currently in space
     and prints their name, the spacecrat they are on board and
     the number of astronauts in space'''

    print('\n\tAstronaut Information:\n')
    for astro in astro_info:
        print('\tName:\t{}'.format(astro['name']))
        print('\tSpacecraft:\t{}\n'.format(astro['craft']))
    print('\tTotal astronauts in space:\t{}\n'.format(len(astro_info)))


def create_parser():
    '''Creates and returns a command-line argument parser'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--astronauts',
                        action='store_true',
                        dest='astros',
                        help='Show a information about all ' +
                        'astronauts in space')
    return parser


def main():
    parser = create_parser()
    ns = parser.parse_args()

    if ns.astros:
        astronauts = get_astros()
        print_astro_info(astronauts)


if __name__ == '__main__':
    main()
