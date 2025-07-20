from textual.containers import Vertical
from textual.widgets import Static
from textual.app import ComposeResult
from textual.message import Message

from ui.components.navigation import Navigation
from ui.pages.editor_page import EditorPage
from ui.pages.hosting_capacity_page import HostingCapacityPage
from ui.pages.powerflow_page import PowerFlowPage

class BodyView(Static):
    """Left panel - 1/3 width body display"""
    
    class PageChangeRequest(Message):
        """Message to request page change in BodyView"""
        def __init__(self, page_name: str):
            self.page_name = page_name
            super().__init__()
    
    def compose(self) -> ComposeResult:
        yield Vertical(
            EditorPage(id="editor-page", classes="page active"),
            PowerFlowPage(id="powerflow-page", classes="page"),
            HostingCapacityPage(id="hosting-page", classes="page"),
            id="page-container"
        )

    def on_body_view_page_change_request(self, event: PageChangeRequest):
        """Handle page change requests"""
        self.action_switch_page(event.page_name)

    def action_switch_page(self, page_name: str):
        """Switch to a different page"""
        # Hide all pages
        for page in self.query(".page"):
            page.remove_class("active")
        
        # Show selected page
        target_page = self.query_one(f"#{page_name}-page")
        if target_page:
            target_page.add_class("active")