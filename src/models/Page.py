from dataclasses import dataclass, field

@dataclass
class Page:
    page_frame_nr: int
    modified: bool = field(default=False)# M bit
    supervisor: bool = field(default=False)
    bufforing: bool = field(default=False)
    write_permision: bool = field(default=False)
    in_use: bool = field(default=False)#R bit
    is_present: bool = field(default=False)

    def enablePresentBit(self):
        self.is_present = True
    def disablePresentBit(self):
        self.is_present = False
    def enableR_bit(self):
        self.in_use = True
    def disableR_bit(self):
        self.in_use = False