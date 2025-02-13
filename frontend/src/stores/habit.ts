import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Habit } from '@/views/HomeView.vue'

export const useHabitStore = defineStore('habit', () => {
  const habit: Ref<Array<Habit>> = ref([])

  return {
    habit,
  }
})
