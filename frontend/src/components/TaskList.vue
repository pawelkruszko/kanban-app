<template>
    <div>
      <h1>Task List</h1>
  
      <TaskForm @task-added="fetchTasks" />
  
      <div v-if="tasks.length">
        <ul>
          <li v-for="task in tasks" :key="task.id">
            <strong>{{ task.title }}</strong> - {{ task.status }}
            <p>{{ task.description }}</p>
          </li>
        </ul>
      </div>
      <p v-else>No tasks available.</p>
    </div>
  </template>
  
  <script>
  import TaskForm from "./TaskForm.vue";
  import api from "../services/api";
  
  export default {
    name: "TaskList",
    components: {
      TaskForm,
    },
    data() {
      return {
        tasks: [],
      };
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await api.get("/tasks/");
          this.tasks = response.data;
        } catch (error) {
          console.error("Error fetching tasks:", error);
        }
      },
    },
    created() {
      this.fetchTasks();
    },
  };
  </script>
  
  <style scoped>
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    margin: 1rem 0;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  li strong {
    color: #007bff;
  }
  
  li p {
    margin: 0.5rem 0 0;
  }
  </style>
  