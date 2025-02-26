<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'
import SideBar from '@/components/SideBar.vue'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import type { HabitLog } from './HomeView.vue'
import router from '@/router'

const habitName = ref('')
const habitDescription = ref('')
const habitStore = useHabitStore()
const isNewHabit = ref('true')
const date = ref()

async function submitHabit() {
  if (!habitName.value) {
    alert("Veuillez entrer un nom d'habitude !")
    return
  }

  try {
    const formattedDates = date.value ? date.value.map((d: HabitLog) => ({ date: d })) : []
    const response = await axios.post('http://127.0.0.1:5000/habits', {
      name: habitName.value,
      description: habitDescription.value,
      habitLogs: formattedDates,
    })

    const newHabit = response.data.habit
    habitStore.habits.push({
      id: newHabit.id,
      name: newHabit.name,
      description: newHabit.description,
      creationDate: newHabit.creationDate,
      habitLogs: newHabit.habit_logs,
    })

    console.log('Réponse du serveur:', response.data)

    habitName.value = ''
    router.push({ name: 'home' })
  } catch (error) {
    console.error("Erreur lors de l'ajout de l'habitude:", error)
    alert('Une erreur est survenue.')
  }
}
</script>

<template>
  <div class="flex dark:bg-gray-600 h-screen">
    <SideBar />
    <div class="flex-1 p-8 ml-64">
      <div class="flex w-full justify-center">
        <form class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-lg w-full max-w-lg space-y-6">
          <h2 class="text-lg font-semibold text-gray-900 dark:text-white text-center">
            Nouvelle habitude
          </h2>

          <div class="grid gap-4">
            <div class="flex flex-col">
              <label for="name" class="text-gray-900 dark:text-white">Nom de l'habitude :</label>
              <input
                v-model="habitName"
                type="text"
                name="name"
                maxlength="25"
                class="mt-1 p-2 border focus:ring-0 rounded-lg focus:ring-sen-gray focus:border-sen-gray bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:text-white outline-none"
              />
            </div>

            <div class="flex flex-col">
              <label for="description" class="text-gray-900 dark:text-white">Description :</label>
              <input
                v-model="habitDescription"
                type="text"
                name="description"
                maxlength="40"
                class="mt-1 p-2 border rounded-lg focus:ring-sen-gray focus:border-sen-gray bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:text-white outline-none"
              />
            </div>

            <div class="flex items-center space-x-3">
              <input
                checked
                type="radio"
                value="true"
                name="habit-start"
                v-model="isNewHabit"
                class="w-4 h-4 text-blue-600 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="today" class="text-gray-900 dark:text-gray-300"
                >Commence aujourd'hui</label
              >
            </div>
            <div class="flex items-center space-x-3">
              <input
                type="radio"
                value="false"
                name="habit-start"
                v-model="isNewHabit"
                class="w-4 h-4 text-blue-600 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="already-started" class="text-gray-900 dark:text-gray-300"
                >A déjà commencé</label
              >
            </div>

            <div v-if="isNewHabit == 'false'">
              <label for="name" class="text-gray-900 dark:text-white"
                >Sélectionner une ou plusieurs dates :</label
              >
              <VueDatePicker v-model="date" multi-dates :enable-time-picker="false" class="mt-1" />
            </div>
          </div>

          <div class="flex justify-end space-x-3">
            <router-link :to="{ name: 'home' }">
              <button
                type="button"
                class="bg-sen-light_red text-white px-4 py-2 rounded-lg shadow-md hover:bg-sen-dark_red transition"
              >
                Retour
              </button>
            </router-link>
            <button
              @click.prevent="submitHabit"
              type="submit"
              class="bg-sen-light_green text-white px-4 py-2 rounded-lg shadow-md hover:bg-sen-dark_green transition"
            >
              Valider
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
