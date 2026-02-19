<script setup>
import { ref } from 'vue';

const currentActive = ref('Tablero');
// Función para realizar el cambio de la pantalla activa
const setActive = (tabName) => {
    currentActive.value = tabName;
};
</script>

<template>
    <ul class="nav nav-underline">
        <li class="nav-item">
            <RouterLink class="nav-link"
            :class="{ 'active': currentActive == 'Tablero'}"
            @click="setActive('Tablero')"
            aria-current="page" to="/">Tablero</RouterLink>
        </li>
        <li class="nav-item">
            <RouterLink class="nav-link"
            :class="{ 'active': currentActive == 'Usuarios'}"
            @click="setActive('Usuarios')"
            to="/usuarios">Empleados</RouterLink>
        </li>
    </ul>
</template>

<style scoped>
.nav {
    background-color: #40749e;
    padding: 5px;
    font-weight: bold;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}

.nav-link {
    color: aliceblue;
}
</style>