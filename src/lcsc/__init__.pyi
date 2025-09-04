"""
src/lcsc/__init__.pyi

Stub file for the `lcsc` package.
"""
from .types import ProductDetails, SearchResult
__all__ = ["view", "get_product_details", "get_search_results", "__version__", "ProductDetails", "SearchResult"]

def view(data: list | dict) -> None: ...
def get_product_details(script_path: str, lcsc_part_number: str) -> "ProductDetails": ...
def get_search_results(keyword: str, min_stock: int = 500, sort_by: str = "stock") -> list["SearchResult"]: ...
