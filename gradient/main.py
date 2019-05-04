import sys
import os

__version__ = "0.0.1"

def main():
    args = sys.argv[:]
    prog = os.path.basename(args.pop(0))

    if not args:
        usage(prog)
        sys.exit(1)

    cmd = args.pop(0)

    help_opts = ['help', '--help', '-h']

    if cmd in help_opts:
        usage(prog)
        sys.exit(0)

    if cmd in ['version', '--version', '-v']:
        vers(prog)
        sys.exit(0)
		
def vers(prog):
    print('%s %s' % (prog, __version__))
	
def usage(prog):
    print('usage: %s version' % prog)