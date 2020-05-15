from util import Queue


class Player:
    def __init__(self, starting_room, num_rooms):
        self.current_room = starting_room
        self.seen = {starting_room.id}
        self.num_rooms = num_rooms
        self.taversal_path = []

    def travel(self, direction, show_rooms = False):
        # gets next room
        next_room = self.current_room.get_room_in_direction(direction)
        # confirm that next room has not been visited and exists 
        if next_room is not None:
            #moves current room to next room 
            self.current_room = next_room
            #adds curent directon to traversal path 
            self.taversal_path.append(direction)
            #adds current room to seen rooms 
            self.seen.add(self.current_room.id)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
    # use BFS to find a path to the nearest unseen rooms 
    def find_rooms(self):
        # def bfs(self, starting_vertex, destination_vertex):
        # """
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breath-first order.
        # """
        # ptv = Queue()
        # ptv.enqueue([starting_vertex])

        # visited = set()

        # while ptv.size() > 0:
        #     path = ptv.dequeue()
        #     cv = path[-1]
        #     if cv not in visited:
        #         if cv == destination_vertex:
        #             return path
        #         visited.add(cv)
        #         for neighbor in self.get_neighbors(cv):
        #             new_path= list(path)
        #             new_path.append(neighbor)
        #             ptv.enqueue(new_path)

        #initilize Que with starting room
        q = Queue()
        q.enqueue((self.current_room, []))
        #keep track of rooms that have been seen
        visited = set()
        #while queue is not empty
        while q.size() > 0:
            #get room and path
            room, path = q.dequeue()
            #print(f"room {room}")
            #print(f"path {path}")
            #if room has not been seen retun path
            if room.id not in self.seen:
                return path
            #else add room to visited
            elif room.id not in visited:
                visited.add(room.id)
                #add paths to que for each edge
                for door in room.get_exits():
                    path_copy = path.copy()
                    path_copy.append(door)
                    q.enqueue((room.get_room_in_direction(door), path_copy))


#find new rooms and explore them then find more rooms and explore those until you've found all rooms
    def run_maze(self):
        #while rooms seen is less than the total number of rooms 
        while len(self.seen)<self.num_rooms:
            #find rooms arround using BFS 
            path = self.find_rooms()
            #Travel in all directions available
            #print(f"PATH>>> {path}")
            for direction in path:
                self.travel(direction)
