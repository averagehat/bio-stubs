from Bio._py3k import basestring as basestring
from typing import Any, Optional

class _RestrictedDict(dict):
    def __init__(self, length: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def update(self, new_dict: Any) -> None: ...

class SeqRecord:
    id: Any = ...
    name: Any = ...
    description: Any = ...
    dbxrefs: Any = ...
    annotations: Any = ...
    letter_annotations: Any = ...
    features: Any = ...
    def __init__(self, seq: Any, id: str = ..., name: str = ..., description: str = ..., dbxrefs: Optional[Any] = ..., features: Optional[Any] = ..., annotations: Optional[Any] = ..., letter_annotations: Optional[Any] = ...) -> None: ...
    seq: Any = ...
    def __getitem__(self, index: Any): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, char: Any): ...
    def format(self, format: Any): ...
    def __format__(self, format_spec: Any): ...
    def __len__(self): ...
    def __lt__(self, other: Any) -> Any: ...
    def __le___(self, other: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def upper(self): ...
    def lower(self): ...
    def reverse_complement(self, id: bool = ..., name: bool = ..., description: bool = ..., features: bool = ..., annotations: bool = ..., letter_annotations: bool = ..., dbxrefs: bool = ...): ...
    def translate(self, table: str = ..., stop_symbol: str = ..., to_stop: bool = ..., cds: bool = ..., gap: Optional[Any] = ..., id: bool = ..., name: bool = ..., description: bool = ..., features: bool = ..., annotations: bool = ..., letter_annotations: bool = ..., dbxrefs: bool = ...): ...
