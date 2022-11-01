# Typechecking (Python)

A small repo to test out how to integrate typechecking (mypy) into
CI/CD pipelines to make the code (or try) more robust, and run the
checks in an automated way. I might also add some linting steps
using pylint, flake8 or both.


- No, I don't like the concept of duck typing. I mean, for some really
concrete cases, like a constant, ok. But a function signature without type
annotations... nope.
- I treat types as a communication tool.
- We don't need to type ALL, ALWAYS. Some typing is better than ZERO typing.
- They help to reduce the mental maps and imaginations about the code.
- Sure, it takes some extra time to write them, but that time is FAR less than
the time it takes to interact with a codebase with no annotations.
- Yes, I would like to have a typed flavor of Python, just like there is
TypeScript on top of JavaScript
