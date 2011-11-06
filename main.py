from argparse import ArgumentParser
from smores import Application

def parse_args():
    parser = ArgumentParser(description='A modest campfire client')
    parser.add_argument('-d', '--domain')
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    return parser.parse_args()

def main():
    args = parse_args()
    Application(args).start()

if __name__ == '__main__':
    main()
