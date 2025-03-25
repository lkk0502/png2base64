import argparse
import base64
import sys

if __name__ == '__main__':

    args = argparse.ArgumentParser()
    args.add_argument('imagepath', nargs='?', help='image Path.')

    if not args.parse_args().imagepath:
        args.parse_args(['--help'])
        sys.exit()

    png = args.parse_args().imagepath
    with open(png, 'rb') as f:
        ls_f = base64.b64encode(f.read())

    print(f'data:image/png;base64,{ls_f}')
