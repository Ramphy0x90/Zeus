from textual.containers import Horizontal, Vertical
from textual.widgets import Static, DataTable, Button
from textual.app import ComposeResult

class PowerFlowPage(Vertical):
    """Power Flow analysis page"""
    
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Static("Input Parameters", classes="section-title"),
                Static("Bus Data:", classes="subsection-title"),
                DataTable(id="bus-table"),
                Static("Line Data:", classes="subsection-title"),
                DataTable(id="line-table"),
                classes="powerflow-left"
            ),
            Vertical(
                Static("Results", classes="section-title"),
                DataTable(id="results-table"),
                Static("Convergence Status: Ready", id="convergence-status"),
                classes="powerflow-right"
            ),
            classes="powerflow-layout"
        )
    
    def on_mount(self):
        """Initialize tables with sample data"""
        bus_table = self.query_one("#bus-table")
        line_table = self.query_one("#line-table")
        results_table = self.query_one("#results-table")
        
        # Initialize bus table
        bus_table.add_columns("Bus ID", "Type", "P (MW)", "Q (MVAr)", "V (p.u.)")
        bus_table.add_row("1", "Slack", "0.0", "0.0", "1.0")
        bus_table.add_row("2", "PQ", "100.0", "50.0", "1.0")
        
        # Initialize line table
        line_table.add_columns("From", "To", "R (p.u.)", "X (p.u.)", "B (p.u.)")
        line_table.add_row("1", "2", "0.01", "0.1", "0.0")
        
        # Initialize results table
        results_table.add_columns("Bus", "V (p.u.)", "Angle (deg)", "P (MW)", "Q (MVAr)") 