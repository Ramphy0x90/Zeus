from textual.containers import Vertical
from textual.widgets import Static, TabPane, TabbedContent, TextArea, Input, DataTable
from textual.app import ComposeResult

class EditorPage(Vertical):
    """Editor page for grid configuration"""
    
    def compose(self) -> ComposeResult:     
        with Vertical(classes="editor-page-layout"):
            # Grid information section
            yield Vertical(
                    Static("Grid Information", classes="section-title"),
                    Static("Name:", classes="input-label"),
                    Input(placeholder="Enter grid name...", id="grid-name"),
                    Static("Description:", classes="input-label"),
                    TextArea("", id="grid-description"),
                    classes="grid-info-section"
                )

            # Grid elements section
            with Vertical(): 
                Static("Grid Elements", classes="section-title")
                with TabbedContent(initial="buses"):
                    with TabPane("Buses", id="buses"):
                        yield DataTable(id="buses-table")
                    with TabPane("Branches", id="branches"):
                        yield DataTable(id="branches-table")
                    with TabPane("Transformers", id="transformers"):
                        yield Static("Transformers", classes="subsection-title")
        
    
    def on_mount(self):
        """Initialize the editor with sample data"""
        self.initialize_tables()
    
    def initialize_tables(self):
        """Initialize all tables with sample data"""
        # Initialize Buses table
        buses_table = self.query_one("#buses-table")
        if buses_table:
            buses_table.add_columns("ID", "Name", "Type", "V (p.u.)", "Angle (deg)", "P (MW)", "Q (MVAr)")
            buses_table.add_row("1", "Slack Bus", "Slack", "1.0", "0.0", "0.0", "0.0")
            buses_table.add_row("2", "Load Bus 1", "PQ", "1.0", "0.0", "100.0", "50.0")
            buses_table.add_row("3", "Load Bus 2", "PQ", "1.0", "0.0", "80.0", "40.0")
        
        # Initialize Branches table
        branches_table = self.query_one("#branches-table")
        if branches_table:
            branches_table.add_columns("From", "To", "R (p.u.)", "X (p.u.)", "B (p.u.)", "Rating (MVA)")
            branches_table.add_row("1", "2", "0.01", "0.1", "0.0", "100.0")
            branches_table.add_row("2", "3", "0.02", "0.15", "0.0", "80.0")

    
    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab