from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class INode(Generic[T], ABC):

    @property
    @abstractmethod
    def value(self) -> T:
        pass

    @value.setter
    @abstractmethod
    def value(self, value: T) -> None:
        pass

    @property
    @abstractmethod
    def left(self) -> Optional['INode[T]']:
        pass

    @left.setter
    @abstractmethod
    def left(self, node: 'INode[T]') -> None:
        pass

    @property
    @abstractmethod
    def right(self) -> Optional['INode[T]']:
        pass

    @right.setter
    @abstractmethod
    def right(self, node: 'INode[T]') -> None:
        pass
