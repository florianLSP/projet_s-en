<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'
import { TrashIcon } from '@heroicons/vue/24/solid'

interface Habit {
  id: number
  name: string
}

const habits: Ref<Array<Habit>> = ref([])

async function deleteHabit(idHabit: number) {
  try {
    const response = await axios.delete(`http://127.0.0.1:5000/habit/${idHabit}`)

    console.log('Réponse du serveur:', response.data)
  } catch (error) {
    console.error("Erreur lors de la suppresion de l'habitude:", error)
    alert('Une erreur est survenue.')
  }
}

async function fetchHabits() {
  try {
    const response = await axios.get('http://127.0.0.1:5000/habits')
    habits.value = response.data
  } catch (error) {
    console.error('Erreur lors de la récupération des habitudes: ', error)
  }
}

onMounted(fetchHabits)
</script>

<template>
  <div class="ml-5 pt-5">
    <div>
      <router-link :to="{ name: 'habit-form' }">
        <button
          class="inline-flex items-center gap-x-1.5 rounded-md bg-gray-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 cursor-pointer"
        >
          Ajouter une nouvelle habitude
        </button>
      </router-link>
    </div>

    <div class="pt-5 w-96">
      <h2 class="text-2xl">Liste des habitudes:</h2>
      <ul>
        <li v-for="habit in habits" :key="habit.id" class="flex items-center">
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
</template>
