"""
# lcsc
Reverse-engineered API for [LCSC Electronics](https://www.lcsc.com/).

## Installation/Updating
- `pip install "git+https://github.com/mkaufman2023/LCSC.git@main"`
- `pip install --upgrade "git+https://github.com/mkaufman2023/LCSC.git@main"`

## Basic Usage
- *Importing the library*
```python
import lcsc
```
- *Getting product details given an LCSC part number*
```python
details = lcsc.get_product_details("C111887")
details.view()
```
- *Searching for products given a keyword*
```python
results = lcsc.get_search_results("L7805CV")
view(results)
```
- *Searching for products with constraints on stock*
```python
results = lcsc.get_search_results("L7805CV", min_stock=1000)
view(results)
```
- *Searching for products with optional sorting type*
```python
# Sorting by base-price (lowest -> highest)
results = lcsc.get_search_results("L7805CV", sort_by="price")
view(results)

# Sorting by quantity in stock (lowest -> highest)
results = lcsc.get_search_results("L7805CV", sort_by="stock")
view(results)
```
"""
from .types import ProductDetails, SearchResult
__all__ = ["view", "get_product_details", "get_search_results", "__version__"]

def view(data: list | dict) -> None: ...
def get_product_details(lcsc_part_number: str) -> "ProductDetails": ...
def get_search_results(keyword: str, min_stock: int = 500, sort_by: str = "stock") -> list["SearchResult"]: ...
