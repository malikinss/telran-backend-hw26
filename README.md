# HW26: Generic Array with O(1) Operations

## Task Definition

Implement a generic class `MyArray[T]` that represents an array of fixed size
and supports constant-time operations.

---

### Class: `MyArray[T]`

#### Description

-   `MyArray` behaves like a fixed-size array of generic type `T`.
-   Supports:
    -   `set_all(value: T)` — set all elements to the same value in O(1)
    -   `set(index: int, value: T)` — set value at a specific index in O(1)
    -   `get(index: int) -> T` — get value at a specific index in O(1)

#### Constructor

```python
MyArray(size: int)
```

-   `size` — number of elements in the array
-   `size` may be very large (e.g. 1_000_000_000)
-   Does **not** allocate a full list

#### Example Usage

```python
arr = MyArray
arr.set_all(5)
assert arr.get(0) == 5
arr.set(3, 10)
assert arr.get(3) == 10
assert arr.get(1) == 5
```

---

### Constraints

-   All methods must run in **O(1)**
-   Memory usage must not scale with `size`
-   Invalid indices raise `IndexError`

---

## 📝 Description

`MyArray` is optimized for massive arrays where allocating memory proportional to `size` is impossible. It stores only overridden indices and a single default value.

## 🎯 Purpose

-   Practice generic programming in Python
-   Implement memory-efficient data structures
-   Ensure constant-time access and update operations

## 🔍 How It Works

-   `_default_value` stores the last value set by `set_all`
-   `_overrides` stores individual elements set with `set`
-   `get` checks `_overrides` first; otherwise returns `_default_value`

## 📜 Output Example

```python
arr = MyArray
arr.set_all(0)
arr.set(2, 99)
print([arr.get(i) for i in range(5)])  # [0, 0, 99, 0, 0]
```

## 📦 Usage

1. Import class:

```python
from src.my_array import MyArray
```

2. Create instance:

```python
arr = MyArray[int](size)
```

3. Use `set_all`, `set`, and `get`.

---

## 🧪 Running Tests

```bash
python -m unittest discover -s tests -v
```

---

## ✅ Dependencies

-   Python 3.10+

---

## 🗂 Project Structure

```
.
├── main.py
├── .gitignore
├── /.vscode
├── src
│   ├── __init__.py
│   └── my_array.py
└── tests
    ├── __init__.py
    └── test_my_array.py
```

## 📊 Project Status

✅ Implemented `MyArray`
✅ All unit tests passing

## 📄 License

MIT License

---

## 🧮 Conclusion

This homework demonstrates a memory-efficient, generic array implementation with O(1) operations.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
