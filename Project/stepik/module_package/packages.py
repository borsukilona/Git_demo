#package - каталог с набором необходимых модулей

import courses #импорт созданного нами пакета

print(dir(courses)) #убеждаемся, что наши модули импортированы ок

courses.python.get_python() #Python course
courses.get_php()
print(courses.python_doc.doc) #Python language documentation: Python course

