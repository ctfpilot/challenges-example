import requests
import argparse

# ----------------- Logger class -----------------

# Fold this line in to minimize the code
class Logger:
    level = 0
    
    def __init__(self, verbose: bool, debug: bool = False):
        if verbose:
            self.level = 1
            self.write('Verbose logging enabled')
        if debug:
            self.write('[DEBUG] Debug logging enabled')
            self.level = 2

    '''
    Write a message to the console, regardless of the log level
    '''
    def write(self, msg: str):
        print(msg)

    '''
    Log a message to the console, if verbose logging is enabled
    '''
    def log(self, msg: str):
        if self.level > 0:
            print(msg)
    
    '''
    Log a message to the console, if debug logging is enabled
    '''
    def debug(self, msg: str):
        if self.level > 1:
            print(f'[DEBUG] {msg}')

logger = Logger(False, False) # Is replaced by the logger in the main function

# ----------------- Challenge specific code -----------------

def solve(url: str, flag: str) -> bool:
    # Solve the challenge
    # Ensure website is reachable
    try:
        logger.debug(f'Connecting to {url}')
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        logger.log(f'Failed to connect to {url}')
        return False
    
    # Send a GET request to the robots.txt file
    try:
        logger.debug('Sending GET request to robots.txt')
        response = requests.get(url + '/robots.txt')
    except requests.exceptions.RequestException as e:
        logger.log('Failed to connect to /robots.txt')
        return False
    # Check if flag.txt is disallowed
    if '/flag.txt' in response.text:
        logger.log('Flag.txt is disallowed')
    else:
        logger.log('Flag.txt not specified in /robots.txt')
        return False
    
    # Send a GET request to the flag.txt file
    try:
        logger.debug('Sending GET request to /flag.txt')
        response = requests.get(url + '/flag.txt')
    except requests.exceptions.RequestException as e:
        logger.log('Failed to connect to flag.txt')
        return False
    # Check if the response contains the flag
    if flag in response.text:
        logger.log('Flag found in flag.txt')
        return True
    else:
        logger.log('Flag not found')
    return False

# ----------------- Helper classes and functions -----------------

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to the challenge', type=str)
    parser.add_argument('flag', help='Correct flag, to check the challenge against')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true', default=False)
    parser.add_argument('-d', '--debug', help='Debug output', action='store_true', default=False)
    return parser.parse_args()

def main():
    args = get_args()
    url = args.url
    flag = args.flag
    
    logger = Logger(args.verbose, args.debug)
    logger.log(f'URL: {url}')
    logger.log(f'Flag: {flag}')
    
    logger.log('Starting solve script...')
    if solve(url, flag):
        print('Challenge solved successfully')
        exit(0)
    else:
        print('Failed to solve challenge')    
        exit(1)

if __name__ == '__main__':
    main()
