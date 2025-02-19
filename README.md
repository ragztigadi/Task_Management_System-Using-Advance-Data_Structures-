# Task Assignment System

This project is a Python-based system for managing tasks using various data structures like lists, stacks, queues, and graphs. It includes modules for task management, user management, and data structure implementations.

---

## Project Structure

```
DATA_STRUCTURES/
├── Task_Assignment_System/
│   ├── Models/
│   │   ├── __init__.py
│   │   ├── Graph.py
│   │   ├── Queue.py
│   │   ├── Stack.py
│   │   ├── Task.py
│   │   └── user.py
│   ├── Service/
│   │   ├── __init__.py
│   │   ├── task_services.py
│   │   └── user_service.py
│   ├── __init__.py
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── Task_Management_System/
│   ├── list_ds.py
│   ├── main.py
│   ├── tuple_ds.py
│   └── zip_file.zip
└── __pycache__/
```

---

## Modules

### 1. **Models**
   - **Graph.py**: Implements graph data structure and related operations.
   - **Queue.py**: Implements queue data structure and related operations.
   - **Stack.py**: Implements stack data structure and related operations.
   - **Task.py**: Defines the `Task` class and its attributes.
   - **user.py**: Defines the `User` class and its attributes.

### 2. **Service**
   - **task_services.py**: Contains service logic for task management (e.g., creating, completing, and tracking tasks).
   - **user_service.py**: Contains service logic for user management.

### 3. **Data Structures**
   - **list_ds.py**: Implements basic list operations (e.g., adding/removing elements).
   - **tuple_ds.py**: Implements basic tuple operations (e.g., creating tuples, finding length).

---

## Setup Instructions

### 1. **Prerequisites**
   - Python 3.x installed on your system.
   - Ensure `pip` is installed to manage dependencies.

### 2. **Install Dependencies**
   Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Running the Code**
   - Navigate to the project root directory:
     ```bash
     cd F:\Data_Structures\Task_Assignment_System
     ```
   - Run the `main.py` file:
     ```bash
     python main.py
     ```
   - To run specific services (e.g., `task_services.py`), ensure you are in the correct directory and use:
     ```bash
     python Service/task_services.py
     ```

### 4. **Setting PYTHONPATH**
   If you encounter `ModuleNotFoundError`, add the project root to the `PYTHONPATH` environment variable:
   ```bash
   set PYTHONPATH=%PYTHONPATH%;F:\Data_Structures
   ```

---

## Usage

### 1. **Task Management**
   - Use the `Task` class in `Models/Task.py` to create and manage tasks.
   - The `task_services.py` file provides methods for creating, completing, and tracking tasks.

### 2. **Data Structures**
   - Use `list_ds.py` and `tuple_ds.py` for basic list and tuple operations.
   - Use `Graph.py`, `Queue.py`, and `Stack.py` for advanced data structure implementations.

---

## Troubleshooting

### 1. **ModuleNotFoundError**
   - Ensure the project root (`DATA_STRUCTURES`) is in the `PYTHONPATH`.
   - Run scripts from the root directory or set the `PYTHONPATH` as described above.

### 2. **Incorrect Imports**
   - Verify that the import statements in your code match the project structure.
   - Example:
     ```python
     from Task_Assignment_System.Models.Graph import Graph
     ```

---

## Contributing
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or issues, please contact the project maintainer:
- **Name**: Raghav Tigadi
- **Email**: ##########
