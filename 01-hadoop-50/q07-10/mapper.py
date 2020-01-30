import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        columna = line.split( )[0]
        columna2 = line.split( )[1]
        columna3 = int(line.split( )[2])
        columna4 = "{:03.0f}".format(columna3)
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(columna,columna4,columna2,columna3))