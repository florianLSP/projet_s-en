<script setup lang="ts">
import SideBar from '@/components/SideBar.vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'
import { onMounted } from 'vue'

const route = useRoute()
const habitStore = useHabitStore()

async function fetchHabits() {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/habit/${route.params.id}`)
    habitStore.selectedHabit = response.data
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
      <div
        v-if="habitStore.selectedHabit"
        class="flex flex-col pt-5 w-full items-center dark:text-white"
      >
        <ul>
          <li>{{ habitStore.selectedHabit.name }}</li>
          <li>{{ habitStore.selectedHabit.description }}</li>
          <li>{{ habitStore.selectedHabit.creationDate }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>
