const API_BASE = 'https://1fqcfk17gg.execute-api.eu-north-1.amazonaws.com';

async function fetchTasks() {
  const res = await fetch(`${API_BASE}/tasks`);
  const tasks = await res.json();

  const taskList = document.getElementById('task-list');
  taskList.innerHTML = '';

  tasks.forEach(task => {
    const li = document.createElement('li');
    li.textContent = task.task;

    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.onclick = () => deleteTask(task.task_id);

    li.appendChild(delBtn);
    taskList.appendChild(li);
  });
}

async function addTask(task) {
  await fetch(`${API_BASE}/task`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  });
  fetchTasks();
}

async function deleteTask(taskId) {
  await fetch(`${API_BASE}/task/${taskId}`, {
    method: 'DELETE'
  });
  fetchTasks();
}

document.getElementById('task-form').onsubmit = e => {
  e.preventDefault();
  const taskInput = document.getElementById('task-input');
  const task = taskInput.value.trim();
  if (task) {
    addTask(task);
    taskInput.value = '';
  }
};

window.onload = fetchTasks;
