"""
src/lcsc/__init__.py

Package-level convenience wrapper.
"""
__all__ = ["lcsc", "__version__"]
__version__ = "0.0.5"



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
    from .api import lcsc
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
    from .api import lcsc
    return lcsc.get_search_results(keyword, min_stock, sort_by)

