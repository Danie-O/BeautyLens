<script setup></script>

<!-- <template>
    <div class="relative">
        <h1 class="mt-[15%] text-2xl border border-black">Not found!</h1>
    </div>
</template> -->

<template>
    <div class="relative">
        <div class="mt-[35%] sm:mt-[25%] md:mt-[15%] text-center justify-center items-center p-16">
            <p class="text-5xl text-title-text-color">Oops! The page you tried to access cannot be found!</p>
            <button @click="$router.back()" class="p-6 mt-8 bg-black rounded-full text-2xl font-medium text-white cursor-pointer">Go Back</button>
        </div>
    </div>
</template>