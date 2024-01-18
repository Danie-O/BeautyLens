<script setup>
    import { ref } from 'vue'

    const password = ref("")
    const showPassword = ref(false)
    const passwordFieldType = ref('password')
    
    const togglePasswordVisibility = () => {
        showPassword.value = !showPassword.value
        passwordFieldType.value = passwordFieldType.value === "password" ? "text": "password"
    }

    const registerUser = () => {
        console.log("login now")
    }
</script>

<template>
    <div class="mx-auto h-full flex flex-col overflow-hidden min-w-screen-md md:max-w-screen-xl px-8 py-8">
        <div class="relative md:grid grid-cols-1 md:grid-cols-2 md:gap-x-3 flex">
                <div>
                    <img class="w-full h-full min-h-screen px-2 hidden md:block object-fill" src="../assets/login-image.png" alt="Login image">
                </div>

                <div class="items-center flex-grow">
                    <div class="mx-auto h-full min-h-screen">
                        <div>
                            <img class="mt-12 left-1/2 transform -translate-x-1/2 relative" src="../components/logo.svg" alt="CompanyLogo">
                            <p class="mt-3 text-[#D39371] text-3xl text-center">SIGN UP</p>
                            <button class="mt-8 bg-zinc-300 w-[80%] px-8 py-3 left-1/2 transform -translate-x-1/2 relative flex items-center justify-center gap-8 text-black text-xl font-normal hover:bg-[#D39371]" 
                                    type="button">
                                <img src="../assets/icons/google-colored.png" alt="google-icon" class="w-6 h-6">
                                <span>Sign up with Google</span>
                            </button>
                        </div>
                        
                        <div class="text-center mt-12 mb-12 relative">
                            <div class="flex items-center mx-24">
                              <div class="flex-1 border-t border-[#D39371]"></div>
                              <span class="mx-4 text-[#D39371] text-xl px-2">OR</span>
                              <div class="flex-1 border-t border-[#D39371]"></div>
                            </div>
                        </div>
                          
                        <form class="text-black text-xl font-normal" @submit.prevent="registerUser" action="" method="post">
                            <div class="flex items-center">
                                <div class="bg-zinc-300 flex w-[80%] left-1/2 transform -translate-x-1/2 relative">
                                    <img class="p-3" src="../assets/icons/user-icon.png" alt="email-icon">
                                    <input class="bg-zinc-300 p-3 w-[80%] placeholder-black outline-none" 
                                        type="text" name="username" placeholder="Username"
                                        autocomplete="off"
                                    >
                                </div>
                            </div>

                            <div class="flex items-center mt-12">
                                <div class="bg-zinc-300 flex w-[80%] left-1/2 transform -translate-x-1/2 relative">
                                    <img class="p-3" src="../assets/icons/black-email-icon.png" alt="email-icon">
                                    <input class="bg-zinc-300 p-3 w-[80%] placeholder-black outline-none" 
                                        type="email" name="email" placeholder="Email"
                                        autocomplete="off"
                                    >
                                </div>
                            </div>

                            <div class="flex items-center mt-12">
                                <div class="bg-zinc-300 flex w-[80%] left-1/2 transform -translate-x-1/2 relative placeholder-black">
                                    <img class="p-3" src="../assets/icons/lock-icon.png" alt="password-icon">
                                    <input
                                        v-model="password"
                                        class="bg-zinc-300 p-3 w-[80%] placeholder-black outline-none" 
                                        :type="passwordFieldType"
                                        placeholder="Password"
                                    />
                                    <img
                                        v-if="!showPassword"
                                        @click="togglePasswordVisibility"
                                        class="p-3 cursor-pointer" 
                                        src="../assets/icons/no-privacy-icon.png"
                                        alt="no-password-privacy-icon"
                                    />
                                    <img
                                        v-else
                                        @click="togglePasswordVisibility"
                                        class="p-3 cursor-pointer" 
                                        src="../assets/icons/privacy-icon.png"
                                        alt="password-privacy-icon"
                                    />
                                </div>
                            </div>

                            <div class="text-[#D39371] grid grid-cols-2 justify-center mt-8 ml-[10%] w-[80%]">
                                <div class="inline-flex flex-row gap-2 items-center">
                                    <input class="h-8 w-8 bg-transparent bg-orange-600" type="checkbox" name="keep-logged-in" id="">
                                    <label class="hover:text-white" for="keep-logged-in">Terms & Conditions</label>
                                </div>
                            </div>

                            <button class="mt-16 text-center w-[80%] left-1/2 transform -translate-x-1/2 relative px-12 py-3 bg-zinc-300 hover:bg-[#D39371]" type="submit">Sign Up</button>
                        </form>
                    </div>
                    
                </div>
        </div>
    </div>
    
</template>

<style scoped>
input[type="checkbox"] {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    background: transparent;
    border: 2px solid white;
    padding: 0.5em;
    border-radius: 0.25rem;
  }

  /* Style for checked state */
  input[type="checkbox"]:checked {
    background-color: #d39371;
  }

  input[type="checkbox"]::before {
    content: '\2713';
    font-size: 1.5em;
    color: transparent;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  input[type="checkbox"]:checked::before {
    color: #000;
  }
</style>