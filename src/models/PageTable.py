from src.models.Page import Page
class PageTable():
    def __init__(self, memory_size: int, table_size: int):
        self.memory_size = memory_size
        self.table_size = table_size
        self.pages_in_memory = 0
        self.Table = []
        self.frames = [None] * memory_size
    
    def getRange(self):
        return self.table_size
    def generateData(self):
        for i in range(self.table_size):
            p = Page(i)
            self.Table.append(p)
    def addToMemory(self ,newPage: Page):
        if self.pages_in_memory >= self.memory_size:
            return "cannot add page"
        newPage.enableR_bit()
        self.pages_in_memory =+ 1


    def memoryReplace(newPage :Page, oldPage :Page):
        newPage.enableR_bit()
        oldPage.disableR_bit()
