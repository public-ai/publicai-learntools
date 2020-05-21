"""
Copyright 2019, All rights reserved.
Author : SangJae Kang
Mail : rocketgrowthsj@gmail.com
"""
class bcolors:
    """
    Text Background Color
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def get_tag(cls, bcolor:str):
        if bcolor.upper() in dir(cls):
            return  cls.__getattribute__(cls, bcolor.upper())
        return ""


def print_with_tag(message, bcolor="okblue"):
    """
    bcolor :
        'HEADER' 'OKBLUE' 'OKGREEN' 'WARNING'
        'FAIL'   'ENDC' 'BOLD' 'UNDERLINE'
    """
    bcolor = bcolors.get_tag(bcolor)
    if bcolor:
        print(bcolor + str(message) + bcolors.ENDC)
    else:
        print(message)
