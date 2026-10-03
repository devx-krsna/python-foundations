# Python Foundations — Learning Log

Coursework from **Computational Thinking with Python** (first semester), organised by topic
instead of by the date the file happened to be saved.

This is a learning log, not a finished project. Each script is a small exercise from a class
session, kept as it was originally written so the progression is visible. Dated
**25 Aug – 23 Sep 2026**.

## Why it's organised this way

My class notes were originally one file per session (`25aug.py`, `3sep.py`, and so on), which
made them hard to look things up in. Grouping them by topic means everything on lists sits
together, everything on loops sits together, and the README can tell you what each one
actually does.

## Contents

### 01 — Control flow

| File | Topic | Session |
|---|---|---|
| [`calculator.py`](01-control-flow/calculator.py) | `if` / `elif` / `else`, arithmetic operators | 26 Aug 2026 |
| [`ca1_grading_and_area.py`](01-control-flow/ca1_grading_and_area.py) | Cascading conditionals for grade bands; variables and input (CA1) | 9 Sep 2026 |

### 02 — Loops

| File | Topic | Session |
|---|---|---|
| [`first_ten_odd_numbers.py`](02-loops/first_ten_odd_numbers.py) | `range()` and `for` loops | 25 Aug 2026 |
| [`number_triangle.py`](02-loops/number_triangle.py) | Nested loops, `print(end="")` | 2 Sep 2026 |
| [`factorial.py`](02-loops/factorial.py) | Accumulator pattern in a `for` loop | 16 Sep 2026 |

### 03 — Collections

| File | Topic | Session |
|---|---|---|
| [`lists_sets_and_dicts.py`](03-collections/lists_sets_and_dicts.py) | List indexing (incl. negative), `append`, `len`, sets, dictionaries | 3 Sep 2026 |
| [`student_record.py`](03-collections/student_record.py) | Building a dictionary from user input | 10 Sep 2026 |

### 04 — Functions and strings

| File | Topic | Session |
|---|---|---|
| [`addition_function.py`](04-functions-and-strings/addition_function.py) | Function definition, parameters, `return` | 11 Sep 2026 |
| [`string_case_converter.py`](04-functions-and-strings/string_case_converter.py) | `str.upper()` / `str.lower()` | 23 Sep 2026 |

## Running them

Every script is standalone and takes input from the terminal. Python 3.10 or newer.

```bash
git clone https://github.com/devx-krsna/python-foundations.git
cd python-foundations
python 02-loops/factorial.py
```

The ones that need input will prompt you — for example `factorial.py` asks for a number, and
`ca1_grading_and_area.py` asks for a mark, then a length and a breadth.

## Concepts covered

See [`docs/concepts-covered.md`](docs/concepts-covered.md) for the full list mapped to files.

## Status

Still in progress. This is the Python fundamentals layer — the part I need solid before moving
on to data handling and `pandas`. Next up is turning the E-waste report into an actual data
analysis project.

## Note on the code

The scripts are kept exactly as written in class. I have deliberately not rewritten them into
cleaner form, so the repo reflects what I actually wrote rather than a tidied-up version of it.
Where something is wrong I would rather it stay visible and get fixed properly — see
[`docs/concepts-covered.md`](docs/concepts-covered.md) for the notes on known issues.
