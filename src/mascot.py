class TurtleMascot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weight_grams = 100
        self.stage = 'Egg Hatchling'

    def encounter_contamination(self):
        print(f'Oh no! Inconsistent recycling or plastic contamination made. {self.name} feels weak :-(')
        self.health = max(0, self.health - 15)
        if self.health == 0:
            #redirect them to the game 
            print(f'{self.name} is too weak to play and has checked into the Eco-Hospital.')
        else:
            return f'Health: {self.health}/100 | Weight: {self.weight_grams}g'

    def feed_turtle(self):
        print(f'Yum! {self.name} loved these clean recyclables!!')
        self.health = min(100, self.health + 5)
        self.weight_grams += 15
        return f'Health: {self.health}/100 | Weight: {self.weight_grams}g'
    
    def get_stage(self):
        if self.weight_grams < 300:
            self.stage = 'Egg Hatchling'
        elif self.weight_grams < 1000: 
            self.stage = 'Young Explorer'
        else:
            self.stage = 'Semakau Landfill Final Boss'
        return self.stage