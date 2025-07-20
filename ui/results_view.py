from textual.containers import Vertical
from textual.widgets import DataTable, Static
from textual.app import ComposeResult

class ResultsView(Vertical):
    """Left panel - 1/3 width results/navigation"""
    def compose(self) -> ComposeResult:
        self.table = DataTable(id="results-table")
        yield self.table
        yield Static("Navigation", id="nav-commands")

    def on_mount(self):
        # Example: Add columns and rows for power flow results
        self.table.add_columns("Bus", "Voltage (p.u.)", "Angle (deg)")
        self.table.add_row("Bus 1", "1.00", "0.0")
        self.table.add_row("Bus 2", "0.98", "-2.3") 