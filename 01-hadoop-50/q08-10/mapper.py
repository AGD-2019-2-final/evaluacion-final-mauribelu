import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
      #line = line[:-1]
      columna = line.split( )[0]
      #columna2 =line.split('-')[1]
      columna3 =line.split( )[2]
      sys.stdout.write("{}\t{}\n".format(columna, columna3))