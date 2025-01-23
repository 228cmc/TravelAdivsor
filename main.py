from db_setup import SessionLocal, init_db
from queries import create_user, get_all_users

def main():
    init_db()  # Ensure tables are created
    db = SessionLocal()

    print("=== Bienvenido al programa ===")
    while True:
        print("\n1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            name = input("Ingresa el nombre del usuario: ")
            email = input("Ingresa el email del usuario: ")
            user = create_user(db, name, email)
            print(f"Usuario creado: {user}")
        elif opcion == "2":
            users = get_all_users(db)
            for user in users:
                print(f"ID: {user.id}, Nombre: {user.name}, Email: {user.email}")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")
    db.close()

if __name__ == "__main__":
    main()
