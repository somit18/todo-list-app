function openEditModal(taskId, taskContent) {
    const form = document.getElementById('editForm');
    const input = document.getElementById('editTaskInput');

    form.action = `/edit/${taskId}`;
    input.value = taskContent;

    const modal = new bootstrap.Modal(document.getElementById('editTaskModal'));
    modal.show();
}

