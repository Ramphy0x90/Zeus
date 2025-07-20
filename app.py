from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Select, Static
from ui.components.navigation import Navigation
from ui.body_view import BodyView
from ui.pages.editor_page import EditorPage
from ui.pages.powerflow_page import PowerFlowPage
from ui.pages.hosting_capacity_page import HostingCapacityPage
from ui.schematic_view import SchematicView

class ZeusApp(App):
    CSS_PATH = "./ui/styles.css"
    
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def on_mount(self) -> None:
        self.theme = "flexoki"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Navigation()
        
        with Horizontal(classes="app-wrapper"):
            with Vertical(classes="app-body"):
                yield BodyView()
            with Vertical(classes="grid-viewer"):
                yield SchematicView()

        yield Footer()

    def on_navigation_page_changed(self, event: Navigation.PageChanged):
        """Handle navigation page changes and forward to BodyView"""
        # Forward the message to the BodyView component
        body_view = self.query_one("BodyView")
        if body_view:
            body_view.post_message(BodyView.PageChangeRequest(event.page_name))

if __name__ == "__main__":
    app = ZeusApp()
    app.run()