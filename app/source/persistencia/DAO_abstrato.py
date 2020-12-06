from abc import ABC, abstractmethod
from app.source.exception.entidade_nao_existente import EntidadeNaoExistente
from app.source.entidade.entidade_abstrata import EntidadeAbstrata
import pickle


class DAOabstrato(ABC):
    @abstractmethod
    def __init__(self, datasource: str = ""):
        self.__datasource = datasource
        self.__cache = {}
        self.__cache_list = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))
        self.__cache_list = list(self.__cache.values())

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))
        self.__cache_list = list(self.__cache.values())

    def add(self, key: str, obj: EntidadeAbstrata):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key: str):
        try:
            return self.__cache[key]
        except KeyError:
            raise EntidadeNaoExistente

    def getOneOrNone(self, key: str):
        return self.__cache.get(key)

    def remove(self, key: str):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise EntidadeNaoExistente

    def get_all(self):
        return self.__cache_list
