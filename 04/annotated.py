from typing import Annotated


class ValueRange: ...
class MatchesRegex: ...

x: Annotated[int, ValueRange(3, 5)]
y: Annotated[str, MatchesRegex('[0-9]{4}')]
