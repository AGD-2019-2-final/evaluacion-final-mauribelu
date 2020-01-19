import sys


##
## Se usa una clase iterable para implementar el mapper.
##

class Mapper:

    def __init__(self, stream):
        ##
        ## almacena el flujo de entrada como una
        ## variable del objeto
        ##
        self.stream = stream

    def emit(self, key, value):
        ##
        ## escribe al flujo estandar de salida
        ##
        sys.stdout.write("{}\t{}\n".format(key, value))


    def status(self, message):
        ##
        ## imprime un reporte en el flujo de error
        ## no se debe usar el stdout, ya que en este
        ## unicamente deben ir las parejas (key, value)
        ##
        sys.stderr.write('reporter:status:{}\n'.format(message))


    def counter(self, counter, amount=1, group="ApplicationCounter"):
        ##
        ## imprime el valor del contador
        ##
        sys.stderr.write('reporter:counter:{},{},{}\n'.format(group, counter, amount))

    def map(self):

        word_counter = 0

        ##
        ## imprime un mensaje a la entrada
        ##
        self.status('Iniciando procesamiento ')

        for word in self:
            ##
            ## cuenta la cantidad de palabras procesadas
            ##
            word_counter += 1

            ##
            ## por cada palabra del flujo de datos
            ## emite la pareja (word, 1)
            ##
            self.emit(key=word, value=1)

        ##
        ## imprime un mensaje a la salida
        ##
        self.counter('num_words', amount=word_counter)
        self.status('Finalizadno procesamiento ')




    def __iter__(self):
        ##
        ## itera sobre cada linea de codigo recibida
        ## a traves del flujo de entrada
        ##
        for line in self.stream:
            lista = line.split(',')
            word = lista[2]
            ##
            ## itera sobre cada palabra de la linea
            ## (en los ciclos for, retorna las palabras
            ## una a una)
            ##
            yield word


if __name__ == "__main__":
    ##
    ## inicializa el objeto con el flujo de entrada
    ##
    mapper = Mapper(sys.stdin)

    ##
    ## ejecuta el mapper
    ##
    mapper.map()