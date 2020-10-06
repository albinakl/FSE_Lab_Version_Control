class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            return 'Key not exist'

    def set(self, key, value):
        if key in self.data:
            self.data[key] = value 
    
    def add(self, key, value):
        if key in self.data:
            #print('Value error, ', key, ' is already in the Storage')
            raise Exception
        else:
            self.data[key] = value
        return self.data
