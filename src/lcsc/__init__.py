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
__version__ = "1.1.2"




class LCSC:
    """
    """
    def __init__(self) -> None:
        self.__headers = {
            "accept-language": "en-US,en;q=0.9",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }


    def __request(self, url: str, params: dict, method: str = "GET", payload: dict | None = None):
        """
        Private wrapper around `request.request()`.
        """
        import requests
        response = requests.request(method=method, url=url, params=params, headers=self.__headers, data=payload)
        return response


    def get_product_details(self, lcsc_part_number: str):
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
        from .types import ProductDetails
        response = self.__request("https://wmsc.lcsc.com/ftps/wm/product/detail", {
            "productCode": lcsc_part_number,
        })
        raw_data = response.json()["result"]
        return ProductDetails(raw_data)
    

    def get_search_results(self, keyword: str, min_stock: int = 500, sort_by: str = "stock"):
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
        from .types import SearchResult, ProductDetails
        if sort_by.lower() not in ["stock", "price"]:
            print(f"Invalid `sort_by` parameter given.")
            return
        response = self.__request("https://wmsc.lcsc.com/ftps/wm/search/global", {
            "keyword": keyword,
            "currentPage": 1,
            "pageSize": 100,
            "searchType": "product",
        })
        raw_data = response.json()["result"]
        product_list = raw_data["productSearchResultVO"]["productList"]
        results = []
        for i, data in enumerate(product_list):
            product_details = ProductDetails(data)
            if min_stock is None or product_details.stock >= min_stock:
                results.append(SearchResult(i, data["url"], bool(data["isDiscount"]), product_details))
        if sort_by.lower() == "stock":
            results.sort(key=lambda x: x.product_details.stock, reverse=True)
        elif sort_by.lower() == "price":
            results.sort(key=lambda x: x.product_details.price[list(x.product_details.price.keys())[0]].price)
        return results



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
    return LCSC().get_product_details(lcsc_part_number)



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
    return LCSC().get_search_results(keyword, min_stock, sort_by)

