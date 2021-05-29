from .preview_table import PreviewTableController
from .struct_table import StructTableController
class AnalisisExploratorioController(PreviewTableController,
    StructTableController):
    def set_analisis_exploratorio(self):
        if self.file:
            self.scroll_analisis.show()
            self.set_preview_table()
            self.set_struct_table()
        else:
            self.scroll_analisis.hide()
