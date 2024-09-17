# main.py
from calculator.operations import add, subtract, multiply, divide, sqrt
from calculator.voice import speak

def main():
    print("Bienvenido a la calculadora que habla!")
    speak("Bienvenido a la calculadora que habla!")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raíz cuadrada")
        print("6. Salir")
        speak("Por favor, selecciona una operación.")
        
        choice = input("Selecciona una opción (1/2/3/4/5/6): ")
        
        if choice == '6':
            speak("Gracias por usar la calculadora. Adiós.")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        
        if choice == '1':
            result = add(num1, num2)
            speak(f"El resultado de sumar {num1} y {num2} es {result}.")
        elif choice == '2':
            result = subtract(num1, num2)
            speak(f"El resultado de restar {num1} y {num2} es {result}.")
        elif choice == '3':
            result = multiply(num1, num2)
            speak(f"El resultado de multiplicar {num1} y {num2} es {result}.")
        elif choice == '4':
            try:
                result = divide(num1, num2)
                speak(f"El resultado de dividir {num1} entre {num2} es {result}.")
            except ValueError as e:
                speak(str(e))
        elif choice == '5':
            num = float(input("Introduce el número para la raíz cuadrada: "))
            try:
                result = sqrt(num)
                speak(f"La raíz cuadrada de {num} es {result}.")
            except ValueError as e:
                speak(str(e))
        else:
            speak("Opción no válida. Por favor, intenta de nuevo.")
        
        print("\n" + "="*40)

if __name__ == "__main__":
    main()
