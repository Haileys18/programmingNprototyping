#Hailey Sooknanan
#Period 5-6
import simplegui
import random

# Constants
WIDTH = 500  # Updated width
HEIGHT = 400  # Updated height
MONSTER_RADIUS = 50
MONSTER_COLOR = "Green"
EYE_COLOR = "White"
TEETH_COLOR = "Black"

# Game variables
player_health = 100
inventory = []
current_room = "Start"
char_position = [100, 150]
char_radius = 30
char_speed = 10

# Monster variables (Hallway)
hallway_monster_pos = [250, 150]  # Starting position far from the character in the hallway
hallway_monster_speed = 1  # Slower speed for the monster
hallway_monster_health = 100  # Health of the monster
hallway_monster_velocity = [random.choice([-hallway_monster_speed, hallway_monster_speed]), random.choice([-hallway_monster_speed, hallway_monster_speed])]

# Monster variables (Treasure Room)
treasure_monster1_pos = [200, 150]
treasure_monster2_pos = [300, 200]
treasure_monster_health = 100
treasure_monster1_velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
treasure_monster2_velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

# Room descriptions
rooms = {
    "Start": {"description": "You are in a dark room. There is a door to the north.", "position": [100, 150]},
    "Hallway": {"description": "You are in a dark what seems be a forset get rid of the threat!", "position": [200, 150]},
    "TreasureRoom": {"description": "You find yourself in another dark area with monsters.", "position": [300, 150]},
    "Ocean": {"description": "You are at the edge of a blue ocean, and the sky is clear with clouds.", "position": [250, 150]}
}

# GUI setup
frame = simplegui.create_frame("Adventure of The Wizard", WIDTH, HEIGHT)
label = frame.add_label("Room: " + rooms[current_room]["description"])
health_label = frame.add_label(f"Player Health: {player_health}")
hallway_monster_health_label = frame.add_label(f"Hallway Monster Health: {hallway_monster_health}")
treasure_monster_health_label = frame.add_label(f"Treasure Monsters Health: {treasure_monster_health}")
inventory_label = frame.add_label(f"Inventory: {', '.join(inventory)}")

# Functions for game mechanics
def start_game():
    global player_health, inventory, current_room, char_position
    global hallway_monster_pos, hallway_monster_health, hallway_monster_velocity
    global treasure_monster1_pos, treasure_monster2_pos, treasure_monster_health, treasure_monster1_velocity, treasure_monster2_velocity
    player_health = 100
    inventory = []
    current_room = "Start"
    char_position[:] = rooms[current_room]["position"]
    
    # Reset hallway monster
    hallway_monster_pos[:] = [250, 150]
    hallway_monster_health = 100
    hallway_monster_velocity = [random.choice([-hallway_monster_speed, hallway_monster_speed]), random.choice([-hallway_monster_speed, hallway_monster_speed])]

    # Reset treasure room monsters
    treasure_monster1_pos[:] = [200, 150]
    treasure_monster2_pos[:] = [300, 200]
    treasure_monster_health = 100
    treasure_monster1_velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    treasure_monster2_velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    update_labels()

def update_labels():
    label.set_text("Room: " + rooms[current_room]["description"])
    health_label.set_text(f"Player Health: {player_health}")
    hallway_monster_health_label.set_text(f"Hallway Monster Health: {hallway_monster_health}")
    treasure_monster_health_label.set_text(f"Treasure Monsters Health: {treasure_monster_health}")
    inventory_label.set_text(f"Inventory: {', '.join(inventory)}")

def move_to_room(new_room):
    global current_room
    current_room = new_room
    char_position[:] = rooms[new_room]["position"]
    update_labels()

def go_north():
    if current_room == "Start":
        move_to_room("Hallway")

def go_east():
    global current_room
    if current_room == "Hallway" and hallway_monster_health > 0:
        label.set_text("You must defeat the hallway monster first!")
    elif current_room == "Hallway" and hallway_monster_health <= 0:
        move_to_room("TreasureRoom")
    elif current_room == "TreasureRoom" and treasure_monster_health <= 0:
        move_to_room("Ocean")

