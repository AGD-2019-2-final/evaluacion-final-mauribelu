import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    valor_max = None
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        
        if valor_max is None:
          valor_max = val

        if key == curkey:
          valor_max= max(valor_max,val)
        else:
            
            if curkey is not None:
               
                sys.stdout.write("{}\t{}\n".format(curkey, valor_max))

            curkey = key
            valor_max = val
            sys.stdout.write("{}\t{}\n".format(curkey,valor_max))