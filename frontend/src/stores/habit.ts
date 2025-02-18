import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Habit } from '@/views/HomeView.vue'

export const useHabitStore = defineStore('habit', () => {
  const habits: Ref<Array<Habit>> = ref([])
  const selectedHabit: Ref<Habit | undefined> = ref()

  return {
    habits,
    selectedHabit,
  }
})
