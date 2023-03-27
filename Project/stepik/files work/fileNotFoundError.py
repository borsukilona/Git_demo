# обработка ошибки FileNotFoundError

'''
try:
    file = open("my_file.txt", encoding="utf-8")
    try:
        s = file.readlines()
        print(s)
    finally:
        file.close()
except FileNotFoundError:
    print("not possible to open the file, please, check the correct name or path")
except:  # отлавливаем любые другие ошибки, которые могут возникнуть
    print("error occurs while working with file")
'''

# прописали внутренний try-finaly, чтобы учесть момент, когда файл открыть мы таки сможем, но мы не сможем его прочесть
# и чтобы файл в любом случае закрылся, даже если мы не сможем его прочитать, то мы поместили file.close() в блок, который будет выполнени по-любому - finally


# try - finally блок можно заменить файловым менеджером контекста:
# менеджер контекста автоматичесви всегда закроет файл (были там ошибки или нет), поэтому прописывать file.close() не нужно

try:
    with open("my_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
except FileNotFoundError:
    print("not possible to open the file, please, check the correct name or path")
except:  # отлавливаем любые другие ошибки, которые могут возникнуть
    print("error occurs while working with file")
finally:
    print(file.closed) #true / false, чисто чтобы убедиться, что файл был закрыт (получаем True)

