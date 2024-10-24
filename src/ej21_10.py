INGREDIENTES_VEGANOS = ('pimiento', 'tofu')
INGREDIENTES_PARA_PERSONAS = ('peperoni', 'jamon', 'salmon')

def elegir_ingrediente(tipo, ingredientes_personas, ingredientes_veganos):
    if tipo == 'normal':
        ingrediente = input(f'\nPuedes elegir entre {ingredientes_personas}\nEscribe cual quieres: ').lower()
        while ingrediente not in ingredientes_personas:
            ingrediente = input(f'\n**ERROR**\nPuedes elegir entre {ingredientes_personas}\nEscribe cual quieres: ').lower()
        return ingrediente
    else:
        ingrediente = input(f'\nPuedes elegir entre {ingredientes_veganos}\nEscribe cual quieres: ').lower()
        while ingrediente not in ingredientes_veganos:
            ingrediente = input(f'\n**ERROR**\nPuedes elegir entre {ingredientes_veganos}\nEscribe cual quieres: ').lower()
        return ingrediente 



def elegir_tipo_pizza():
    confirmacion = False
    tipo = input('\n¿Quieres pizza vegetariana? (Si dices que si me das miedo): ').lower()

    while tipo not in ('si', 'no'):
        tipo = input('\n**ERROR**\nResponde si o no\n¿Quieres pizza vegetariana? (Si dices que si me das miedo): ').lower()
    
    confirmacion = True

    if tipo == 'si':
        seguro = input('\n¿Estas seguro al 100x100?\nResponde: ')
        while seguro not in ('si', 'no'):
            seguro = input('\n¿Estas seguro al 100x100?\nResponde: ')
        if seguro == 'si':
            print('\nQue mal.')
            tipo = 'vegetariana'
            return tipo
        else:
            print('\nHaces bien.')
            tipo = 'normal'
            return tipo
    else:
        tipo = 'normal'
        return tipo
        
def main():
    tipo_pizza = elegir_tipo_pizza()
    ingrediente = elegir_ingrediente(tipo_pizza, INGREDIENTES_PARA_PERSONAS, INGREDIENTES_VEGANOS)

    print(f'\nHas elegido la pizza {tipo_pizza} con {ingrediente}.')

    if tipo_pizza == 'vegetariana':
        print('\nMe das asco.')

if __name__ == '__main__':
    main() 