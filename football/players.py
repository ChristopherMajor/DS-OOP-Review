'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring TODO
    THIS IS NOT A VERY GENERALIZABLE MODEL IF YOU KNOW THINGS ABOUT FOOTBALL
    and that's okay
    Player perameters are name, yards, touchdowns, safety, interceptions, field goals. 
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.

class Defense(Player):
    '''
    add defensive player class
    '''
    def __init__(self, name=None, yards=0, touchdowns=0, safety=0,
                 interceptions=0, field_goals=0, tackles=4, sacks=1):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.tackles = tackles
        self.sacks = sacks
        
    def def_points(self):
        ''' 
        function for adding points scored by defensive players 
        '''
        tackle_points = self.tackles
        sack_points = self.sacks *2
        defense_points = tackle_points + sack_points
        return defense_points

#if __name__ == '__main__':
    