from typing import Any, Optional
from lib.parser.methods import do_parse_method
from lib.ptypes import MethodInfo


def is_syncify_method(name: str, member: object) -> bool:
    try:
        return (
            member.__class__.__name__ == "_SyncWrapper" and
            member.__class__.__module__ == "flyte.syncify._api"
        )
    except (AttributeError, ValueError, KeyError, ImportError):
        return False


def parse_syncify_method(name: str, member: Any) -> Optional[MethodInfo]:
    return do_parse_method(name, member, "syncify")
