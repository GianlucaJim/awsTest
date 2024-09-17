import boto3
from botocore.exceptions import NoCredentialsError

# Configurar el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-2') 

# Conectar con la tabla
table = dynamodb.Table('Personas')

# Función para guardar un ítem en DynamoDB
def guardar_persona(id, nombre, edad):
    try:
        response = table.put_item(
            Item={
                'ID': id,
                'Nombre': nombre,
                'Edad': edad
            }
        )
        print(f"Persona {nombre} guardada con éxito.")
    except NoCredentialsError:
        print("Credenciales no encontradas. Asegúrate de haber configurado tus credenciales de AWS.")

# Función para obtener un ítem de DynamoDB
def obtener_persona(id):
    try:
        response = table.get_item(
            Key={
                'ID': id
            }
        )
        # Verificar si el ítem fue encontrado
        if 'Item' in response:
            persona = response['Item']
            print(f"Persona encontrada: ID={persona['ID']}, Nombre={persona['Nombre']}, Edad={persona['Edad']}")
        else:
            print("Persona no encontrada.")
    except NoCredentialsError:
        print("Credenciales no encontradas. Asegúrate de haber configurado tus credenciales de AWS.")

# menú
def mostrar_menu():
    print("\nMenú:")
    print("1 - Guardar persona")
    print("2 - Buscar persona por ID")
    print("3 - Salir")
    return input("Elige una opción: ")

# Punto de entrada principal del programa
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Guardar persona
            id = input("Introduce un ID: ")
            nombre = input("Introduce el nombre: ")
            edad = int(input("Introduce la edad: "))
            guardar_persona(id, nombre, edad)

        elif opcion == '2':
            # Buscar persona por ID
            id_buscar = input("Introduce el ID de la persona que deseas buscar: ")
            obtener_persona(id_buscar)

        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")
