class CharCounter:

    def __init__(self):
        self._charCounter = {}

    def get_char_count(self,c):
        if c in self._charCounter:
            return self._charCounter[c]
        else:
            return 0

    def add_char(self,c):
        #if not exist this char set the counter to 1
        if self.get_char_count(c) == 0:
            self._charCounter[c] = 1
        #else increase it by 1
        else:
            self._charCounter[c] += 1
    
    def get_char_counter(self):
        return self._charCounter