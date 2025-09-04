"""
src/lcsc/types.py

Dataclass types for the `lcsc` package.
"""
from dataclasses import (
    field as _field,
    asdict as _asdict,
    astuple as _astuple,
    dataclass as _dataclass
)
from pyjsonviewer import view_data as _view



@_dataclass(frozen=True)
class CatalogDetails:
    """
    """
    id: int
    name: str

    def as_dict(self):
        return _asdict(self)
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())



@_dataclass(frozen=True)
class BrandDetails:
    """
    """
    id: int
    name: str

    def as_dict(self):
        return _asdict(self)
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())
    


@_dataclass(frozen=True)
class PriceDetails:
    """
    """
    quantity: int
    price: float
    discount: float
    discount_pct: float

    def as_dict(self):
        return _asdict(self)
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())



@_dataclass(frozen=True)
class Spec:
    """
    """
    name: str
    code: str
    value: str

    def as_dict(self):
        return _asdict(self)
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())



@_dataclass(frozen=True)
class ProductDetails:
    """
    """
    __raw_data: dict = _field(default_factory=dict)
    
    product_id: int = _field(init=False)
    product_code: str = _field(init=False)
    product_url: str = _field(init=False)
    product_model: str = _field(init=False)
    product_title: str = _field(init=False)
    parent_catalog: "CatalogDetails" = _field(init=False)
    catalog: "CatalogDetails" = _field(init=False)
    brand: "BrandDetails" = _field(init=False)
    split_quantity: int = _field(init=False)
    min_quantity: int = _field(init=False)
    is_hot: bool = _field(init=False)
    stock: int = _field(init=False)
    price: dict[int, "PriceDetails"] = _field(init=False, default_factory=dict)
    image_urls: list[str] = _field(init=False, default_factory=list)
    datasheet_url: str = _field(init=False)
    description: str = _field(init=False)
    specs: list["Spec"] = _field(init=False, default_factory=list)

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
        d = _asdict(self)
        k = [x for x in d.keys() if x.find('__raw_data') != -1]
        if len(k) > 0:
            d.pop(k[0])
        return d
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())

    def view_raw(self):
        _view(json_data=self.__raw_data)

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



@_dataclass(frozen=True)
class SearchResult:
    """
    """
    index: int
    product_url: str
    on_discount: bool
    product_details: "ProductDetails"

    def as_dict(self):
        d = _asdict(self)
        k = [x for x in d["product_details"].keys() if x.find('__raw_data') != -1]
        if len(k) > 0:
            d["product_details"].pop(k[0])
        return d

    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=self.as_dict())



@_dataclass(frozen=True)
class SearchResults:
    """
    """
    results: list["SearchResult"] = _field(default_factory=list)

    def as_dict(self):
        d = _asdict(self)
        return _asdict(self)
    
    def as_tuple(self):
        return _astuple(self)
    
    def view(self):
        _view(json_data=[x.as_dict() for x in self.results])