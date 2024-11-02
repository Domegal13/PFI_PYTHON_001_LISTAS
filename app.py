from src.modulos.funciones import mostrar_menu, menu_switch_case, limpiar_consola
from colorama import init, Fore, Style
init()


#? ########################################### FUNCTION MAIN ##################################################################
def funcion_main():
    
    opcion_seleccionada = 1000
    while opcion_seleccionada != 7:
        mostrar_menu()
        try:
            opcion_seleccionada = int(input(Fore.GREEN + Style.BRIGHT + "Por favor, selecciona una opción (1-7): "  ))
            menu_switch_case(opcion_seleccionada)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Opción Inválida...")


if __name__ == "__main__":
    limpiar_consola()
    funcion_main()
