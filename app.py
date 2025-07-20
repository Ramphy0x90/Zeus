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
                yield Vertical(
                    EditorPage(id="editor-page", classes="page active"),
                    PowerFlowPage(id="powerflow-page", classes="page"),
                    HostingCapacityPage(id="hosting-page", classes="page"),
                    id="page-container"
                )
            with Vertical(classes="grid-viewer"):
                yield SchematicView()

        yield Footer()

    def on_navigation_page_changed(self, event: Navigation.PageChanged):
        """Handle navigation page changes"""
        self.sub_title = event.page_name
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

    def on_select_changed(self, event: Select.Changed):
        """Handle grid selection changes"""
        if event.select.id == "grid-select":
            selected_grid = event.value
            # self.notify(f"Selected grid: {selected_grid}")

if __name__ == "__main__":
    app = ZeusApp()
    app.run()