<template>
    <div>
      <h2>Add New Task</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="title">Title:</label>
          <input
            type="text"
            id="title"
            v-model="task.title"
            required
          />
        </div>
        <div>
          <label for="description">Description:</label>
          <textarea
            id="description"
            v-model="task.description"
            required
          ></textarea>
        </div>
        <div>
          <label for="status">Status:</label>
          <select id="status" v-model="task.status" required>
            <option value="todo">To Do</option>
            <option value="in-progress">In Progress</option>
            <option value="done">Done</option>
          </select>
        </div>
        <button type="submit">Add Task</button>
      </form>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    name: "TaskForm",
    data() {
      return {
        task: {
          title: "",
          description: "",
          status: "todo",
        },
      };
    },
    methods: {
      async submitForm() {
        try {
          const response = await api.post("/tasks/", this.task);
          console.log("Task added:", response.data);

          this.task = {
            title: "",
            description: "",
            status: "todo",
          };
  
          this.$emit("task-added", response.data);
        } catch (error) {
          console.error("Error adding task:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  button {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  