# Concepts covered

Every concept below appears in at least one script in this repo, with the file that
demonstrates it.

## 1. Input and output

| Concept | Where |
|---|---|
| `input()` and type casting with `int()` | `calculator.py`, `factorial.py`, `student_record.py` |
| `print()` with multiple arguments | `ca1_grading_and_area.py` |
| `print("\n")` for a blank line | `ca1_grading_and_area.py` |
| `print(end="")` to suppress the newline | `number_triangle.py` |
| Escape sequences inside a string (`\n`) | `calculator.py` |

## 2. Variables and data types

| Concept | Where |
|---|---|
| Integer, string, float values | all files |
| Variable assignment and re-assignment | `number_triangle.py` |
| Naming conventions — lowercase with underscores | `ca1_grading_and_area.py` |

## 3. Operators

| Concept | Where |
|---|---|
| Arithmetic `+ - * / %` | `calculator.py` |
| Comparison `>=` | `ca1_grading_and_area.py` |
| Equality `==` | `calculator.py` |

## 4. Control flow

| Concept | Where |
|---|---|
| `if` / `elif` / `else` | `calculator.py`, `ca1_grading_and_area.py` |
| Cascading thresholds and why order matters | `ca1_grading_and_area.py` |
| Nested conditionals | `ca1_grading_and_area.py` |

## 5. Loops

| Concept | Where |
|---|---|
| `for` loops | `first_ten_odd_numbers.py`, `factorial.py` |
| `range(start, stop)` | `first_ten_odd_numbers.py` |
| `range(start, stop, step)` with a negative step | `number_triangle.py` |
| Nested loops | `number_triangle.py` |
| Accumulator variable (`fact = fact * i`) | `factorial.py` |

## 6. Collections

| Concept | Where |
|---|---|
| List creation and indexing | `lists_sets_and_dicts.py` |
| Negative indexing (`fruits[-1]`) | `lists_sets_and_dicts.py` |
| `list.append()` | `lists_sets_and_dicts.py` |
| `len()` | `lists_sets_and_dicts.py` |
| Sets and uniqueness | `lists_sets_and_dicts.py` |
| Dictionaries — key/value pairs | `lists_sets_and_dicts.py`, `student_record.py` |

## 7. Functions

| Concept | Where |
|---|---|
| `def` and function naming | `addition_function.py` |
| Parameters and arguments | `addition_function.py` |
| `return` vs printing inside a function | `addition_function.py` |

## 8. Strings

| Concept | Where |
|---|---|
| `str.upper()` and `str.lower()` | `string_case_converter.py` |
| String methods | `string_case_converter.py` |

---

## Fixed after the first pass

Both were genuine errors in my class code. I found them while writing up this concept map and
fixed them in the commit history rather than quietly editing, so the change is visible.

### `factorial.py` — print inside the loop

`print(fact)` sat inside the `for` block, so entering `5` printed `1, 2, 6, 24, 120` — the
partial products — instead of the final answer. The accumulation itself was correct; only the
reporting was in the wrong place. Accumulating and reporting are separate concerns, so the
print now sits below the loop and `5` gives `120`.

### `number_triangle.py` — exercise never implemented

The nested-loop triangle from 2 Sep was fully commented out, with a placeholder `print("sagar")`
as the only live code. The commented version also counted down with `range(n, 1, -1)`, which is
backwards for a left-aligned triangle. Implemented with the outer loop counting up, and verified
against `n = 5`.

## Known issues

Still unfixed, and left visible rather than tidied away.

### `student_record.py` — variable shadows a builtin

The dictionary is bound to `dict`, which shadows Python's built-in `dict` type for the rest of
the module. Harmless in a five-line file, a real problem in anything larger. Same issue with
`str` in `string_case_converter.py`.

### `lists_sets_and_dicts.py` — names reused for different types

`a` is first a list, then a set, and `b` is first a number pair, then a dict. Reusing one name
for unrelated types makes the file harder to follow than it needs to be.

---

## Not yet covered

Things I have not used yet, listed so this file doubles as a to-do list:

- File handling (`open`, reading and writing)
- Exception handling (`try` / `except`)
- Modules and imports
- `while` loops
- Functions with default and keyword arguments
- List comprehensions
- Anything from the standard library — `math`, `datetime`, `random`
- Third-party libraries — `pandas`, `numpy`, `matplotlib`

These are the gaps between this repo and the data analysis work I want to move into next.
