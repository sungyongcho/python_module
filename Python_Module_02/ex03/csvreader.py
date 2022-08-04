class CsvReader():
    def __init__(self, filename=None, sep=', ', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        self.file_obj = open(self.filename, "r")
        for line in self.file_obj:
            self.data.append(list(map(str.strip, line.split(self.sep))))
        if all(len(line) == len(self.data[0]) for line in self.data):
            return self
        else:
            return None

    def __exit__(self, type, value, trace_back):
        self.file_obj.close()

    def getdata(self):
        """Retrieves the data/records from skip_top to skip bottom.
        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        header_to_insert = self.data[0]
        return_data = self.data[self.skip_top +
                                1: len(self.data) - self.skip_bottom]
        if self.header is True:
            return_data.insert(0, header_to_insert)
            return return_data
        else:
            return return_data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is False:
            return None
        else:
            return self.data[0]
