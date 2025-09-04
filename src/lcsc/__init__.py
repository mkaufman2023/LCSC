"""
src/lcsc/__init__.py

Package-level convenience wrapper.

Allows:
    `import lcsc`
    `lcsc.some_method()`         # forwards to a default LCSC() instance
    `cls = lcsc.LCSC`            # access the class if you want to instantiate yourself
"""
import threading
from __future__ import annotations
from typing import TYPE_CHECKING, Any

__all__ = ["LCSC", "configure", "get_client", "__version__"]
__version__ = "0.0.2"

# Lazy-initialized default client and lock
_default_client = None
_default_client_lock = threading.Lock()

def _create_default_client():
    """Create the default LCSC instance. Import inside function to avoid import cycles."""
    from .api import LCSC
    # construct with no args; change if you need config at import time
    return LCSC()

def _ensure_default_client():
    global _default_client
    if _default_client is None:
        with _default_client_lock:
            if _default_client is None:
                _default_client = _create_default_client()
    return _default_client

# public helpers
def get_client():
    """Return the package's default LCSC instance (creating it if necessary)."""
    return _ensure_default_client()

def configure(*args: Any, **kwargs: Any) -> None:
    """Replace default client with a newly-constructed one using provided args/kwargs.

    Example: lcsc.configure(api_key="...", timeout=10)
    """
    global _default_client
    with _default_client_lock:
        from .api import LCSC
        _default_client = LCSC(*args, **kwargs)

# Delegation: allow attribute access on the package to forward to the default client.
def __getattr__(name: str):
    # expose the class (and any other module-level symbols) by importing them explicitly
    if name == "LCSC":
        from .api import LCSC
        return LCSC

    # delegate everything else to the client instance
    client = _ensure_default_client()
    try:
        return getattr(client, name)
    except AttributeError as exc:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from exc

def __dir__():
    # include module attributes plus the client's attributes for tab-completion
    attrs = set(globals().keys())
    try:
        client = _ensure_default_client()
        attrs.update(dir(client))
    except Exception:
        # if client creation fails at dir-time, ignore and return module attrs only
        pass
    return sorted(attrs)