import { createRouter, createMemoryHistory } from 'vue-router'

const router = createRouter({
    history: createMemoryHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: () => import('../components/tablero.vue')
        },
        {
            path: '/usuarios',
            component: () => import('../components/usuarios.vue')
        },
    ],
})

export default router
