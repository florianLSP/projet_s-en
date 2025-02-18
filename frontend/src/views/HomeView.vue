<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'
import { TrashIcon } from '@heroicons/vue/24/solid'
import { useHabitStore } from '@/stores/habit'
import SideBar from '@/components/SideBar.vue'
import HabitCard from '@/components/HabitCard.vue'

export interface Habit {
  id: number
  name: string
  description: string
  creationDate: string
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

function formatDate(dateString: string) {
  return new Date(dateString).toLocaleDateString('fr-FR', {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
  })
}

onMounted(fetchHabits)
</script>

<template>
  <div class="flex dark:bg-gray-600 h-screen">
    <SideBar />
    <div class="flex-1 p-5 ml-64">
      <div class="flex pt-5 w-full justify-center dark:text-white">
        <div v-for="habit in habitStore.habits" :key="habit.id" class="flex items-center pt-2 px-6">
          <router-link :to="{ name: 'habit-details', params: { id: habit.id } }">
            <HabitCard
              class="cursor-pointer"
              :id="habit.id"
              :name="habit.name"
              :description="habit.description"
              :creationDate="formatDate(habit.creationDate)"
            />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
