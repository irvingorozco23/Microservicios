from abc import ABC, abstractmethod

class UsuarioRepositoryPort(ABC):
    @abstractmethod
    def save(self, usuario): pass
    @abstractmethod
    def get_by_id(self, idusuario): pass
    @abstractmethod
    def update(self, idusuario, nombre, email): pass
    @abstractmethod
    def delete(self, idusuario): pass