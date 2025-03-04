<script setup lang="ts">
import { onMounted } from 'vue'
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'
import SideBar from '@/components/SideBar.vue'
import HabitCard from '@/components/HabitCard.vue'

export interface Habit {
  id: number
  name: string
  description: string
  creationDate: string
  habitLogs: Array<HabitLog>
  emoji: string
}

export interface HabitLog {
  id: number
  date: string
}

const habitStore = useHabitStore()

async function fetchHabits() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/habits')
    habitStore.habits = response.data
  } catch (error) {
    console.error('Erreur lors de la récupération des habitudes: ', error)
  }
}

onMounted(fetchHabits)
</script>

<template>
  <div class="flex dark:bg-gray-600 h-screen">
    <SideBar />
    <div class="flex-1 p-5 ml-64">
      <div class="flex pt-5 w-full justify-center dark:text-white">
        <div v-for="habit in habitStore.habits" :key="habit.id" class="flex items-center pt-2 px-6">
          <HabitCard
            class="cursor-pointer transition-transform transform hover:scale-105 hover:dark:border-gray-500"
            :id="habit.id"
            :name="habit.name"
            :description="habit.description"
            :creationDate="habit.creationDate"
            :logs="habit.habitLogs"
            :emoji="habit.emoji"
          />
        </div>
      </div>
    </div>
  </div>
</template>
