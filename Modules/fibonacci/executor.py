from . import create_sequence

class Executor:
    def __init__(self):
        self.__sequence=[]


    def run(self):
        while True:
            res=self.run_once()
            if not res:
                break

    def run_once(self):
        command = input()

        if command.startswith('Create Sequence'):
            return self.__handle_create(command)
        elif command.startswith('Locate'):
            return self.__handle_locate(command)
        elif command == 'Stop':
            return self.__handle_stop(command)
        return True

    def __handle_create(self,command):
        n = int(command.split()[-1])
        self.__sequence = create_sequence(n)
        print(self.__sequence)
        return True
    def __handle_locate(self,command):
        search = int(command.split()[-1])
        try:
            pos = self.__sequence.index(search)
            print(f"{search} is at {pos} position")
        except ValueError:
            print('no such position')
        return True
    def __handle_stop(self,command):
        return False
