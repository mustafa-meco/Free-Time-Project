class CustomList(list):
    def remove_if_exist(self, el):
        try:
            self.remove(el)
        except ValueError:
            pass
            #print(f"{el} already deleted!")