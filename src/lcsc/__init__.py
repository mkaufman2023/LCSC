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
__all__ = ["view", "get_product_details", "get_search_results", "__version__"]
__version__ = "1.0.1"



def view(data: list | dict):
    """
    Views a JSON-serializable object in a GUI window.

    ## Parameters
    - `data` ( *list* | *dict* ) - The data to view.
    """
    from pyjsonviewer import view_data
    view_data(json_data=data)



def get_product_details(lcsc_part_number: str):
    """
    Get details for a product with a specific LCSC part #.

    ## Parameters
    - `lcsc_part_number` ( *str* ) - The part number on the product's page, under the `LCSC Part #` label.

    ## Returns
    - `product_details` ( *ProductDetails* ) - Dataclass object containing the product's details.

    ## Example
    ```python
    >>> lcsc = LCSC()
    >>> details = lcsc.get_product_details("C111887")
    >>> details.view()
    ```
    """
    from _impl.api import lcsc
    return lcsc.get_product_details(lcsc_part_number)



def get_search_results(keyword: str, min_stock: int = 500, sort_by: str = "stock"):
    """
    Get search results for a specific search query/keyword.

    By default, the results will be limited to only products with at least `500` in stock, and sorted by the total quantity for sale.

    ## Parameters
    - `keyword` ( *str* ) - The search query.
    - `min_stock` ( *int*, *optional* ) - Limit results to only products with at least the specified quantity. Pass `None` to disable.
    - `sort_by` ( *str*, *optional* ) - Return the list sorted by either quantity in stock (`stock`) or by base-price (`price`).

    ## Example
    ```python
    >>> lcsc = LCSC()
    >>> results = lcsc.get_search_results("L7805CV")
    >>> results = lcsc.get_search_results("L7805CV", min_stock=1000)
    >>> results = lcsc.get_search_results("L7805CV", sort_by="price")
    >>> view(results)
    ```
    """
    from _impl.api import lcsc
    return lcsc.get_search_results(keyword, min_stock, sort_by)

