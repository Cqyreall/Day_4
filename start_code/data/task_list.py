tasks = [
	{ "description": "Wash Dishes", "completed": False, "time_taken": 10 },
	{ "description": "Clean Windows", "completed": False, "time_taken": 15 },
	{ "description": "Make Dinner", "completed": True, "time_taken": 30 },
	{ "description": "Feed Cat", "completed": False, "time_taken": 5 },
	{ "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


def task_descrip(lists, user_descrip):
    # old = []
    for lst in lists:
        if (lst["description"] == user_descrip):
            lists.append(lst)
        else:
            lists = []
    return lists
