<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { EllipsisHorizontalIcon } from '@heroicons/vue/24/solid'
import axios from 'axios'
import { useHabitStore } from '@/stores/habit'

const cardMenu = ref(false)
const habitStore = useHabitStore()

const props = defineProps({
  id: {
    type: Number,
    required: true,
  },
  name: String,
  description: String,
  creationDate: String,
})

function toggleMenu() {
  cardMenu.value = !cardMenu.value
}

function handleClickOutside(event: Event) {
  const target = event.target as HTMLElement
  if (!target.closest('.dropdown-wrapper')) {
    cardMenu.value = false
  }
}

async function deleteHabit(idHabit: Number) {
  try {
    const response = await axios.delete(`http://127.0.0.1:5000/habit/${idHabit}`)

    const index = habitStore.habits.findIndex((habit) => habit.id === idHabit)

    if (index !== -1) {
      habitStore.habits.splice(index, 1)
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

onMounted(() => {
  window.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  window.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div
    class="w-80 max-w-sm bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700"
  >
    <div class="flex justify-end px-4 pt-4 relative dropdown-wrapper">
      <button
        @click.stop="toggleMenu"
        class="inline-block text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-1.5"
        type="button"
      >
        <span class="sr-only">Open dropdown</span>
        <EllipsisHorizontalIcon class="w-5 h-5" />
      </button>

      <transition
        enter-active-class="transition-opacity duration-300"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition-opacity duration-300"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <div
          v-show="cardMenu"
          class="z-10 absolute left-36 mt-8 ml-24 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow-lg w-44 dark:bg-gray-700"
        >
          <ul class="py-2" aria-labelledby="dropdownButton">
            <li>
              <a
                href="#"
                class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
                >Edit</a
              >
            </li>
            <li
              @click="deleteHabit(props.id)"
              class="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"
            >
              Delete
            </li>
          </ul>
        </div>
      </transition>
    </div>
    <router-link :to="{ name: 'habit-details', params: { id: props.id } }">
      <div class="flex flex-col items-center pb-10">
        <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">
          {{ props.name }}
        </h5>
        <p class="text-sm text-gray-500 dark:text-gray-400">
          Date de création: {{ props.creationDate }}
        </p>
        <p>{{ props.description }}</p>
      </div>
    </router-link>
  </div>
</template>
