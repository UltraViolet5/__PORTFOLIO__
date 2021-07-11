
player_start_position = 'X'
enemies_start_position = 'E'
boss_start_position = 'B'

walls = ('╔', '═', '╗', '║', '╚', '╝')
closed_door = '▐'
opened_door = '/'
npc = '&'

treasure = '■'
treasure_empty = '□'
treasure_value = 50

life = '♥'
life_regeneration = 5

trap = '░'
trap_damage = 3

fog = '.'


# Enemies
goblin = 'G'
boss = 'B'

enemies = [goblin, boss]

interactive_elements = [closed_door, npc, treasure]

collision_elements = [closed_door, npc, treasure, treasure_empty]
collision_elements.extend(walls)
collision_elements.extend(enemies)
