<script setup>
  import { ref } from 'vue'

  const productCategories = ref([
    {
      id: '01',
      name: 'Foundation',
      url: '../assets/product_categories/foundation.jpeg'
    },
    {
      id: '02',
      name: 'Concealer',
      url: '../assets/product_categories/concealer.png'
    },
    {
      id: '03',
      name: 'Lipstick',
      url: '../assets/product_categories/lipstick.png'
    },
    {
      id: '04',
      name: 'Powder',
      url: '../assets/product_categories/powder2.jpg'
    },
  ])

  const featuredBrands = ref([
    {
      id: '01',
      brandName: 'Fenty',
      url: '../assets/brand_logos/fenty.png'
    },
    {
      id: '02',
      brandName: 'House Of Tara',
      url: '../assets/brand_logos/house_of_tara.png'
    },
    {
      id: '03',
      brandName: 'Hegai & Esther',
      url: '../assets/brand_logos/hegai_and_esther.png'
    },
    {
      id: '04',
      brandName: 'Hegai & Esther',
      url: '../assets/brand_logos/hegai_and_esther2.png'
    },
    {
      id: '05',
      brandName: 'Elsa\'s Pro',
      url: '../assets/brand_logos/elsas_pro.png'
    },
  ])

  const getUrl = (url) => {
    return new URL(`${url}`, import.meta.url).href
  }
</script>

<template>
  <div class="mt-auto w-full">
    <div>
      <div class="text-center relative" :style="{ height: '70vh' }">
        <button class="bg-black px-48 py-10 text-4xl absolute bottom-60 md:bottom-14 left-1/2 transform -translate-x-1/2">BEAUTY LENS</button>
        <img class="w-full object-fit max-w-full max-h-full" src="../assets/home/hero-image.png">
      </div>
      
      <div class="md:inline-flex md:flex-row text-left mx-16 md:mt-14 sm:mb-8 sm:relative md:gap-x-6 items-center">
        <img class="w-80 h-80" src="../assets/home/makeup-tools.png" alt="">
        <div class="relative h-80">
          <p class="mt-8 md:mt-0 text-5xl md:text-4xl font-normal">BEAUTY LENS</p>
          <p class="text-2xl lg:text-3xl font-normal mt-4 md:mt-10 tracking-wider">
            Welcome to BeautyLens, your personal makeup recommendation expert.<br>
            Discover the perfect makeup products through the power of AI & unlock 
            the secrets to precise beauty tailored just for you!
            <br>Try BeautyLens today and experience a world of personalized
            makeup product recommendations.
          </p>
        </div>
      </div> 

      <div class="mt-12 lg:mt-0 md:flex md:flex-col">
        <div class="font-normal mt-12 mx-auto p-4">
          <p class="text-center text-4xl underline underline-offset-4 md:no-underline">PRODUCT CATEGORIES</p>
          <div class="mt-8 md:inline-flex md:flex-row gap-10">
            <div v-for="category in productCategories" :key="category.id">
              <img class="w-72 h-72 object-fill mx-auto" :src="getUrl(category.url)" alt="">
              <p class="mt-8 mb-4 md:mb-0 text-center md:text-left text-3xl">{{ category.name }}</p>
            </div>
          </div>
        </div>

        <div class="font-normal mt-12 mx-auto p-4">
          <p class="md:mt-8 text-center text-4xl underline underline-offset-4 md:no-underline">FEATURED BRANDS</p>
          <div class="mt-8 md:inline-flex md:flex-row gap-10">
            <div v-for="brand in featuredBrands" :key="brand.id">
              <img class="w-60 h-60 rounded-full mx-auto" :src="getUrl(brand.url)" alt="">
              <p class="mt-8 mb-4 md:mb-0 text-4xl text-center">{{ brand.brandName }}</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
