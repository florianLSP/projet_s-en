<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'
import { TrashIcon } from '@heroicons/vue/24/solid'
import { useHabitStore } from '@/stores/habit'
import SideBar from '@/components/SideBar.vue'

export interface Habit {
  id: number
  name: string
}

const habitStore = useHabitStore()

async function deleteHabit(idHabit: number) {
  try {
    const response = await axios.delete(`http://127.0.0.1:5000/habit/${idHabit}`)

    const index = habitStore.habit.findIndex((habit) => habit.id === idHabit)

    if (index !== -1) {
      habitStore.habit.splice(index, 1)
      console.log('Suppression effectuée!')
    } else {
      console.log("L'id n'a pas été trouvé.")
    }

    console.log('Réponse du serveur:', response.data)
  } catch (error) {
    console.error("Erreur lors de la suppresion de l'habitude:", error)
    alert('Une erreur est survenue.')
  }
}

async function fetchHabits() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/habits')
    habitStore.habit = response.data
  } catch (error) {
    console.error('Erreur lors de la récupération des habitudes: ', error)
  }
}

onMounted(fetchHabits)
</script>

<template>
  <div class="flex">
    <SideBar />
    <div class="flex-1 p-5 ml-64">
      <div class="flex flex-col pt-5 w-full items-center">
        <h2 class="text-2xl">Liste des habitudes:</h2>
        <ul>
          <li v-for="habit in habitStore.habit" :key="habit.id" class="flex items-center">
            {{ habit.id }}. {{ habit.name }}
            <button
              @click="deleteHabit(habit.id)"
              class="flex items-center justify-center ml-2 rounded-md bg-red-500 p-2 text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 cursor-pointer"
            >
              <TrashIcon class="h-5 w-5" />
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
