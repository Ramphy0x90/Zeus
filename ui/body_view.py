from textual.widgets import Static
from textual.app import ComposeResult

class BodyView(Static):
    """Left panel - 1/3 width body display"""
    def compose(self) -> ComposeResult:
        yield Static("[Schematic Area]", id="schematic-canvas") 