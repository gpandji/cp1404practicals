"""
Project Management Program
Estimated time: 3 hours
Actual time: 3 hours
"""

import csv
from datetime import datetime
from project import Project
from operator import attrgetter


def print_menu():
    """Print the menu."""
    print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date")
    print("- (A)dd new project\n- (U)update project\n- (Q)uit")


def load_projects(filename):
    """Load projects from a CSV file."""
    projects = []
    in_file = open(filename, 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file, delimiter='\t')

    for row in reader:
        projects.append(Project(row[0], row[1], row[2], row[3], row[4]))
    in_file.close()
    return projects


def save_projects(filename, projects):
    """Save projects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime("%d/%m/%Y"), project.priority, project.cost_estimate,
                 project.completion_percentage])


def display_projects(projects):
    """Display projects grouped by completion status, sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    complete_projects = sorted([p for p in projects if p.is_complete()])

    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_string):
    """Filter and display projects that start after a given date."""
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    filtered_projects.sort(key=attrgetter('start_date'))

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    print(selected_project)
    completion_percentage = input("New Percentage: ")
    priority = input("New Priority: ")

    if completion_percentage == "":
        completion_percentage = selected_project.completion_percentage
    else:
        completion_percentage = int(completion_percentage)

    if priority == "":
        priority = selected_project.priority
    else:
        priority = int(priority)

    selected_project.update_priority(priority)
    selected_project.update_completion_percentage(completion_percentage)


def main():
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print_menu()
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


main()
