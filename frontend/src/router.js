import { createRouter, createWebHistory } from 'vue-router'
import TaskList from './components/TaskList.vue'

const routes = [
  {
    path: '/',
    name: 'TaskList',
    component: TaskList
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router