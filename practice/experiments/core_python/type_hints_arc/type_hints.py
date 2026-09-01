def double(n: int) -> int:
    return n * 2

result = double("ab")


def find(name: str) -> str | None:
    return {"cal": "calvin"}.get(name)

name = find("nobody")
if name is not None:        # ← you PROVE to the enforcer that None is gone
    print(name.upper())     # inside here, name is str — squiggle vanishes

from typing import Protocol, reveal_type


class Quacker(Protocol):
    def quack(self) -> str: ...

def make_it_quack(thing: Quacker) -> str:
    return thing.quack()

class Duck:
    def quack(self) -> str:
        return "Quack!"

class Rock:
    pass

make_it_quack(Duck())   # (1) squiggle or clean? why?
make_it_quack(Rock())   # (2) squiggle or clean? why?