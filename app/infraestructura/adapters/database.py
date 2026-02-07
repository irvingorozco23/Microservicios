# infraestructura/adapters/db_adapter.py
class MemoriaUsuarioAdapter(UsuarioRepositoryPort):
    def __init__(self):
        self.db = {}

    def save(self, usuario):
        self.db[usuario.idusuario] = usuario
        return usuario

    def get_by_id(self, idusuario):
        return self.db.get(idusuario)
    
    # ... implementar update y delete
    