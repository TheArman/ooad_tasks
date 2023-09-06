class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def add(self, t2):
        total_seconds = self.to_seconds() + t2.to_seconds()
        return Time.from_seconds(total_seconds)

    def print(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def read(self):
        self.hours = int(input("Enter hours: "))
        self.minutes = int(input("Enter minutes: "))
        self.seconds = int(input("Enter seconds: "))

    def to_seconds(self) -> float:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, seconds):
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        return cls(h, m, s)


# Usage example
t1 = Time(2, 30, 45)
t2 = Time(1, 15, 30)

t3 = t1.add(t2)
t3.print()

t4 = Time.from_seconds(5000)
t4.print()
print(t4.to_seconds())
