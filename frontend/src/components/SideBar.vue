<script setup lang="ts">
import { HomeIcon, PlusCircleIcon } from '@heroicons/vue/24/outline'
</script>

<template>
  <!-- Container for sidebar and main content -->
  <div class="flex">
    <!-- Sidebar -->
    <aside
      id="default-sidebar"
      class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
      aria-label="Sidebar"
    >
      <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
        <ul class="space-y-2 font-medium">
          <router-link :to="{ name: 'home' }">
            <li
              class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"
            >
              <HomeIcon class="w-5 h-5" />
              <span class="ms-3">Accueil</span>
            </li></router-link
          >
          <router-link :to="{ name: 'habit-form' }">
            <li
              class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"
            >
              <PlusCircleIcon class="w-5 h-5" />
              <span class="ms-3">Nouvelle habitude</span>
            </li></router-link
          >
        </ul>
      </div>
    </aside>
  </div>
</template>
