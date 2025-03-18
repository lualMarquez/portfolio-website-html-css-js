import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect("tasks.db") #Opens a database file named tasks.db
cursor = conn.cursor() #Creates a cursor, which allos us to execute SQL commands


#Creating a table (SQL Create Table)
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task_name TEXT NOT NULL, 
               status TEXT NOT NULL CHECK (status IN ('Pending', 'Completed'))
               )
""") 

conn.commit() #Saves changes to the database
conn.close()

print("Database and table created successfully!")

#ADD A TASK FUNCTION
 
def add_task(task_name):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    #THE ? placeholders prevent query to add a new task
    cursor.execute("INSERT INTO tasks (task_name, status) VALUES (?, ?)", (task_name, "Pending"))
    conn.commit()
    conn.close()
    
    print(f"Task '{task_name}' added successfully!")

#VIEW ALL TASKS
def view_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    #Retrieves all(*) rows FROM the tasks table
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    conn.close()
    
    print("\nTask List:")
    for task in tasks:
        print(f"[{task[0]}] {task[1]} - {task[2]}")

#UPDATE TASK STATUS

def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    #THIS UPDATES A TASK'S STATUS TO COMPLETED BASED ON ITS ID
    cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
    print(f"Task {task_id} marked as Completed!")

#DELETE A TASK

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    #THIS REMOVES A TASK FROM THE DATABASE
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
    print(f"Task {task_id} deleted successfully!")

#BUILD A SIMPLE MENU (MAIN)

def main():
    while True:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
