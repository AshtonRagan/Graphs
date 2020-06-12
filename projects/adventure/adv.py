from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# `player.current_room.id`
# `player.current_room.get_exits()`
# `player.travel(direction)`
traversal_path = []


def past_room(dir):
    if dir.lower() == "n":
        return "s"
    if dir.lower() == "w":
        return "e"
    if dir.lower() == "e":
        return "w"
    if dir.lower() == "s":
        return "n"


visted = {}


def treversal():

    cur_id = world.starting_room.id
    cur_dir = ""
    count = 0
    # len(room_graph)
    while len(visted) != len(room_graph):
        # while count >= 0:
        count += 1
        print("Count: ", count)
        if count >= 2000:
            return print("Failed")

        prev_id = cur_id
        cur_id = player.current_room.id
        # if room has not been visted, add it to visited

        # print("=---------------------------------------------=")
        # print("Current Room Id: ", cur_id)
        # print("Prev Room Id: ", prev_id)

        if cur_id not in visted:
            room_exits = {}
            for room in player.current_room.get_exits():
                room_exits[room] = "?"
            visted[cur_id] = room_exits

            # set the directions we visted
            if cur_id != world.starting_room.id:
                # change pre dir to our id
                if cur_dir in visted[prev_id]:
                    if visted[prev_id][cur_dir] == "?":
                        visted[prev_id][cur_dir] = cur_id
                if past_room(cur_dir) in visted[cur_id]:
                    if visted[cur_id][past_room(cur_dir)] == "?":
                        visted[cur_id][past_room(cur_dir)] = prev_id

        # print("Cur_dur: ", cur_dir)
        # print("Visted: ")
        # for i in visted:
        #     print(i, visted[i])

        # move
        # pick a direction to go
        if cur_id == world.starting_room.id:
            if prev_id != cur_id:
                # print("HERE")
                # changeing the pre ids to  cur id dir
                if cur_dir in visted[prev_id]:
                    if visted[prev_id][cur_dir] == "?":
                        visted[prev_id][cur_dir] = cur_id
                        # changeing cur oppiste dir to pre id
                if past_room(cur_dir) in visted[cur_id]:
                    if visted[cur_id][past_room(cur_dir)] == "?":
                        visted[cur_id][past_room(cur_dir)] = prev_id
            for key in visted[cur_id]:
                if visted[cur_id][key] == "?":
                    cur_dir = key
            else:
                if visted[cur_id][cur_dir] != "?":
                    player.travel(past_room(cur_dir))

            # print("Cur_dur: ", cur_dir)

        if player.can_travel(cur_dir):
            for key in visted[cur_id]:
                if visted[cur_id][key] == "?":
                    cur_dir = key
            print("Bing!")
            traversal_path.append(cur_dir)
            player.travel(cur_dir)
        else:
            print("Fizz")
            copy = cur_dir
            # check if there are other directions we can go
            # if there is not then backtrack till there is
            for key in visted[cur_id]:
                if visted[cur_id][key] == "?":
                    cur_dir = key
                else:
                    if visted[cur_id][key] != prev_id:
                        cur_dir = key
            # check if we found ?
            if copy == cur_dir:
                # no "?"

                cur_dir = past_room(cur_dir)
                player.travel(cur_dir)
            else:
                player.travel(cur_dir)
            print(visted)

        # print("=---------------------------------------------=\n")
        # move from room to room
        # add to our treversal path
        # mark each room as visted
        # goto new room
        # if we reach a room with no exits or
        # a room with all ajc-rooms visted
        # we need to back track till we find an unexplored path


# treversal()
# print(f"Treversal: ", traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
treversal()

print(f"Treversal: ", traversal_path)
print("LEN!!: ", len(visted))

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)


print("LEN-R-GRAPH: ", len(room_graph))

if len(visted) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visted)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
