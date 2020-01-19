import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":    
    for line in sys.stdin:
      tipo= line.split(',')[4]
      valor= line.split(',')[5]
      
      sys.stdout.write("{}\t1{}\n".format(tipo,valor))