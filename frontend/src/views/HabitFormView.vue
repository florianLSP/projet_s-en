<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'
import SideBar from '@/components/SideBar.vue'

const habitName = ref('')
const habitStore = useHabitStore()

async function submitHabit() {
  if (!habitName.value) {
    alert("Veuillez entrer un nom d'habitude !")
    return
  }

  try {
    const response = await axios.post('http://127.0.0.1:5000/habits', {
      name: habitName.value,
    })

    const newHabit = response.data.habit
    habitStore.habit.push({ id: newHabit.id, name: newHabit.name })

    console.log('Réponse du serveur:', response.data)

    habitName.value = ''
  } catch (error) {
    console.error("Erreur lors de l'ajout de l'habitude:", error)
    alert('Une erreur est survenue.')
  }
}
</script>

<template>
  <div class="flex dark:bg-gray-600 h-screen">
    <SideBar />
    <div class="flex-1 p-5 ml-64">
      <div class="flex pt-5 w-full justify-center">
        <form>
          <div class="flex w-full items-center space-x-2">
            <label for="name" class="text-gray-900 dark:text-white whitespace-nowrap"
              >Nom de l'habitude:</label
            >
            <input
              v-model="habitName"
              type="text"
              name="name"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            />
          </div>

          <router-link :to="{ name: 'home' }">
            <input
              @click="submitHabit()"
              type="button"
              value="Retour"
              class="inline-flex items-center gap-x-1.5 rounded-md bg-gray-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 cursor-pointer mt-5"
            />
          </router-link>
          <router-link :to="{ name: 'home' }">
            <input
              @click="submitHabit()"
              type="submit"
              value="Valider"
              class="inline-flex items-center gap-x-1.5 rounded-md bg-gray-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 cursor-pointer mt-5"
            />
          </router-link>
        </form>
      </div>
    </div>
  </div>
</template>
