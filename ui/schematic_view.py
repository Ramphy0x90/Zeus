from textual.widgets import Static
from textual.app import ComposeResult

class SchematicView(Static):
    """Right panel - 2/3 width schematic display"""
    def compose(self) -> ComposeResult:
        yield Static("[Schematic Area]", id="schematic-view") 