# Problem Set 1: Creating a daily ToDo List

weekly_todos = [
    ["Wake up early", "Exercise", "Prepare breakfast"],  # Monday
    ["Check emails", "Team meeting", "Submit report"],   # Tuesday
    ["Grocery shopping", "Prepare lunch", "Read a book"],# Wednesday
    ["Clean the house", "Workout", "Plan weekend"],      # Thursday
    ["Finish project", "Attend Python class", "Dinner"], # Friday
    ["Go hiking", "Watch a movie", "Family time"],       # Saturday
    ["Relax", "Organize files", "Plan for next week"]    # Sunday
]

# Function to display all tasks for a given day
def show_all_todos_for_day(day_index):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"\nTo-dos for {days[day_index]}:")
    for task in weekly_todos[day_index]:
        print(f"- {task}")

# Function to display one task at a time for a given day
def show_tasks_one_by_one(day_index):
    print("\nTasks for the day (one by one):")
    for task in weekly_todos[day_index]:
        print(task)

# Show all tasks for the entire week
def show_all_weekly_todos():
    print("\nAll Weekly To-Dos:")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, day in enumerate(days):
        print(f"\n{day}:")
        for task in weekly_todos[i]:
            print(f"- {task}")

# Show all tasks for Wednesday
show_all_todos_for_day(0)  # Wednesday

# Show tasks one by one for Friday
show_tasks_one_by_one(6)  # Friday

# Show all weekly todos
show_all_weekly_todos()


# P.S 2  creating a bio dict.

my_bio = {
	"name": "Solomon Oyathekhua", 
	"age": 28,
	"class": "Python Programming",
	"skills": ["Python",  "AI Tools", "MySQL"],
	"hobbies": ["Reading", "Cycling", "Sight-Seeing", "Road Trips"]
}

#P.S 3

for key, value in my_bio.items():
	if key == "skills":
		print("My skills are: ")
		for skills in value:
			print(skills)
	else:
		print(f"My {key.capitalize()} is {value}")


#Problem Set 4

double_list = [(lambda x: x * 2)(x) for x in range(1, 51)]
print(double_list)
