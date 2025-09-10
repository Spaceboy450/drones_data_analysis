from abc import ABC, abstractmethod

class AbstractProcessor(ABC):
    @abstractmethod
    def processing(self):
        #Метод должен быть реализован в дочерних классах
        pass