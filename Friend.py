import helpers as h
from TimeRange import TimeRange
from dataclasses import dataclass, field

@dataclass
class Friend:
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)




