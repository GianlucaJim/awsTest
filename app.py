import boto3
from botocore.exceptions import NoCredentialsError

# Configurar el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')  # Cambia la región según corresponda

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
        print(f"Persona {nombre} guardada con éxito: {response}")
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

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Pedir datos al usuario
    id = input("Introduce un ID: ")
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    # Guardar la persona en la base de datos
    guardar_persona(id, nombre, edad)

    # Preguntar si se desea recuperar la persona guardada
    respuesta = input("¿Deseas buscar la persona por su ID? (s/n): ")
    if respuesta.lower() == 's':
        id_buscar = input("Introduce el ID de la persona que deseas buscar: ")
        obtener_persona(id_buscar)
