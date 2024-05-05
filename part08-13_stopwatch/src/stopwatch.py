# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def tick(self):
        self.seconds += 1
        
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
    
    # optimized
    def __str__(self):
        return (f"{self.minutes:02}:{self.seconds:02}")
    
    # def __str__(self):
    #     if self.minutes < 10:
    #         minu = "0" + str(self.minutes)
    #     else:
    #         minu = str(self.minutes)
        
    #     if self.seconds < 10:
    #         sec = "0"+ str(self.seconds)
    #     else:
    #         sec = str(self.seconds)
        
    #     return(f"{minu}:{sec}")

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3605):
        print(watch)
        watch.tick()
    