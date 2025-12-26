# HW26: Generic Array with O(1) Operations

## Task Definition

Implement a generic class `MyArray[T]` that represents an array of fixed size
and supports constant-time operations.

---

### Requirements

1.  Class

```python
class MyArray(Generic[T]):
```

2.  Constructor

```py
def __init__(self, size: int):
```

-   `size` — number of elements in the array
-   `size` may be extremely large (e.g. `1_000_000_000`)
-   Do **not** allocate a real list of this size

3.  Methods

    `setAll`

```python
def setAll(self, value: T) -> None:
```

-   Sets all elements to the given value
-   Must work in **O(1)** time

    `set`

```python
def set(self, index: int, value: T) -> None:
```

-   Sets value at `index`
-   Valid indices: `0 <= index < size`
-   Raises `IndexError` if index is out of range
-   Must work in **O(1)** time

    `get`

```python
def get(self, index: int) -> T:
```

-   Returns value at `index`
-   Valid indices: `0 <= index < size`
-   Raises `IndexError` if index is out of range
-   Must work in **O(1)** time

---

### Constraints

-   All methods (`__init__`, `setAll`, `set`, `get`) must be **O(1)**
-   Iterating over the array or allocating memory proportional to `size`
    is not allowed

---

### Testing

Write unit tests for:

```python
MyArray[int]
```

Tests should cover:

-   `setAll`, `set`, `get`
-   Boundary indices
-   `IndexError` for invalid indices

---

## 📝 Description

## 🎯 Purpose

## 🔍 How It Works

## 📜 Output Example

## 📦 Usage

## 🧪 Running Tests

## ✅ Dependencies

## 🗂 Project Structure

## 📊 Project Status

## 📄 License

MIT License

---

## 🧮 Conclusion

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
