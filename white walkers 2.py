class locker:
    def __init__(self, locker_no):
        self.locker_no = locker_no
        self.assigned_team = None
    
    def assign_team(self, team_name):
        self.assigned_team = team_name
    
    def release(self):
        self.assigned_team = None    

class Team:
    def __init__(self, name):
        self.name = name

class locker_room:
    def __init__(self,total_lockers):
        self.total_lockers = total_lockers
        self.lockers = [locker(i) for i in range(1, total_lockers + 1)]
    
    def locker_assignments(self, locker_no, team_name):
        locker1 = self.lockers[locker_no - 1 ]
        if locker1.assigned_team:
            print(f"Locker {locker_no} is already assigned to {locker1.assigned_team.name}")
            print()
            print("available lockers are : ")
            print()
            self.locker_room_access()
        
        else:
            locker1.assign_team(team_name)
            print(f"locker {locker_no} is assigned  ")
    
    def increase_lockers(self, additional_lockers):
        self.total_lockers += additional_lockers
        
        print(f"{additional_lockers} added")
        print(f"Total number of lockers {self.total_lockers}")
        for i in range(self.total_lockers - additional_lockers + 1, self.total_lockers + 1):
            self.lockers.append(locker(i))
    
    def add_lockers(self):
        number = int(input("Enter how many lockers need to be added: "))
        self.increase_lockers(number)
        
    def locker_room_access(self):
        print("Locker No's\tStatus")
        print("-" * 25)
        for lock in self.lockers:
            if lock.assigned_team:
                print(f"    {lock.locker_no}\t\tAssigned to {lock.assigned_team.name}")
            else:
                print(f"    {lock.locker_no}\t\tAvailable")

    def save_to_file(self):
        with open("project_file.txt", "w") as file:
            file.write("Locker No's\tStatus\n")
            file.write("-----------------------------------\n")
            for lock in self.lockers:
                if lock.assigned_team:
                    file.write(f"    {lock.locker_no}\t\tAssigned to {lock.assigned_team.name}\n")
                else:
                    file.write(f"    {lock.locker_no}\t\tAvailable\n")
        print(" data saved to 'project_file.txt'.")

    
    def release(self, locker_num):
        lockers = self.lockers[locker_num - 1]
        lockers.release()
        print(f"Locker number {locker_num} is released")
 
l = locker_room(10)
choices = {'1': l.locker_assignments,
           '2': l.release,
           '3': l.locker_room_access,
           '4': l.add_lockers,
           '5': l.save_to_file,
           }

while True:
    print("\n1. Locker Assignments")
    print("2. Release Locker")
    print("3. Locker Room Access")
    print("4. Add Lockers")
    print("5. Save to File")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '6':
        print("Program exited.")
        break
    
    if choice in choices:
        if choice == '1':
            locker_numbers = int(input("Enter locker number: "))
            if  0 < locker_numbers <= len(l.lockers) :
                team_names = input("Enter team name: ")
                choices[choice](locker_numbers, Team(team_names))
            else:
                print(f"Locker number {locker_numbers} is must within total number of lockers.")
        
        elif choice == '2':
            locker_numbers = int(input("Enter locker number: "))
            choices[choice](locker_numbers)
        else:
            choices[choice]()
    else:
        print("Invalid choice. Please try again.")
