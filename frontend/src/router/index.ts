import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HabitFormView from '@/views/HabitFormView.vue'
import HabitDetailsView from '@/views/HabitDetailsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/habit',
      name: 'habit-form',
      component: HabitFormView,
    },
    {
      path: '/habit/:id',
      name: 'habit-details',
      component: HabitDetailsView,
    },
  ],
})

export default router
