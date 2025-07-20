from textual.containers import Horizontal, Vertical
from textual.widgets import Static, TextArea, Button
from textual.app import ComposeResult

class EditorPage(Vertical):
    """Editor page for grid configuration"""
    
    def compose(self) -> ComposeResult:
        yield Static("Editor Page")