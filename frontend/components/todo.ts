import axios from "axios";

export const setupToDoApp = () => {
    const addButton = document.getElementById("add-todo");
    const newTodoInput = document.getElementById("new-todo") as HTMLInputElement;
    const todoList = document.getElementById("todo-list");

    if (!addButton || !newTodoInput || !todoList) {
        console.error("Required elements not found in the DOM.");
        return;
    }

    // Attach event listener for the Add button
    addButton.addEventListener("click", async () => {
        const title = newTodoInput.value.trim();
        if (!title) {
            alert("Please enter a task title.");
            return;
        }

        try {
            // Get CSRF token from meta tag
            const csrfToken = getCSRFToken();
            if (!csrfToken) throw new Error("CSRF token not found.");

            // Send POST request with CSRF token
            await axios.post(
                "/todo/api/todos/",
                { title, completed: false },
                {
                    headers: {
                        "X-CSRFToken": csrfToken, // Send CSRF token in the headers
                    },
                }
            );
            newTodoInput.value = "";
            fetchAndRenderTodos();
        } catch (error) {
            console.error("Error adding task:", error);
            alert("Failed to add the task. Please try again.");
        }
    });

    // Fetch and render todos
    const fetchAndRenderTodos = async () => {
        try {
            const response = await axios.get("/todo/api/todos/");
            renderTodos(response.data, todoList);
        } catch (error) {
            console.error("Error fetching tasks:", error);
            alert("Failed to fetch tasks. Please try again later.");
        }
    };

    // Render todos
    const renderTodos = (
        todos: Array<{ id: number; title: string; completed: boolean }>,
        container: HTMLElement
    ) => {
        if (!todos.length) {
            container.innerHTML = `
                <li class="list-group-item text-center text-muted">
                    No tasks found.
                </li>`;
            return;
        }

        container.innerHTML = todos
            .map(
                (todo) => `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${todo.title}
                    <span class="badge ${todo.completed ? "bg-success" : "bg-secondary"}">
                        ${todo.completed ? "Completed" : "Pending"}
                    </span>
                </li>`
            )
            .join("");
    };

    // Helper to get CSRF token
    const getCSRFToken = (): string | null => {
        const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
        return csrfTokenMeta ? csrfTokenMeta.getAttribute("content") : null;
    };

    // Initial fetch of todos
    fetchAndRenderTodos();
};
