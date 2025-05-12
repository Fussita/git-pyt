
from typing import List, Tuple, Dict, Optional, TypeVar, List, NewType, TypedDict, Protocol, Callable, Annotated, TypeAlias

"""
    TypeVar: Genericos
    NewType: nombres distintos para el mismo tipado
    Final Type: Constantes
    Protocol: subtipado estructural o ducktypping
    Union Type: varios tipos
    Callable Type: funciones
    Annotated Type: metadatos a un tipo
    Alias type: nombres mas sencillos
"""

# List[int], Tuple[str, int], Dict[str, float]
# Optional[str] , str | None
name: str = "PEPE" # float, bool, None

# def greet(t: str, n: List[int]) -> str:
# greet(t="Juan", n=[1,2,3])
# def top( data: int | float ) -> str: return f'HALTA'

T = TypeVar('T')
UserId = NewType('UserId', int) # user_id = UserId(2077)
# def get_user_name(user_id: UserId)

# GENERICOS
# def get_first(l: List[T]) -> T: 
# numbers: List[int] = [1, 2, 3]
# result: int = get_first(numbers)

# TYPED DICT
class Leader(TypedDict): # author: Leader = {"name": "Gregorio Castillo", "year": 2077}
    name: str
    year: int

# CALLABLE
# def perform_action( action: Callable[[int, int], str] ) # action(1, 22)
# def sum_two(a: int, b: int) # perfom_action( sum_two )

# ANNOTATED
# def max_length(length: int):
# Name = Annotated[str, max_length(10)]
# def register_user(name: Name) -> None:

# TYPEALIAS
Matrix: TypeAlias = List[int|float] # a: Matrix = [1,2,3]
type Mat = List[int|float] # b: Mat = [1, 2]
