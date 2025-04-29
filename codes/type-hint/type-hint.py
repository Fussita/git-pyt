# from typing import List, Tuple, Dict , Union

# TYPE HINTS
name: str = 'Pepe'

# int, float, bool, None
# List[int], Dict[str, float]

def greet(name: str) -> str:
    return f"hola, {name}"

def process(data: int | float) -> str:
    pass

def get_name() -> str | None:
    pass

from typing import TypeVar, List

T = TypeVar('T')

def get_first(l: List[T]) -> T:
    return l[0]


from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def get_user_name(user_id: UserId) -> str:
    # Implementación específica para manejar un user ID
    return "Gregorio Castillo"

def get_order_details(order_id: OrderId) -> str:
    # Implementación específica para manejar un order ID
    return "iPhone 2000"

user_id = UserId(2077)
order_id = OrderId(9527)


from typing import TypedDict

class Leader(TypedDict):
    name: str
    year: int

author: Leader = {"name": "Gregorio Castillo", "year": 2077}

print(author)

from typing import Callable


def perform_action(action: Callable[[int, int], str], x: int, y: int) -> None:
    result = action(x, y)
    print(f"Resultado de la acción: {result}")


def sum_two(a: int, b: int) -> str:
    return f"La suma es: {a + b}"


perform_action(sum_two, 5, 3)
# Action Result: The sum is: 8




def function_call(function) -> int:
    number_to_add = 5
    return function(number_to_add)

print(function_call(function=plus_one))