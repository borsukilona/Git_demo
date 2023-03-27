#внутри модуля вложенного покета мы можем обратиться к модулю пакета ИЗВНЕ (к модулю нашего пакета-родителя)
#.. означают переход к родительской папке

from ..python import get_python

doc = """Python language documentation: """ + get_python()
