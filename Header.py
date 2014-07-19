class Header:
    
    def __init__(self, file_name):
        self.scrollStart = 0
        self.scrollStop = 0
        self.year = 0
        self.month = 0
        self.day = 0
        self.endDistance = 0
        self.USMH = ""
        self.DSMH = ""
        fp = open(file_name,'r')
        for line in fp:
            parts = line.split("=")
            if "Scroll Start" in parts[0]:
                self.scrollStart = float(parts[1]) / 100.0
            if "Scroll End" in parts[0]:
                self.scrollStop = float(parts[1]) / 100.0
            if "Year" in parts[0]:
                self.year = int(parts[1])
            if "Month" in parts[0]:
                self.month = int(parts[1])
            if "Day" in parts[0]:
                self.day = int(parts[1])
            if "Downstream MH" in parts[0]:
                self.DSMH = parts[1].rstrip()
            if "Upstream MH" in parts[0]:
                self.USMH = parts[1].rstrip()
            if "End Distance" in parts[0]:
                self.endDistance = float(parts[1].rstrip())
