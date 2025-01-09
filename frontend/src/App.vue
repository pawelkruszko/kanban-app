<template>
    <div id="app">
      <TaskList />
    </div>
  </template>
  
  <script>
  import TaskList from "./components/TaskList.vue";
  
  export default {
    name: "App",
    components: {
      TaskList,
    },
  };
  </script>
  
  <style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  </style>
  