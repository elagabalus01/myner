from .preview_table import PreviewTableController
from .struct_table import StructTableController
from .faltantes_table_controller import FaltantesTableController
class AnalisisExploratorioController(PreviewTableController,
    StructTableController,FaltantesTableController):
    def set_analisis_exploratorio(self):
        if self.file:
            self.scroll_analisis.show()
            self.set_preview_table()
            self.set_struct_table()
            self.set_missed_table()
        else:
            self.scroll_analisis.hide()
