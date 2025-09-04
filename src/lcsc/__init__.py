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
__version__ = "1.0.4"
from dataclasses import dataclass, field, asdict, astuple


@dataclass(frozen=True)
class CatalogDetails:
    """
    """
    id: int
    name: str

    def as_dict(self):
        return asdict(self)
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())



@dataclass(frozen=True)
class BrandDetails:
    """
    """
    id: int
    name: str

    def as_dict(self):
        return asdict(self)
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())
    


@dataclass(frozen=True)
class PriceDetails:
    """
    """
    quantity: int
    price: float
    discount: float
    discount_pct: float

    def as_dict(self):
        return asdict(self)
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())



@dataclass(frozen=True)
class Spec:
    """
    """
    name: str
    code: str
    value: str

    def as_dict(self):
        return asdict(self)
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())



@dataclass(frozen=True)
class ProductDetails:
    """
    """
    __raw_data: dict = field(default_factory=dict)
    
    product_id: int = field(init=False)
    product_code: str = field(init=False)
    product_url: str = field(init=False)
    product_model: str = field(init=False)
    product_title: str = field(init=False)
    parent_catalog: "CatalogDetails" = field(init=False)
    catalog: "CatalogDetails" = field(init=False)
    brand: "BrandDetails" = field(init=False)
    split_quantity: int = field(init=False)
    min_quantity: int = field(init=False)
    is_hot: bool = field(init=False)
    stock: int = field(init=False)
    price: dict[int, "PriceDetails"] = field(init=False, default_factory=dict)
    image_urls: list[str] = field(init=False, default_factory=list)
    datasheet_url: str = field(init=False)
    description: str = field(init=False)
    specs: list["Spec"] = field(init=False, default_factory=list)
    # optimal_order_quantity: int = field(init=False, default=0)

    def __post_init__(self):
        super().__setattr__("product_id",     int(self.__raw_data["productId"]))
        super().__setattr__("product_code",   self.__raw_data["productCode"])
        super().__setattr__("product_url",    f"https://www.lcsc.com/product-detail/{self.__raw_data["productCode"]}.html")
        super().__setattr__("product_model",  self.__raw_data["productModel"])
        super().__setattr__("product_title",  self.__raw_data["title"])
        super().__setattr__("parent_catalog", CatalogDetails(int(self.__raw_data["parentCatalogId"]), self.__raw_data["parentCatalogName"]))
        super().__setattr__("catalog",        CatalogDetails(int(self.__raw_data["catalogId"]), self.__raw_data["catalogName"]))
        super().__setattr__("brand",          BrandDetails(int(self.__raw_data["brandId"]), self.__raw_data["brandNameEn"]))
        super().__setattr__("split_quantity", int(self.__raw_data["split"]))
        super().__setattr__("min_quantity",   int(self.__raw_data["minBuyNumber"]))
        super().__setattr__("is_hot",         bool(self.__raw_data["isHot"]))
        super().__setattr__("stock",          int(self.__raw_data["stockNumber"]))
        super().__setattr__("image_urls",     self.__raw_data["productImages"])
        super().__setattr__("datasheet_url",  self.__raw_data["pdfUrl"])
        super().__setattr__("description",    self.__raw_data["productIntroEn"])
        price_details: dict[int, "PriceDetails"] = {}
        for i, p in enumerate(self.__raw_data["productPriceList"]):
            ladder = int(p["ladder"])
            price = float(p["usdPrice"])
            discount = 0
            discount_percent = 0
            if i > 0:
                first_price = float(self.__raw_data["productPriceList"][0]["usdPrice"])
                discount = first_price - price
                discount_percent = 100 * abs((price - first_price) / first_price)
            price_details[ladder] = PriceDetails(ladder, price, discount, discount_percent)
        specs_list = []
        for p in self.__raw_data["paramVOList"]:
            name = str(p["paramNameEn"])
            code = str(p["paramCode"])
            value = str(p["paramValueEn"])
            specs_list.append(Spec(name, code, value))
        super().__setattr__("price", price_details)
        super().__setattr__("specs", specs_list)

    def __hash__(self):
        """
        Allows using `ProductDetails` as dictionary keys and in sets.
        """
        return hash(self.product_code)
    
    def as_dict(self):
        d = asdict(self)
        k = [x for x in d.keys() if x.find('__raw_data') != -1]
        if len(k) > 0:
            d.pop(k[0])
        return d
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())

    def view_raw(self):
        view(self.__raw_data)

    def get_price_breaks(self) -> list[int]:
        return sorted(self.price.keys())
    
    def get_order_cost(self, quantity: int) -> float:
        if quantity < self.min_quantity:
            raise ValueError(f"Quantity {quantity} is less than minimum order quantity of {self.min_quantity}.")
        if quantity % self.split_quantity != 0:
            raise ValueError(f"Quantity {quantity} is not a multiple of split quantity of {self.split_quantity}.")
        ladders = sorted(self.price.keys())
        applicable_ladder = ladders[0]
        for ladder in ladders:
            if quantity >= ladder:
                applicable_ladder = ladder
            else:
                break
        return self.price[applicable_ladder].price * quantity



@dataclass(frozen=True)
class SearchResult:
    """
    """
    index: int
    product_url: str
    on_discount: bool
    product_details: "ProductDetails"

    def as_dict(self):
        d = asdict(self)
        k = [x for x in d["product_details"].keys() if x.find('__raw_data') != -1]
        if len(k) > 0:
            d["product_details"].pop(k[0])
        return d

    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view(self.as_dict())



@dataclass(frozen=True)
class SearchResults:
    """
    """
    results: list["SearchResult"] = field(default_factory=list)

    def as_dict(self):
        d = asdict(self)
        return asdict(self)
    
    def as_tuple(self):
        return astuple(self)
    
    def view(self):
        view([x.as_dict() for x in self.results])



class LCSC:
    """
    """
    def __init__(self) -> None:
        self.__headers = {
            "accept-language": "en-US,en;q=0.9",
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }
        self.__base_url = "https://wmsc.lcsc.com/ftps/wm/"


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

