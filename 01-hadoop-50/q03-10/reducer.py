import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    for line in sys.stdin:
        valor, key, valor2 = line.split("\t")
        valor2=int(valor2)

        sys.stdout.write("{},{}\n".format(key, valor2))
