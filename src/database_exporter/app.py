import wx
import wx.grid
import configparser
from pathlib import Path
from .db_manager import DatabaseManager

# Ez a fájl az alkalmazás grafikus felületét és működését tartalmazza.
# Az alkalmazás beolvassa a konfigurációs fájlt, csatlakozik egy adatbázishoz,
# és megjeleníti az adatbázis tábláit egy táblázatos formában, ahol a felhasználó kiválaszthatja a menteni kívánt táblákat.
class DatabaseExporterFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Database Exporter')
        self.config = configparser.ConfigParser()
        if not self.config.read('config.ini') or not self.config.has_section('database'):
            wx.MessageBox('Configuration file (config.ini) is missing or invalid.', 'Error', wx.OK | wx.ICON_ERROR)
            self.Destroy()
            return

        db_config = self.config['database']

        self.db_manager = DatabaseManager(
            db_config.get('host'),
            db_config.get('user'),
            db_config.get('password'),
            db_config.get('database')
        )
        if not self.db_manager.connect():
            wx.MessageBox('Failed to connect to the database.', 'Error', wx.OK | wx.ICON_ERROR)
            self.Destroy()
            return

        self.tables = self.db_manager.get_tables()

        self.UI()

    def UI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.grid = wx.grid.Grid(panel)
        self.grid.CreateGrid(len(self.tables), 2)
        self.grid.SetRowLabelSize(0)
        
        self.grid.SetColLabelValue(0, "Select")
        self.grid.SetColLabelValue(1, "Table Name")
        attr = wx.grid.GridCellAttr()
        attr.SetRenderer(wx.grid.GridCellBoolRenderer())
        attr.SetEditor(wx.grid.GridCellBoolEditor())
        self.grid.SetColAttr(0, attr)
        
        for i, table in enumerate(self.tables):
            self.grid.SetCellValue(i, 1, table)
            self.grid.SetCellValue(i, 0, "0")
        
        self.grid.SetColSize(0, 50)
        self.grid.AutoSizeColumn(1, setAsMin=True)
        vbox.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(vbox)
        
        self.Fit()
        self.SetMinSize((600, 500))

if __name__ == "__main__":
    app = wx.App()
    frame = DatabaseExporterFrame()
    frame.Show()
    app.MainLoop()