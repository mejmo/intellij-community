from typing import List, Any, TypeVar, Union, Iterable, Iterator, TypeVar, Generic, Type, Sized, Reversible, Container, Mapping
from abc import ABCMeta

_T = TypeVar('_T', bound=Enum)
_S = TypeVar('_S', bound=Type[Enum])

# Note: EnumMeta actually subclasses type directly, not ABCMeta.
# This is a temporary workaround to allow multiple creation of enums with builtins
# such as str as mixins, which due to the handling of ABCs of builtin types, cause
# spurious inconsistent metaclass structure. See #1595.
class EnumMeta(ABCMeta, Iterable[Enum], Sized, Reversible[Enum], Container[Enum]):
    def __iter__(self: Type[_T]) -> Iterator[_T]: ...
    def __reversed__(self: Type[_T]) -> Iterator[_T]: ...
    def __contains__(self, member: Any) -> bool: ...
    def __getitem__(self: Type[_T], name: str) -> _T: ...
    @property
    def __members__(self: Type[_T]) -> Mapping[str, _T]: ...

class Enum(metaclass=EnumMeta):
    def __new__(cls: Type[_T], value: Any) -> _T: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __dir__(self) -> List[str]: ...
    def __format__(self, format_spec: str) -> str: ...
    def __hash__(self) -> Any: ...
    def __reduce_ex__(self, proto: Any) -> Any: ...

    name = ...  # type: str
    value = ...  # type: Any

class IntEnum(int, Enum): ...

def unique(enumeration: _S) -> _S: ...
