class Workshop:
    def __init__(self, length, width, thickness):   # dimensions of raw timber
        self.length = length
        self.width = width
        self.thick = thickness

    def rip_cut(self, designW):     # Method for the table saw
        if (self.width - designW) / self.length >= 0.005:     # Timber is wider than desired by > 0.5% of its length
            self.width = designW
            print("Board width was successfully reduced to", self.width, "mm")
        else:
            print("\nThe actual board width of ", self.width,
                  "is not wide enough to take out warping.\n Reduce design width or try wider timber.")
        return self.width

    def cross_cut(self, designL):           # Method for the cross-cut saw
        if self.length - designL >= 20:     # Timber is 20 mm > than desired to allow for proper squaring of ends.
            self.length = designL
            print("Board length was successfully reduced to", self.length, "mm")
        else:
            print("\nThe actual board length of ", self.length,
                  "is not long enough to square off ends of the board.\n Reduce design length or try longer timber.")
        return self.length

    def thicknesser(self, designT):     # Method for the planer/thicknesser
        if self.thick - designT >= 3:     # Check that there is adequate thickness to remove gouges and tool marks.
            self.thick = designT
            print("Board thickness was successfully reduced to", self.thick, "mm")
        else:
            print(
                "\nThe actual board thickness is insufficient to take out surface imperfections."
                " \nReduce the design thickness or try a thicker board")
        return self.thick

    def final_size(self):
        print("\nFinal board size: Length =", self.length, "mm, Width =", self.width, "mm, Thickness =", self.thick, "mm.")


# Instructions to cut down an over-sized piece of timber down to 2"x4"x6'
# Initiating board was purposely chosen too thin to generate warning
# This section can be improved by giving a more elegant user interface for input and output
Board1 = Workshop(1850, 115, 53)
Board1.rip_cut(102)
Board1.cross_cut(1829)
Board1.thicknesser(51)
Board1.final_size()