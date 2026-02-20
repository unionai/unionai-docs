from typing import Optional, Any
import inspect

from lib.ptypes import MethodInfo
from lib.parser.methods import do_parse_method

PROCESS_CALLABLES = [
    "flyte.map",
]


def is_callable(name: str, member: Any, parent_name: str) -> bool:
    """Check if a member is a callable object (i.e., has a __call__ method)."""
    # Check allowlist first to avoid triggering __getattr__ on objects that
    # raise exceptions (e.g., flytekit context manager objects).
    if f"{parent_name}.{name}" not in PROCESS_CALLABLES:
        return False
    try:
        return hasattr(member, "__call__")
    except Exception:
        return False

def parse_callable(name: str, member: Any, parent_name: str = None) -> Optional[MethodInfo]:
    """Parse a callable member and extract its information."""
    if not is_callable(name, member, parent_name):
        return None

    call_method = getattr(member, '__call__')

    return do_parse_method(name, call_method, "syncify", parent_name=parent_name)
