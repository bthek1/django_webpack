const todos: { title: string; completed: boolean }[] = [];

const addTodo = (title: string) => {
    todos.push({ title, completed: false });
    renderTodos();
};

const toggleTodo = (index: number) => {
    todos[index].completed = !todos[index].completed;
    renderTodos();
};

const renderTodos = () => {
    const todoList = document.getElementById('todo-list')!;
    todoList.innerHTML = todos
        .map(
            (todo, index) => `
                <li>
                    <input type="checkbox" ${todo.completed ? 'checked' : ''} onchange="toggle(${index})" />
                    ${todo.title}
                </li>
            `
        )
        .join('');
};

// Attach global functions for simplicity
(window as any).addTodo = addTodo;
(window as any).toggle = toggleTodo;
