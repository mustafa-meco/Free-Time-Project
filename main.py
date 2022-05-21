import helpers as h
from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time : str # 00:30
    end_time : str # 05:00

    start_minutes : int = field(init=False) # 30
    end_minutes : int = field(init= False) # 300

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)



t1 = TimeRange(start_time="00:30", end_time="05:00")
print(t1)