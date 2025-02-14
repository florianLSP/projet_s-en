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
  <div class="ml-5 pt-5">
    <SideBar />
    <div>
      <router-link :to="{ name: 'home' }">
        <button
          class="inline-flex items-center gap-x-1.5 rounded-md bg-gray-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 cursor-pointer"
        >
          Accueil
        </button>
      </router-link>
    </div>

    <div class="pt-5 w-96">
      <form>
        <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >Nom de l'habitude:</label
        >
        <input
          v-model="habitName"
          type="text"
          name="name"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />

        <router-link :to="{ name: 'home' }">
          <input
            @click="submitHabit()"
            type="submit"
            value="Submit"
            class="inline-flex items-center gap-x-1.5 rounded-md bg-gray-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-700 cursor-pointer mt-5"
          />
        </router-link>
      </form>
    </div>
  </div>
</template>
