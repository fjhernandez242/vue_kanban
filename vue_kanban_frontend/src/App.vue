<script setup>
// Importa Header
import headerVue from './components/shared/header.vue'
</script>

<template>
    <section>
        <headerVue />
        <main>
            <router-view />
        </main>
    </section>
</template>

<style scoped></style>
