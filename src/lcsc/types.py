"""
src/lcsc/types.py

Class objects/types for the `lcsc` package.
"""



class CatalogDetails:
    """
    Catalog details for a product.
    """
    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name
    
    @property
    def id(self) -> int:
        """
        The catalog's unique ID.
        """
        return self._id
    
    @property
    def name(self) -> str:
        """
        The catalog's name.
        """
        return self._name

    def as_dict(self) -> dict[str, int | str]:
        """
        Returns the catalog details as a dictionary.

        ## Keys
        - `id` ( *int* ) - The catalog's unique ID.
        - `name` ( *str* ) - The catalog's name.
        """
        return {"id": self.id, "name": self.name}
    
    def as_tuple(self) -> tuple[int, str]:
        """
        Returns the catalog details as a tuple.

        ## Elements
        - `0` ( *int* ) - The catalog's unique ID.
        - `1` ( *str* ) - The catalog's name.
        """
        return (self.id, self.name)
    
    def view(self) -> None:
        """
        Views the catalog details in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())



class BrandDetails:
    """
    Brand details for a product.
    """
    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name
    
    @property
    def id(self) -> int:
        """
        The brand's unique ID.
        """
        return self._id
    
    @property
    def name(self) -> str:
        """
        The brand's name.
        """
        return self._name

    def as_dict(self) -> dict[str, int | str]:
        """
        Returns the brand details as a dictionary.

        ## Keys
        - `id` ( *int* ) - The brand's unique ID.
        - `name` ( *str* ) - The brand's name.
        """
        return {"id": self.id, "name": self.name}
    
    def as_tuple(self) -> tuple[int, str]:
        """
        Returns the brand details as a tuple.

        ## Elements
        - `0` ( *int* ) - The brand's unique ID.
        - `1` ( *str* ) - The brand's name.
        """
        return (self.id, self.name)
    
    def view(self) -> None:
        """
        Views the brand details in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())



class PriceDetails:
    """
    Price details for a product.
    """
    def __init__(self, quantity: int, price: float, discount: float, discount_pct: float) -> None:
        self._quantity = quantity
        self._price = price
        self._discount = discount
        self._discount_pct = discount_pct
    
    @property
    def quantity(self) -> int:
        """
        The quantity required to get this price.
        """
        return self._quantity
    
    @property
    def price(self) -> float:
        """
        The price for the specified quantity, in USD.
        """
        return self._price
    
    @property
    def discount(self) -> float:
        """
        The discount amount, in USD, as measured from the base price (i.e. minimum quantity price).
        """
        return self._discount
    
    @property
    def discount_pct(self) -> float:
        """
        The discount percentage, as measured from the base price (i.e. minimum quantity price).
        """
        return self._discount_pct

    def as_dict(self) -> dict[str, int | float]:
        """
        Returns the price details as a dictionary.

        ## Keys
        - `quantity` ( *int* ) - The quantity required to get this price.
        - `price` ( *float* ) - The price for the specified quantity, in USD.
        - `discount` ( *float* ) - The discount amount, in USD, as measured from the base price (i.e. minimum quantity price).
        - `discount_pct` ( *float* ) - The discount percentage, as measured from the base price (i.e. minimum quantity price).
        """
        return {
            "quantity": self.quantity,
            "price": self.price,
            "discount": self.discount,
            "discount_pct": self.discount_pct,
        }
    
    def as_tuple(self) -> tuple[int, float, float, float]:
        """
        Returns the price details as a tuple.

        ## Elements
        - `0` ( *int* ) - The quantity required to get this price.
        - `1` ( *float* ) - The price for the specified quantity, in USD.
        - `2` ( *float* ) - The discount amount, in USD, as measured from the base price (i.e. minimum quantity price).
        - `3` ( *float* ) - The discount percentage, as measured from the base price (i.e. minimum quantity price).
        """
        return (self.quantity, self.price, self.discount, self.discount_pct)
    
    def view(self) -> None:
        """
        Views the price details in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())



class Spec:
    """
    Specification detail for a product.
    """
    def __init__(self, name: str, code: str, value: str) -> None:
        self._name = name
        self._code = code
        self._value = value
    
    @property
    def name(self) -> str:
        """
        The specification's name.
        """
        return self._name
    
    @property
    def code(self) -> str:
        """
        The specification's code.
        """
        return self._code
    
    @property
    def value(self) -> str:
        """
        The specification's value.
        """
        return self._value

    def as_dict(self) -> dict[str, str]:
        """
        Returns the specification detail as a dictionary.

        ## Keys
        - `name` ( *str* ) - The specification's name.
        - `code` ( *str* ) - The specification's code.
        - `value` ( *str* ) - The specification's value.
        """
        return {
            "name": self.name,
            "code": self.code,
            "value": self.value,
        }
    
    def as_tuple(self) -> tuple[str, str, str]:
        """
        Returns the specification detail as a tuple.

        ## Elements
        - `0` ( *str* ) - The specification's name.
        - `1` ( *str* ) - The specification's code.
        - `2` ( *str* ) - The specification's value.
        """
        return (self.name, self.code, self.value)
    
    def view(self) -> None:
        """
        Views the specification detail in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())



