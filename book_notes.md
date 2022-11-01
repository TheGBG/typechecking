Some quick notes from the book "Robust Python", by Patrick Viafore

## Main idea

It is all about Intent:

Choose the right collection to express our intent in the code, e.g.:

- Preserve / not preserve order
- Allow / not allow duplicates
- Mutable / inmutable

and so on

If we want to count stuff, just use the `Counter`

```
from collections import Counter
def create_author_count_mapping(cookbooks: List[Cookbook]):
   return Counter(book.author for book in cookbooks)
```


**Law of least surprise**
The Law Of Least Surprise, also known as the Law of Least Aston‐
ishment, states that a program should always respond to the user in
the way that astonishes them the least.

Surprising behavior leads to confusion. 
Confusion leads to misplaced assumptions. 
Misplaced assumptions lead to bugs. 
And that is how you get unreliable software


## Annotating code with types

Types are a communication method

- Mechanical representation: for the machine
- Semantical representation: for the developers. This is the most important of
both


## Why do we need them?

- They are a communication tool, equally or more important as comments and
docstrings
- It is harder to forget to update the types when the code changes
- They reduce the ammount of assumputions we have to make
- Our imagination plays no role. The types are determining what we see. We
don't have to do any guessing.
- In the extreme case, if the code has no comments nor docstrings, the 
annotations can be really helpful
- Make the code more understandable: we don't need to go into the
- They add an extra layer of robustness when statically checked. If we use
mypy (or other tool) we can check the code calls and see if we are breaking
anything
- Make the code editor work better (code completion)


## How?

- basic types: str, int ...
- Optional: to replace none references in the codebase
- Union: present a selection of types
- Literal: restrict developres to very specific values
- Final: prevent variables from being rebound to a new value
- collections: lists, sets, etc

From a usability standpoint, your lists, sets, and dictionaries should nearly always be
homogenous

Example: the collection of Signals (type == News) is not homogenous. Thus, we
have to be careful when accessing values.


- TypedDict

Usefull to determine (when possible) the shape of the data. When it 
comes from an API, it can be quite tricky

- Dataclasses

Use them to group values toghether and represent relationships. They represent
a heterogeneous collection of variables, all rolled into a composite type.
Composite types are made up of multiple values, and should always represent some
sort of relationship or logical grouping.

An example would be the `Fraction` which contains two scalar values: a
`numerator` and a `denominator`

```
from fraction import Fraction
Fraction(numerator=3, denominator=5)  # represents the relationship between
                                      # numerator and denominator
```

Another example (can be found in the trend analysis project)

```
DateRange(from, to)
```


### Dataclass vs other structures

**vs dictionaries**

Dicts are more appropiated when are homogeneous. All the keys
and values have the same type. For this case, such as config,
it is better to use a dataclass

**vs TypedDict**
TypeDict should be used for reading data from configs
(such as json)

**vs namedtuple**
Better to use dataclass, unless we seek for specific compatibility with
python <= 3.6

Remember: dataclasses are good only if its attributes are trully independent
from eachother. If we need to create some sort of manipulation of att A based
on att B, we will need to create vanilla Classes.

## Chapter 10 - Classes

This will be the final user-defined type cover in the book


Why would we use a class over a dataclass? Invariants

### Invariants

Invariants are absolute truths about the code, and remain unchanged through
all the program. They can hold math rules, business rules, or anything that we
want to set and hold true. They don't have to mirror the real world. They just
have to reflect the truth in our system.

This chapter will focus on classes and their role preserving invariants.

Classes should follow the SRP: if they have too many inconex attributes, it
can be an indicator of low cohesion and bad code. The class takes care of
too much stuff.


## Final guide on user types

How to decide?

- Dictionaries: for when we handle external data, json filesm etc. If we use
them itearting or dynamically asking for keys, thats a wrong use (except from
API responses). In those cases it is recommended to parse them into another
user defined data type

- Enumerations: great for representing a union of discrete values when we
do not care about what those numbers are, and we only need to separate cases
in the code

- Data Classes: easy classes, for when the data is mostly independent from
eachother

- Classes: all about invariants, rules, and preserve business logic
