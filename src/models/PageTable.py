from src.models.Page import Page

class PageTable:
    def __init__(self, memory_size: int, table_size: int):
        self.memory_size = memory_size
        self.table_size = table_size

        self.pages_in_memory = 0
        self.frames = [None] * memory_size

    def getRange(self):
        return self.table_size

    def memoryReplace(self, newPage: Page, oldPage: Page):
        idx = self.frames.index(oldPage)
        self.frames[idx] = newPage

    def access(self, page_id, op, algorithm, time):
        for page in self.frames:
            if page is not None and page.page_id == page_id:
                page.set_r_bit()
                page.last_use = time
                if op == "write":
                    page.set_m_bit()
                return "hit"

        new_page = Page(page_id=page_id)
        new_page.set_r_bit()
        new_page.last_use = time

        if op == "write":
            new_page.set_m_bit()

        if None in self.frames:
            idx = self.frames.index(None)
            self.frames[idx] = new_page
            self.pages_in_memory += 1
            return "fault"

        victim = algorithm.select_victim(self.frames)
        self.memoryReplace(new_page, victim)
        return "fault"