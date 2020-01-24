from Bio import Alphabet as Alphabet, BiopythonWarning as BiopythonWarning
from Bio.Alphabet import IUPAC as IUPAC
from Bio.Data import CodonTable as CodonTable
from Bio.Data.IUPACData import ambiguous_dna_complement as ambiguous_dna_complement, ambiguous_rna_complement as ambiguous_rna_complement
from Bio._py3k import basestring as basestring, range as range
from typing import Any, Optional

class Seq:
    alphabet: Any = ...
    def __init__(self, data: Any, alphabet: Any = ...) -> None: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __len__(self): ...
    def __getitem__(self, index: Any): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def tomutable(self): ...
    def count(self, sub: Any, start: int = ..., end: Any = ...): ...
    def count_overlap(self, sub: Any, start: int = ..., end: Any = ...): ...
    def __contains__(self, char: Any): ...
    def find(self, sub: Any, start: int = ..., end: Any = ...): ...
    def rfind(self, sub: Any, start: int = ..., end: Any = ...): ...
    def index(self, sub: Any, start: int = ..., end: Any = ...): ...
    def rindex(self, sub: Any, start: int = ..., end: Any = ...): ...
    def startswith(self, prefix: Any, start: int = ..., end: Any = ...): ...
    def endswith(self, suffix: Any, start: int = ..., end: Any = ...): ...
    def split(self, sep: Optional[Any] = ..., maxsplit: int = ...): ...
    def rsplit(self, sep: Optional[Any] = ..., maxsplit: int = ...): ...
    def strip(self, chars: Optional[Any] = ...): ...
    def lstrip(self, chars: Optional[Any] = ...): ...
    def rstrip(self, chars: Optional[Any] = ...): ...
    def upper(self): ...
    def lower(self): ...
    def encode(self, encoding: str = ..., errors: str = ...): ...
    def complement(self): ...
    def reverse_complement(self): ...
    def transcribe(self): ...
    def back_transcribe(self): ...
    def translate(self, table: str = ..., stop_symbol: str = ..., to_stop: bool = ..., cds: bool = ..., gap: Optional[Any] = ...): ...
    def ungap(self, gap: Optional[Any] = ...): ...
    def join(self, other: Any): ...

class UnknownSeq(Seq):
    alphabet: Any = ...
    def __init__(self, length: Any, alphabet: Any = ..., character: Optional[Any] = ...) -> None: ...
    def __len__(self): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def __getitem__(self, index: Any): ...
    def count(self, sub: Any, start: int = ..., end: Any = ...): ...
    def count_overlap(self, sub: Any, start: int = ..., end: Any = ...): ...
    def complement(self): ...
    def reverse_complement(self): ...
    def transcribe(self): ...
    def back_transcribe(self): ...
    def upper(self): ...
    def lower(self): ...
    def translate(self, **kwargs: Any): ...
    def ungap(self, gap: Optional[Any] = ...): ...
    def join(self, other: Any): ...

class MutableSeq:
    array_indicator: str = ...
    data: Any = ...
    alphabet: Any = ...
    def __init__(self, data: Any, alphabet: Any = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __len__(self): ...
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __delitem__(self, index: Any) -> None: ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def append(self, c: Any) -> None: ...
    def insert(self, i: Any, c: Any) -> None: ...
    def pop(self, i: int = ...): ...
    def remove(self, item: Any) -> None: ...
    def count(self, sub: Any, start: int = ..., end: Any = ...): ...
    def count_overlap(self, sub: Any, start: int = ..., end: Any = ...): ...
    def index(self, item: Any): ...
    def reverse(self) -> None: ...
    def complement(self) -> None: ...
    def reverse_complement(self) -> None: ...
    def extend(self, other: Any) -> None: ...
    def toseq(self): ...
    def join(self, other: Any): ...

def transcribe(dna: Any): ...
def back_transcribe(rna: Any): ...
def translate(sequence: Any, table: str = ..., stop_symbol: str = ..., to_stop: bool = ..., cds: bool = ..., gap: Optional[Any] = ...): ...
def reverse_complement(sequence: Any): ...
def complement(sequence: Any): ...
