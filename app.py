import boto3
from botocore.exceptions import NoCredentialsError

# Configurar el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')  # Cambia la región según tu configuración

# Conectar con la tabla
table = dynamodb.Table('Personas')

def guardar_persona(id, nombre, edad):
    try:
        response = table.put_item(
            Item={
                'ID': id,
                'Nombre': nombre,
                'Edad': edad
            }
        )
        print("Persona guardada con éxito:", response)
    except NoCredentialsError:
        print("Credenciales no encontradas, asegúrate de haber configurado tus credenciales de AWS")

def obtener_persona(id):
    try:
        response = table.get_item(
            Key={
                'ID': id
            }
        )
        if 'Item' in response:
            print("Persona encontrada:", response['Item'])
        else:
            print("Persona no encontrada.")
    except NoCredentialsError:
        print("Credenciales no encontradas, asegúrate de haber configurado tus credenciales de AWS")

if __name__ == "__main__":
    # Pedir datos al usuario
    id = input("Introduce un ID: ")
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    # Guardar la persona en la base de datos
    guardar_persona(id, nombre, edad)

    # Recuperar y mostrar la persona desde la base de datos
    obtener_persona(id)
