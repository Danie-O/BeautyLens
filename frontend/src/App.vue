<script setup>
import { RouterView } from 'vue-router'
import NavbarSection from './components/NavbarSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <body class="flex flex-col w-full h-full min-h-screen m-auto bg-black overflow-hidden">
    <NavbarSection :class="{ 'hidden' : $route.name === 'login' || $route.name === 'register' || $route.name === 'not-found' || $route.name === 'network-error' }"/>

    <RouterView/>

    <FooterSection :class="{ 'hidden' : $route.name === 'login' || $route.name === 'register' || $route.name === 'not-found' || $route.name === 'network-error' }"/>
  </body>
</template>

<style scoped>

</style>
