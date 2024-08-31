class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero not allowed."

def main():
    calc = Calculadora()
    
    print("Basic Calculator")
    while True:
        print("\nSelect the operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Split")
        print("5. Go out")
        
        opcion = input("Enter the option (1/2/3/4/5): ")

        if opcion == '5':
            print("leaving...")
            break
        
        if opcion in ['1', '2', '3', '4']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if opcion == '1':
                print(f"Result: {calc.sumar(a, b)}")
            elif opcion == '2':
                print(f"Result: {calc.restar(a, b)}")
            elif opcion == '3':
                print(f"Result: {calc.multiplicar(a, b)}")
            elif opcion == '4':
                print(f"Result: {calc.dividir(a, b)}")
        else:
            print("Invalid option. try again.")

if __name__ == "__main__":
    main()