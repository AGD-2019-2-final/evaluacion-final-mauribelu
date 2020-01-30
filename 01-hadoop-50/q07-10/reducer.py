import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    for line in sys.stdin:
        columna, columna2, columna3, columna4= line.split("\t")
        sys.stdout.write("{}\t{}\t{}".format(columna,columna3,columna4))