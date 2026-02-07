class UsuarioService:
    def __init__(self, repository: UsuarioRepositoryPort):
        self.repository = repository

    def registrar_usuario(self, id, nombre, email):
        nuevo_usuario = Usuario(id, nombre, email)
        return self.repository.save(nuevo_usuario)

    def obtener_usuario(self, id):
        return self.repository.get_by_id(id)