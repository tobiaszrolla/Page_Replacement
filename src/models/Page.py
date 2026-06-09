from dataclasses import dataclass, field

@dataclass
class Page:
    page_id: tuple[int, int]
    modified: bool = False  # M bit
    referenced: bool = False  # R bit
    is_present: bool = False
    last_use = 0
    use_counter = 0


    def set_r_bit(self):
        self.referenced = True

    def reset_r_bit(self):
        self.referenced = False

    def set_m_bit(self):
        self.modified = True

    def reset_m_bit(self):
        self.modified = False

    def set_present(self):
        self.is_present = True

    def reset_present(self):
        self.is_present = False