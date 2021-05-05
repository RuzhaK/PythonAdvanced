
# context manager
class CM:
    def __init__(self, file_name, mode):
        self.__file_name= file_name
        self.__mode=mode
    def __enter__(self):
        self.__file_handle=open(self.__file_name)
        return self.__file_handle
    def __exit__(self,*args,**kwargs):
        self.__file_handle.close()
# towa se prawi s funkciata with koiato posle zatwaria avtomatchno file-a
with open('numbers.txt') as f:
    print(f.readlines())