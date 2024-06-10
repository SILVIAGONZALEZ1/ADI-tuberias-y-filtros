class Pipe:
    def __init__(self, filter_function):
        self.filter_function = filter_function
        self.next_pipe = None

    def set_next(self, pipe):
        self.next_pipe = pipe
        return pipe

    def process(self, data):
        result = self.filter_function(data)
        if self.next_pipe:
            return self.next_pipe.process(result)
        return result

def to_lowercase(data):
    return data.lower()

def remove_non_alpha(data):
    return ''.join(char for char in data if char.isalpha() or char.isspace())

def split_words(data):
    return data.split()

def count_words(data):
    return len(data)

# Crear los filtros
lowercase_pipe = Pipe(to_lowercase)
alpha_pipe = Pipe(remove_non_alpha)
split_pipe = Pipe(split_words)
count_pipe = Pipe(count_words)

# Conectar los filtros en una tubería
lowercase_pipe.set_next(alpha_pipe).set_next(split_pipe).set_next(count_pipe)

# Datos de entrada
input_text = "Hello, World! This is a test string with numbers 123 and symbols %$#."

# Procesar los datos a través de la tubería
result = lowercase_pipe.process(input_text)

print(f"El número de palabras en el texto procesado es: {result}")
