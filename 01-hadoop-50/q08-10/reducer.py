import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    curkey = None
    total1 = 0
    count = 0
    total2 = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:
            total1 = val + total1
            count += 1
            total2 =total1/count
        else:
            if curkey is None:
                curkey = key
                total1 = val
                count = 1
                total2 =total1/count
            else:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1, total2))
                curkey = key
                total1 = val
                count = 1
                total2 =total1/count
sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1, total2))