def go_south():
    global current_room
    if current_room == "Hallway" or current_room == "Start":
        move_to_room("Start")
    elif current_room == "TreasureRoom":
        move_to_room("Ocean")
    elif current_room == "Ocean":
        # When the player is in the Ocean room and goes south, show the end screen
        label.set_text("You Win!")
        update_labels()  # Update the labels with the victory message
        # Optionally, you can reset the game or show a final victory message.
        start_game()  # Uncomment this if you want to reset the game after winning



def encounter_monster(damage):
    global player_health
    player_health = max(0, player_health - damage)
    health_label.set_text(f"Player Health: {player_health}")
    if player_health <= 0:
        label.set_text("Game Over")
        start_game()  # Restart the game if health is zero

def fight_monster():
    global hallway_monster_health, treasure_monster_health, player_health
    if current_room == "Hallway" and hallway_monster_health > 0:
        hallway_monster_health = max(0, hallway_monster_health // 2)
        player_health = min(100, player_health + 10)
    elif current_room == "TreasureRoom" and treasure_monster_health > 0:
        treasure_monster_health = max(0, treasure_monster_health - 50)  # Reduce health by 50
        player_health = min(100, player_health + 10)
    update_labels()

# Monster movement
def move_monsters():
    global hallway_monster_pos, hallway_monster_velocity
    global treasure_monster1_pos, treasure_monster2_pos, treasure_monster1_velocity, treasure_monster2_velocity

    if current_room == "Hallway" and hallway_monster_health > 0:
        # Move hallway monster
        hallway_monster_pos[0] += hallway_monster_velocity[0]
        hallway_monster_pos[1] += hallway_monster_velocity[1]
        if hallway_monster_pos[0] - MONSTER_RADIUS <= 0 or hallway_monster_pos[0] + MONSTER_RADIUS >= WIDTH:
            hallway_monster_velocity[0] = -hallway_monster_velocity[0]
        if hallway_monster_pos[1] - MONSTER_RADIUS <= 0 or hallway_monster_pos[1] + MONSTER_RADIUS >= HEIGHT:
            hallway_monster_velocity[1] = -hallway_monster_velocity[1]

    if current_room == "TreasureRoom" and treasure_monster_health > 0:
        # Move treasure room monsters
        treasure_monster1_pos[0] += treasure_monster1_velocity[0]
        treasure_monster1_pos[1] += treasure_monster1_velocity[1]
        treasure_monster2_pos[0] += treasure_monster2_velocity[0]
        treasure_monster2_pos[1] += treasure_monster2_velocity[1]
        for monster_pos, velocity in [(treasure_monster1_pos, treasure_monster1_velocity), (treasure_monster2_pos, treasure_monster2_velocity)]:
            if monster_pos[0] - MONSTER_RADIUS <= 0 or monster_pos[0] + MONSTER_RADIUS >= WIDTH:
                velocity[0] = -velocity[0]
            if monster_pos[1] - MONSTER_RADIUS <= 0 or monster_pos[1] + MONSTER_RADIUS >= HEIGHT:
                velocity[1] = -velocity[1]

# Collision detection
def check_collision():
    global player_health
    if current_room == "Hallway" and hallway_monster_health > 0:
        distance = ((char_position[0] - hallway_monster_pos[0])**2 + (char_position[1] - hallway_monster_pos[1])**2)**0.5
        if distance < char_radius + MONSTER_RADIUS:
            encounter_monster(2)
    if current_room == "TreasureRoom" and treasure_monster_health > 0:
        for monster_pos in [treasure_monster1_pos, treasure_monster2_pos]:
            distance = ((char_position[0] - monster_pos[0])**2 + (char_position[1] - monster_pos[1])**2)**0.5
            if distance < char_radius + MONSTER_RADIUS:
                encounter_monster(2)

# Key handler for player movement
def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        char_position[0] -= char_speed
    elif key == simplegui.KEY_MAP["right"]:
        char_position[0] += char_speed
    elif key == simplegui.KEY_MAP["up"]:
        char_position[1] -= char_speed
    elif key == simplegui.KEY_MAP["down"]:
        char_position[1] += char_speed

# Drawing handler
def draw(canvas):
    if current_room == "Hallway" and hallway_monster_health <= 0:
        # Draw forest background
        canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, "SkyBlue", "SkyBlue")
        canvas.draw_line([0, HEIGHT - 50], [WIDTH, HEIGHT - 50], 1, "Green")  # Grass

        # Draw trees
        tree_positions = [100, 200, 300, 400]
        for pos in tree_positions:
            canvas.draw_line([pos, HEIGHT - 50], [pos, HEIGHT - 100], 5, "Brown")  # Tree trunk
            canvas.draw_circle([pos, HEIGHT - 110], 30, 1, "Green", "DarkGreen")  # Tree leaves

        # Draw clouds
        canvas.draw_circle([100, 100], 30, 1, "White", "White")
        canvas.draw_circle([150, 100], 30, 1, "White", "White")
        canvas.draw_circle([200, 100], 30, 1, "White", "White")
        
        canvas.draw_circle([350, 50], 30, 1, "White", "White")
        canvas.draw_circle([400, 50], 30, 1, "White", "White")
        canvas.draw_circle([450, 50], 30, 1, "White", "White")
        
        canvas.draw_text("You defeated the monster!", (WIDTH // 2 - 100, HEIGHT // 2), 30, "Yellow")
        
    elif current_room == "TreasureRoom"  and treasure_monster_health <= 0:
       # Draw ocean background
        canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, "SkyBlue", "SkyBlue")
        canvas.draw_line([0, HEIGHT - 50], [WIDTH, HEIGHT - 50], 1, "Blue")  # Water

        # Draw fish
        fish_positions = [
            [100, HEIGHT - 80],
            [150, HEIGHT - 90],
            [200, HEIGHT - 100],
            [250, HEIGHT - 120],
            [300, HEIGHT - 110],
            [350, HEIGHT - 90]
        ]

        for pos in fish_positions:
            canvas.draw_circle([pos[0], pos[1]], 10, 1, "Orange", "Orange")

        # Additional fish with more details (e.g., tails)
        fish_details = [
            {"position": [100, HEIGHT - 80], "size": 10, "tail_direction": "left"},
            {"position": [150, HEIGHT - 90], "size": 12, "tail_direction": "right"},
            {"position": [200, HEIGHT - 100], "size": 14, "tail_direction": "left"},
            {"position": [250, HEIGHT - 120], "size": 16, "tail_direction": "right"},
            {"position": [300, HEIGHT - 110], "size": 18, "tail_direction": "left"},
            {"position": [350, HEIGHT - 90], "size": 12, "tail_direction": "right"}
        ]

        for fish in fish_details:
            canvas.draw_circle(fish["position"], fish["size"], 1, "Orange", "Orange")
            # Draw fish tail
            if fish["tail_direction"] == "left":
                canvas.draw_polygon(
                    [(fish["position"][0] - fish["size"], fish["position"][1]),
                     (fish["position"][0] - fish["size"] - 10, fish["position"][1] - 5),
                     (fish["position"][0] - fish["size"] - 10, fish["position"][1] + 5)],
                    1, "Orange", "Orange"
                )
            elif fish["tail_direction"] == "right":
                canvas.draw_polygon(
                    [(fish["position"][0] + fish["size"], fish["position"][1]),
                     (fish["position"][0] + fish["size"] + 10, fish["position"][1] - 5),
                     (fish["position"][0] + fish["size"] + 10, fish["position"][1] + 5)],
                    1, "Orange", "Orange"
                )

        # Draw clouds
        canvas.draw_circle([100, 100], 30, 1, "White", "White")
        canvas.draw_circle([150, 100], 30, 1, "White", "White")

        canvas.draw_text("You Win!", (WIDTH // 2 - 40, HEIGHT // 2), 30, "Yellow")
    elif current_room == "Ocean":
        canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, "SkyBlue", "SkyBlue")
        # Draw castle in the background
        # Castle walls
        canvas.draw_polygon([(WIDTH // 4, HEIGHT - 150), (WIDTH // 4 + 100, HEIGHT - 150), 
                             (WIDTH // 4 + 100, HEIGHT - 50), (WIDTH // 4, HEIGHT - 50)], 
                            1, "Grey", "Grey")
        canvas.draw_polygon([(WIDTH // 2, HEIGHT - 150), (WIDTH // 2 + 100, HEIGHT - 150),
                             (WIDTH // 2 + 100, HEIGHT - 50), (WIDTH // 2, HEIGHT - 50)],
                            1, "Grey", "Grey")

        # Castle roof
        canvas.draw_polygon([(WIDTH // 4 - 10, HEIGHT - 150), (WIDTH // 4 + 110, HEIGHT - 150),
                             (WIDTH // 4 + 50, HEIGHT - 200)], 1, "Grey", "Grey")
        canvas.draw_polygon([(WIDTH // 2 - 10, HEIGHT - 150), (WIDTH // 2 + 110, HEIGHT - 150),
                             (WIDTH // 2 + 50, HEIGHT - 200)], 1, "Grey", "Grey")

        # Draw door (castle entrance)
        canvas.draw_polygon([(WIDTH // 4 + 40, HEIGHT - 50), (WIDTH // 4 + 60, HEIGHT - 50),
                             (WIDTH // 4 + 60, HEIGHT - 100), (WIDTH // 4 + 40, HEIGHT - 100)], 
                            1, "Brown", "Brown")

        # Draw towers
        canvas.draw_polygon([(WIDTH // 4 - 20, HEIGHT - 150), (WIDTH // 4 - 20, HEIGHT - 250),
                             (WIDTH // 4 + 20, HEIGHT - 250), (WIDTH // 4 + 20, HEIGHT - 150)],
                            1, "Grey", "Grey")
        canvas.draw_polygon([(WIDTH // 2 + 80, HEIGHT - 150), (WIDTH // 2 + 80, HEIGHT - 250),
                             (WIDTH // 2 + 120, HEIGHT - 250), (WIDTH // 2 + 120, HEIGHT - 150)],
                            1, "Grey", "Grey")

        # Draw text
        canvas.draw_text("You Win!", (WIDTH // 2 - 40, HEIGHT // 2), 30, "Yellow")
    elif current_room == "Start":
        # Draw the background for the Start room
        # Blue sky
        canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, "SkyBlue", "SkyBlue")

        # Draw grass
        canvas.draw_line([0, HEIGHT - 50], [WIDTH, HEIGHT - 50], 1, "Green")

        # Draw trees
        tree_positions = [100, 200, 300, 400]  # Different tree positions
        for pos in tree_positions:
            # Tree trunk
            canvas.draw_line([pos, HEIGHT - 50], [pos, HEIGHT - 100], 5, "Brown")
            # Tree leaves
            canvas.draw_circle([pos, HEIGHT - 110], 30, 1, "Green", "DarkGreen")

        # Draw text on the screen
        canvas.draw_text("Welcome to The Adeventures of The Wizard!", (1,100), 14, "White")
        canvas.draw_text("Here You Will Complete Two Levels to Save The Forests and Oceans", (1,200), 14, "White")

        # Draw character (optional, could show the character standing in the start room)
        canvas.draw_circle(char_position, char_radius, 2, "Black", "Yellow")

        # Draw wizard hat (optional)
        canvas.draw_polygon([(char_position[0] - 15, char_position[1] - 30), 
                              (char_position[0] + 15, char_position[1] - 30), 
                              (char_position[0], char_position[1] - 60)], 1, "Gold", "Gold")

    else:
        # Draw current room visuals
        canvas.draw_text(rooms[current_room]["description"], (20, 20), 14, "White")
        
        # Draw character
        canvas.draw_circle(char_position, char_radius, 2, "Black", "Yellow")
        
        # Draw wizard hat on the character (simple triangle)
        canvas.draw_polygon([(char_position[0] - 15, char_position[1] - 30), 
                              (char_position[0] + 15, char_position[1] - 30), 
                              (char_position[0], char_position[1] - 60)], 1, "Gold", "Gold")
        
        # Draw monsters
        if current_room == "Hallway" and hallway_monster_health > 0:
            canvas.draw_circle(hallway_monster_pos, MONSTER_RADIUS, 1, MONSTER_COLOR, MONSTER_COLOR)
        elif current_room == "TreasureRoom" and treasure_monster_health > 0:
            for monster_pos in [treasure_monster1_pos, treasure_monster2_pos]:
                canvas.draw_circle(monster_pos, MONSTER_RADIUS, 1, MONSTER_COLOR, MONSTER_COLOR)
    
    # Move monsters and check collisions
    move_monsters()
    check_collision()


# Button setup
frame.add_button("Start Game", start_game)
frame.add_button("Level 1", go_north)
frame.add_button("Level 2", go_east)
frame.add_button("End Game", go_south)
frame.add_button("Fight Monster", fight_monster)

# Register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Start the game
start_game()
frame.start()
