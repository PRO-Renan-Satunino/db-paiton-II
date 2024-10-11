from services.usuario_services import UsuarioServices
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioServices(repository)

    service.criar_usuario("Mateus Brasileiro", "matue30@gmail.com", "333")

    print("\nListando todos os usuarios.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuario.nome} - {usuario.email}")

if __name__ == "__main__":
    main()