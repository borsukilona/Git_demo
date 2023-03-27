'''
file = open("out.txt", "w") # открываем файл на запись в этот файл чего-либо
# все содержимое файла, до открытия его на запись, уничножается и мы туда записываем новую инфу

file.write("Hello")
file.close()
'''

try:
    with open("out.txt", "w") as file:
        '''
        file.write("Hello1")
        file.write("Hello2")
        file.write("Hello3")
        #Hello1Hello2Hello3
        '''
        # Hello1Hello2Hello3
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
        # Hello1
        # Hello2
        # Hello3
        with open("out.txt", "a"): # добавляем к существующей инфе в файле другую инфу; мы не можем читать данные из файла такого (куда пишем или дозаписываем)
            file.write("Hello4\n")
            file.write("Hello5\n")
            file.write("Hello6\n")
            # Hello1
            # Hello2
            # Hello3
            # Hello4
            # Hello5
            # Hello6
except:
    print("error with working with the file")

# -------------------------------------------------------------------------------------------------------------------

try:
    with open("out.txt", "a+") as file:  # теперь мы можем и читать и добавлять инфу
        file.seek(0)  # поскольку файловая позиция (именно для СЧИТЫВАНИЯ файла, а не для записи ) в конце, мы перемещаем её в начало, чтоб читать файл сначала
        s = file.readlines()
        print(s)
        # ['Hello1\n', 'Hello2\n', 'Hello3\n', 'Hello4\n', 'Hello5\n', 'Hello6\n']
except:
    print("error with working with the file")

# -------------------------------------------------------------------------------------------------------------------

try:
    with open("out.txt", "a+") as file:  # теперь мы можем и читать и добавлять инфу
        file.seek(0)  # поскольку файловая позиция (именно для СЧИТЫВАНИЯ файла, а не для записи ) в конце, мы перемещаем её в начало, чтоб читать файл сначала
        file.writelines(["Hello7\n", "Hello8\n"])  # дозапись в файл нескольких строк
        file.seek(0)
        s = file.readlines()
        print(s)
        # ['Hello1\n', 'Hello2\n', 'Hello3\n', 'Hello4\n', 'Hello5\n', 'Hello6\n', 'Hello7\n', 'Hello8\n']
except:
    print("error with working with the file")

# -------------------------------------------------------------------------------------------------------------------
# сохранить коллекцию books в файл и потом прочитать этот файл
import pickle

books = [
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мёртвые души", "Гоголь Н.В.", 190)
]

# пишем данные в файл
file_write = open("out.bin", "wb") #открываем файл на запись в бинарном режиме доступа
pickle.dump(books, file_write) #что занести, куда занести
file_write.close()

# читаем данные из файла
file_read = open("out.bin", "rb") # читаем бинарный файл
bs = pickle.load(file_read)
print(bs)
#[('Евгений Онегин', 'Пушкин А.С.', 200),
# ('Муму', 'Тургенев И.С.', 250),
# ('Мастер и Маргарита', 'Булгаков М.А.', 500),
# ('Муртвые души', 'Гоголь Н.В.', 190)]

# -------------------------------------------------------------------------------------------------------------------
# сохранить несколько коллекций book в файл

book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Мёртвые души", "Гоголь Н.В.", 190]

# пишем данные в файл
try:
    with open("out2.bin", "wb") as file_collections:
        pickle.dump(book1, file_collections)
        pickle.dump(book2, file_collections)
        pickle.dump(book3, file_collections)
        pickle.dump(book4, file_collections)
except:
    print("error with working with the file")


# читаем данные из файла
try:
    with open("out2.bin", "rb") as file_collections:
        b1 = pickle.load(file_collections)
        b2 = pickle.load(file_collections)
        b3 = pickle.load(file_collections)
        b4 = pickle.load(file_collections)
        print(b1, b2, b3, b4, sep="\n")
        # ['Евгений Онегин', 'Пушкин А.С.', 200]
        # ['Муму', 'Тургенев И.С.', 250]
        # ['Мастер и Маргарита', 'Булгаков М.А.', 500]
        # ['Мёртвые души', 'Гоголь Н.В.', 190]
except:
    print("error with working with the file")
