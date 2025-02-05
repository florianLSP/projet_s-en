<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'

interface Habit {
  id: number
  name: string
}

const habits: Ref<Array<Habit>> = ref([])

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
        <li v-for="habit in habits" :key="habit.id">
          {{ habit.name }}
        </li>
      </ul>
    </div>
  </div>
</template>