class ProductDetails:
    """
    Details for a product.
    """
    def __init__(self, raw_data: dict) -> None:
        self.__raw_data = raw_data
        self._product_id =     int(self.__raw_data["productId"])
        self._product_code =   self.__raw_data["productCode"]
        self._product_url =    f"https://www.lcsc.com/product-detail/{self.__raw_data['productCode']}.html"
        self._product_model =  self.__raw_data["productModel"]
        self._product_title =  self.__raw_data["title"]
        self._parent_catalog = CatalogDetails(int(self.__raw_data["parentCatalogId"]), self.__raw_data["parentCatalogName"])
        self._catalog =        CatalogDetails(int(self.__raw_data["catalogId"]), self.__raw_data["catalogName"])
        self._brand =          BrandDetails(int(self.__raw_data["brandId"]), self.__raw_data["brandNameEn"])
        self._split_quantity = int(self.__raw_data["split"])
        self._min_quantity =   int(self.__raw_data["minBuyNumber"])
        self._is_hot =         bool(self.__raw_data["isHot"])
        self._stock =          int(self.__raw_data["stockNumber"])
        
        price_details: dict[int, PriceDetails] = {}
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
        self._price = price_details
        
        self._image_urls =     self.__raw_data["productImages"]
        self._datasheet_url =  self.__raw_data["pdfUrl"]
        self._description =    self.__raw_data["productIntroEn"]
        
        specs_list = []
        for p in self.__raw_data["paramVOList"]:
            name = str(p["paramNameEn"])
            code = str(p["paramCode"])
            value = str(p["paramValueEn"])
            specs_list.append(Spec(name, code, value))
        self._specs: list["Spec"] = specs_list

    def __hash__(self):
        """
        Allows using `ProductDetails` as dictionary keys and in sets.
        """
        return hash(self._product_code)
    
    @property
    def product_id(self) -> int:
        """
        The product's unique ID (e.g. `113118`).
        """
        return self._product_id
    
    @property
    def product_code(self) -> str:
        """
        The product's LCSC part number/code (e.g. `C111887`).
        """
        return self._product_code
    
    @property
    def product_url(self) -> str:
        """
        The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        """
        return self._product_url
    
    @property
    def product_model(self) -> str:
        """
        The product's model number (e.g. `L7805CV`).
        """
        return self._product_model
    
    @property
    def product_title(self) -> str:
        """
        The product's title, as it appears on LCSC's website (e.g. `ST L7805CV`).
        """
        return self._product_title
    
    @property
    def parent_catalog(self) -> CatalogDetails:
        """
        The product's parent catalog details (see: [`CatalogDetails`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L9)).
        """
        return self._parent_catalog
    
    @property
    def catalog(self) -> CatalogDetails:
        """
        The product's catalog details (see: [`CatalogDetails`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L9)).
        """
        return self._catalog
    
    @property
    def brand(self) -> BrandDetails:
        """
        The product's brand details (see: [`BrandDetails`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L60)).
        """
        return self._brand
    
    @property
    def split_quantity(self) -> int:
        """
        The product's split quantity (i.e. order in multiples of this quantity).
        """
        return self._split_quantity
    
    @property
    def min_quantity(self) -> int:
        """
        The minimum order quantity for the product.
        """
        return self._min_quantity
    
    @property
    def is_hot(self) -> bool:
        """
        Whether the product is marked as a "hot" item on LCSC's website.
        """
        return self._is_hot
    
    @property
    def stock(self) -> int:
        """
        The quantity of the product currently in stock.
        """
        return self._stock
    
    @property
    def price(self) -> dict[int, PriceDetails]:
        """
        A dictionary mapping quantity breakpoints to their corresponding price details (see: [`PriceDetails`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L111)).
        """
        return self._price
    
    @property
    def image_urls(self) -> list[str]:
        """
        A list of URLs pointing to images of the product.
        """
        return self._image_urls
    
    @property
    def datasheet_url(self) -> str:
        """
        The URL pointing to the product's datasheet, if available (e.g. https://www.lcsc.com/datasheet/C3795.pdf).
        """
        return self._datasheet_url
    
    @property
    def description(self) -> str:
        """
        The product's description, as it appears on LCSC's website (e.g. `62dB@(120Hz) 1.5A Fixed 5V Positive 25V TO-220 Voltage Regulators - Linear, Low Drop Out (LDO) Regulators ROHS`).
        """
        return self._description
    
    @property
    def specs(self) -> list["Spec"]:
        """
        A list of the product's specifications (see: [`Spec`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L187)).
        """
        return self._specs
    
    def as_dict(self) -> dict[str, int | str | bool | dict | list]:
        """
        Returns the product details as a dictionary.

        ## Keys
        - `product_id` ( *int* ) - The product's unique ID (e.g. `113118`).
        - `product_code` ( *str* ) - The product's LCSC part number/code (e.g. `C111887`).
        - `product_url` ( *str* ) - The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        - `product_model` ( *str* ) - The product's model number (e.g. `L7805CV`).
        - `product_title` ( *str* ) - The product's title, as it appears on LCSC's website (e.g. `ST L7805CV`).
        - `parent_catalog` ( *dict* ) - The product's parent catalog details, as a dictionary.
        - `catalog` ( *dict* ) - The product's catalog details, as a dictionary.
        - `brand` ( *dict* ) - The product's brand details, as a dictionary.
        - `split_quantity` ( *int* ) - The product's split quantity (i.e. order in multiples of this quantity).
        - `min_quantity` ( *int* ) - The minimum order quantity for the product.
        - `is_hot` ( *bool* ) - Whether the product is marked as a "hot" item on LCSC's website.
        - `stock` ( *int* ) - The quantity of the product currently in stock.
        - `price` ( *dict[int, dict]* ) - A dictionary mapping quantity breakpoints to their corresponding price details.
        - `image_urls` ( *list[str]* ) - A list of URLs pointing to images of the product.
        - `datasheet_url` ( *str* ) - The URL pointing to the product's datasheet, if available.
        - `description` ( *str* ) - The product's description, as it appears on LCSC's website.
        - `specs` ( *list[dict]* ) - A list of the product's specifications.
        """
        return {
            "product_id": self._product_id,
            "product_code": self._product_code,
            "product_url": self._product_url,
            "product_model": self._product_model,
            "product_title": self._product_title,
            "parent_catalog": self._parent_catalog.as_dict(),
            "catalog": self._catalog.as_dict(),
            "brand": self._brand.as_dict(),
            "split_quantity": self._split_quantity,
            "min_quantity": self._min_quantity,
            "is_hot": self._is_hot,
            "stock": self._stock,
            "price": {k: v.as_dict() for k, v in self._price.items()},
            "image_urls": self._image_urls,
            "datasheet_url": self._datasheet_url,
            "description": self._description,
            "specs": [s.as_dict() for s in self._specs],
        }
    
    def as_tuple(self) -> tuple[int, str, str, str, str, tuple[int, str], tuple[int, str], tuple[int, str], int, int, bool, int, tuple[tuple[int, tuple[int, float, float, float]], ...], tuple[str], str, str, tuple[tuple[str, str, str], ...]]:
        """
        Returns the product details as a tuple.

        ## Elements
        - `0` / `product_id` ( *int* ) - The product's unique ID (e.g. `113118`).
        - `1` / `product_code` ( *str* ) - The product's LCSC part number/code (e.g. `C111887`).
        - `2` / `product_url` ( *str* ) - The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        - `3` / `product_model` ( *str* ) - The product's model number (e.g. `L7805CV`).
        - `4` / `product_title` ( *str* ) - The product's title, as it appears on LCSC's website (e.g. `ST L7805CV`).
        - `5` / `parent_catalog` ( *tuple* ) - The product's parent catalog details, as a tuple.
        - `6` / `catalog` ( *tuple* ) - The product's catalog details, as a tuple.
        - `7` / `brand` ( *tuple* ) - The product's brand details, as a tuple.
        - `8` / `split_quantity` ( *int* ) - The product's split quantity (i.e. order in multiples of this quantity).
        - `9` / `min_quantity` ( *int* ) - The minimum order quantity for the product.
        - `10` / `is_hot` ( *bool* ) - Whether the product is marked as a "hot" item on LCSC's website.
        - `11` / `stock` ( *int* ) - The quantity of the product currently in stock.
        - `12` / `price` ( *tuple* ) - A tuple of tuples, each containing a quantity breakpoint and its corresponding price details as a tuple.
        - `13` / `image_urls` ( *tuple* ) - A tuple of URLs pointing to images of the product.
        - `14` / `datasheet_url` ( *str* ) - The URL pointing to the product's datasheet, if available.
        - `15` / `description` ( *str* ) - The product's description, as it appears on LCSC's website.
        - `16` / `specs` ( *tuple* ) - A tuple of the product's specifications, each as a tuple.
        """
        return (
            self._product_id,
            self._product_code,
            self._product_url,
            self._product_model,
            self._product_title,
            self._parent_catalog.as_tuple(),
            self._catalog.as_tuple(),
            self._brand.as_tuple(),
            self._split_quantity,
            self._min_quantity,
            self._is_hot,
            self._stock,
            tuple((k, v.as_tuple()) for k, v in self._price.items()),
            tuple(self._image_urls),
            self._datasheet_url,
            self._description,
            tuple(s.as_tuple() for s in self._specs),
        )
    
    def view(self) -> None:
        """
        Views the product details in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())

    def view_raw(self) -> None:
        """
        Views the raw product details data in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.__raw_data)

    def get_price_breaks(self) -> list[int]:
        """
        Gets the quantity breakpoints for the product's pricing.

        ## Returns
        - `price_breaks` ( *list[int]* ) - A sorted list of the quantity breakpoints.
        """
        return sorted(self.price.keys())
    
    def get_order_cost(self, quantity: int) -> float:
        """
        Calculates the total cost to order a specific quantity of the product.

        ## Parameters
        - `quantity` ( *int* ) - The quantity to order.

        ## Returns
        - `total_cost` ( *float* ) - The total cost.
        """
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



