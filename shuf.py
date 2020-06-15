

import random, sys, argparse, string

maxnum=-1
repeats=False

def basic():
    input = sys.stdin.readlines()
    i = 0
    while input != [] and i!=maxnum:
        chosen=(random.choice(input))
        print(chosen.rstrip())
        if repeats==False:
            input.remove(chosen)
        i+=1


def a_file(thefile):
    lines = thefile.readlines()
    thefile.close()
    i = 0
    while lines != [] and i!=maxnum:
        chosen=random.choice(lines)
        print(chosen.rstrip())
        if repeats==False:
            lines.remove(chosen)
        i+=1

def numbers(rnum):
    newone = rnum.split('-')
    try:
        low = int(newone[0])
        high = int(newone[1])
    except ValueError:
        sys.exit("invalid input range")
    if low<0 or high<0 or low>high:
        sys.exit("0 <= low <= high")
    thelist = list(range(low,high+1))
    i = 0
    while thelist != [] and i!=maxnum:
        chosen=random.choice(thelist)
        print(chosen)
        if repeats==False:
            thelist.remove(chosen)
        i+=1

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'))
    group.add_argument('-i', '--input-range', nargs=1, 
help='this generates a random permutation of the integers in [LO, HI]')
    parser.add_argument('-n', "--head-count", type=int, nargs=1, 
help='at most given # of outputs')
    parser.add_argument('-r', "--repeat", action="store_true", help='allow repeats')
    args = parser.parse_args()
    
    if args.head_count:
        global maxnum
        maxnum=args.head_count[0]
        if maxnum<0:
            sys.exit("COUNT>=0")
    if args.repeat:
        global repeats
        repeats=True
    if args.input_range is not None:
        numbers(args.input_range[0])
    if args.infile is not None:
        a_file(args.infile)
    if args.input_range is None and args.infile is None:
        basic()
    

if __name__ == "__main__":
    main()
