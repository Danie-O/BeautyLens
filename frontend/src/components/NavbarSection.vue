<script setup>
</script>

<template>
    <div>
        <nav class="mt-6 h-16 px-14 py-6 m-auto grid grid-cols-2 md:flex md:justify-between md:items-center relative">
            <img class="md:mt-6" src="./logo.svg" alt="">

            <div class="relative text-2xl font-normal text-center leading-loose">
                <ul class="inline-flex justify-between gap-6 right-[30%] relative">
                    <router-link :to="{ name: 'home' }">Home</router-link>
                    <router-link :to="{ name: 'shop' }">Shop</router-link>
                    <router-link :to="{ name: 'blog' }">Blog</router-link>
                    <router-link :to="{ name: 'contact' }">Contact Us</router-link>
                    <router-link :to="{ name: 'about' }">About Us</router-link>
                </ul>
                <!-- <div class="hidden ml-14 md:inline-flex md:justify-between gap-6">
                    <button class="bg-[#D39371] px-4 text-xl font-semibold rounded-3xl" type="button"><router-link :to="{ name: 'login' }">Login</router-link></button>
                    <button class="bg-[#D39371] px-4 text-xl font-semibold rounded-3xl" type="button"><router-link :to="{ name: 'register' }">Register</router-link></button>
                </div> -->
            </div>
        </nav>
    </div>
</template>

<style scoped>
    nav a.router-link-exact-active {
        color: #D39371;
    }
</style>