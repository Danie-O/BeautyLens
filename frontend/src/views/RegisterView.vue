<script setup>
    const registerUser = () => {
        console.log("register now")
    }
</script>

<template>
    <div class="mx-auto min-w-screen-md md:max-w-screen-xl px-8 py-3">
        <div class="relative md:grid grid-cols-1 md:grid-cols-2 md:gap-3">
                <div>
                    <img class="w-full h-full hidden md:block object-contain" src="../assets/login-image.png" alt="Login image">
                </div>

                <div class="items-center">
                    <div class="mx-auto">
                        <div>
                            <img class="mt-12 left-1/2 transform -translate-x-1/2 relative" src="../components/logo.svg" alt="CompanyLogo">
                            <p class="mt-3 text-[#D39371] text-3xl text-center">WELCOME BACK</p>
                            <button class="mt-8 bg-zinc-300 w-[80%] px-8 py-3 left-1/2 transform -translate-x-1/2 relative flex items-center justify-center gap-8 text-black text-xl font-normal hover:bg-[#D39371]" 
                                    type="button">
                                <img src="../assets/icons/google-colored.png" alt="Google Icon" class="w-6 h-6">
                                <span>Register with Google</span>
                            </button>
                        </div>
                        
                        <div class="text-center mt-16 mb-12 relative">
                            <div class="flex items-center mx-24">
                              <div class="flex-1 border-t border-[#D39371]"></div>
                              <span class="mx-4 text-[#D39371] text-xl px-2">OR</span>
                              <div class="flex-1 border-t border-[#D39371]"></div>
                            </div>
                        </div>
                          
                        <form class="text-black text-xl font-normal" @submit.prevent="registerUser" action="" method="post">
                            <div class="flex items-center">
                                <!-- <img class="bg-white p-2" src="../assets/icons/black-email-icon.png" alt=""> -->
                                <input class="bg-zinc-300 p-3 w-[80%] left-1/2 transform -translate-x-1/2 relative placeholder-black" 
                                        type="email" name="email" placeholder="Email"
                                >
                            </div>

                            <div class="flex items-center mt-12">
                                <!-- <img class="bg-white p-2" src="../assets/icons/lock-icon.png" alt=""> -->
                                <input class="bg-zinc-300 p-3 w-[80%] left-1/2 transform -translate-x-1/2 relative placeholder-black" 
                                        type="password" name="password" placeholder="Password"
                                >
                                <!-- <img class="" src="../assets/icons/privacy-icon.png" alt=""> -->
                            </div>

                            <div class="flex items-center mt-12">
                                <!-- <img class="bg-white p-2" src="../assets/icons/lock-icon.png" alt=""> -->
                                <input class="bg-zinc-300 p-3 w-[80%] left-1/2 transform -translate-x-1/2 relative placeholder-black" 
                                        type="password" name="password" placeholder="Confirm Password"
                                >
                                <!-- <img class="" src="../assets/icons/privacy-icon.png" alt=""> -->
                            </div>

                            <button class="mt-16 text-center font-semibold w-[80%] left-1/2 transform -translate-x-1/2 relative px-12 py-3 bg-[#D39371] hover:bg-zinc-300" type="submit">Register</button>

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