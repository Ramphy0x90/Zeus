from textual.containers import Horizontal
from textual.widgets import Button, Static
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.message import Message

class Navigation(Static):
    """Horizontal navigation menu"""
    
    current_page = reactive("Editor")
    
    def compose(self) -> ComposeResult:
        yield Button("Editor", id="nav-editor", classes="nav-item active")
        yield Button("Power Flow", id="nav-powerflow", classes="nav-item")
        yield Button("Hosting Capacity", id="nav-hosting", classes="nav-item")
    
    def on_mount(self):
        """Called when the navigation is mounted"""
        self.log.info("Navigation mounted")
    
    def on_button_pressed(self, event):
        """Handle navigation button clicks"""
        self.log.info(f"Navigation button pressed: {event.button.id}")
        clicked_id = event.button.id
        if clicked_id and clicked_id.startswith("nav-"):
            # Extract page name from id (e.g., "nav-editor" -> "editor")
            page_name = clicked_id.replace("nav-", "")
            self.log.info(f"Switching to page: {page_name}")
            self.switch_page(page_name)
    
    def switch_page(self, page_name: str):
        """Switch to a different page"""
        self.log.info(f"switch_page called with: {page_name}")
        # Update active state
        for nav_item in self.query(".nav-item"):
            nav_item.remove_class("active")
        
        # Add active class to clicked item
        clicked_item = self.query_one(f"#nav-{page_name}")
        if clicked_item:
            clicked_item.add_class("active")
            self.current_page = page_name.title()
            # Notify parent about page change
            self.log.info(f"Posting PageChanged message: {page_name}")
            self.post_message(self.PageChanged(page_name))
        else:
            self.log.error(f"Could not find nav item with id: nav-{page_name}")
    
    class PageChanged(Message):
        """Message sent when page changes"""
        def __init__(self, page_name: str):
            self.page_name = page_name
            super().__init__() 