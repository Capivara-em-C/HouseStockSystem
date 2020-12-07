from abc import ABC, abstractmethod
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
import pickle


class DAOAbstrato(ABC):
    @abstractmethod
    def __init__(self, local_arquivo: str = ""):
        self.__local_arquivo = "app/database/" + local_arquivo + ".pkl"
        self.__cache = {}
        self.__cache_lista = []

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__local_arquivo, 'wb'))
        self.__cache_lista = list(self.__cache.values())

    def __load(self):
        self.__cache = pickle.load(open(self.__local_arquivo, 'rb'))
        self.__cache_lista = list(self.__cache.values())

    def add(self, chave: str, obj: EntidadeAbstrata):
        self.__cache[chave] = obj
        self.__dump()

    def get(self, chave: str):
        try:
            return self.__cache[chave]
        except KeyError:
            raise EntidadeNaoExistente()

    def get_one_or_none(self, chave: str):
        return self.__cache.get(chave)

    def remove(self, chave: str, eh_atualizacao: bool):
        try:
            self.__cache.pop(chave)
            self.__dump()
        except KeyError:
            if eh_atualizacao:
                pass
            else:
                raise EntidadeNaoExistente

    def get_all(self):
        return self.__cache_lista