class SearchResult:
    """
    Details for a search result item.
    """
    def __init__(self, index: int, product_url: str, on_discount: bool, product_details: ProductDetails) -> None:
        self._index = index
        self._product_url = product_url
        self._on_discount = on_discount
        self._product_details = product_details
    
    @property
    def index(self) -> int:
        """
        The search result's index in the overall search results (0-based).
        """
        return self._index
    
    @property
    def product_url(self) -> str:
        """
        The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        """
        return self._product_url
    
    @property
    def on_discount(self) -> bool:
        """
        Whether the product is currently on discount.
        """
        return self._on_discount
    
    @property
    def product_details(self) -> ProductDetails:
        """
        The product's details (see: [`ProductDetails`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L252)).
        """
        return self._product_details

    def as_dict(self) -> dict[str, int | str | bool | dict]:
        """
        Returns the search result details as a dictionary.

        ## Keys
        - `index` ( *int* ) - The search result's index in the overall search results (0-based).
        - `product_url` ( *str* ) - The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        - `on_discount` ( *bool* ) - Whether the product is currently on discount.
        - `product_details` ( *dict* ) - The product's details, as a dictionary.
        """
        return {
            "index": self.index,
            "product_url": self.product_url,
            "on_discount": self.on_discount,
            "product_details": self.product_details.as_dict(),
        }

    def as_tuple(self) -> tuple[int, str, bool, tuple]:
        """
        Returns the search result details as a tuple.

        ## Elements
        - `0` / `index` ( *int* ) - The search result's index in the overall search results (0-based).
        - `1` / `product_url` ( *str* ) - The URL pointing to the product on LCSC's website (e.g. `www.lcsc.com/product-detail/C111887.html"`).
        - `2` / `on_discount` ( *bool* ) - Whether the product is currently on discount.
        - `3` / `product_details` ( *tuple* ) - The product's details, as a tuple.
        """
        return (
            self.index,
            self.product_url,
            self.on_discount,
            self.product_details.as_tuple(),
        )
    
    def view(self) -> None:
        """
        Views the search result details in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=self.as_dict())



class SearchResults:
    """
    A collection of search result items.
    """
    def __init__(self, results: list["SearchResult"] = None) -> None:
        if results is None:
            results = []
        self._results = results
    
    @property
    def results(self) -> list["SearchResult"]:
        """
        The list of search result items (see: [`SearchResult`](https://github.com/mkaufman2023/LCSC/blob/main/src/lcsc/types.py#L555)).
        """
        return self._results

    def as_dict(self) -> list[dict[str, int | str | bool | dict]]:
        """
        Returns the search results as a list of dictionaries.

        ## Returns
        - `results` ( *list[dict]* ) - A list of the search result items, each as a dictionary.
        """
        return [r.as_dict() for r in self._results]
    
    def as_tuple(self) -> tuple[tuple[int, str, bool, tuple]]:
        """
        Returns the search results as a tuple of tuples.

        ## Returns
        - `results` ( *tuple[tuple]* ) - A tuple of the search result items, each as a tuple.
        """
        return tuple(r.as_tuple() for r in self._results)
    
    def view(self) -> None:
        """
        Views the search results in a GUI window.
        """
        from pyjsonviewer import view_data as _view
        _view(json_data=[x.as_dict() for x in self.results])
