"""Shared rich console of the package."""

from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
    {
        "success": "green",
        "info": "blue",
        "warning": "orange3",
        "error": "red",
    }
)

console = Console(record=True, theme=custom_theme)
