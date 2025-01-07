<template>
    <div>
      <h2>Tasks</h2>
      <ul>
        <li v-for="task in tasks" :key="task.id">
          {{ task.title }} - {{ task.status }}
        </li>
      </ul>
    </div>
</template>
  
<script>
  import axios from 'axios'
  
  export default {
    name: 'TaskList',
    data() {
      return {
        tasks: [],
      }
    },
    created() {
      axios.get('http://127.0.0.1:8000/api/tasks/')
        .then(response => {
          this.tasks = response.data
        })
        .catch(error => {
          console.error('There was an error fetching tasks:', error)
        })
    }
  }
</script>
  
<style scoped>
</style>