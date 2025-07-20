from textual.containers import Horizontal, Vertical
from textual.widgets import Static, DataTable, Button, Input
from textual.app import ComposeResult

class HostingCapacityPage(Vertical):
    """Hosting Capacity analysis page"""
    
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Static("Analysis Parameters", classes="section-title"),
                Static("Penetration Level (%):", classes="param-label"),
                Input(value="20", id="penetration-input"),
                Static("Increment Step (%):", classes="param-label"),
                Input(value="5", id="step-input"),
                Static("Constraints:", classes="subsection-title"),
                Static("• Voltage limits: 0.95 - 1.05 p.u.", classes="constraint"),
                Static("• Thermal limits: 100% of rated capacity", classes="constraint"),
                Static("• Power factor: 0.95 lagging", classes="constraint"),
                classes="hosting-left"
            ),
            Vertical(
                Static("Results", classes="section-title"),
                DataTable(id="hosting-results"),
                Static("Maximum Hosting Capacity: TBD", id="max-capacity"),
                classes="hosting-right"
            ),
            classes="hosting-layout"
        )
    
    def on_mount(self):
        """Initialize hosting capacity results table"""
        results_table = self.query_one("#hosting-results")
        results_table.add_columns("Penetration (%)", "Status", "Limiting Factor", "Capacity (MW)")
        results_table.add_row("0", "Valid", "N/A", "0.0")
        results_table.add_row("5", "Valid", "N/A", "25.0")
        results_table.add_row("10", "Valid", "N/A", "50.0")
        results_table.add_row("15", "Valid", "N/A", "75.0")
        results_table.add_row("20", "Valid", "N/A", "100.0") 