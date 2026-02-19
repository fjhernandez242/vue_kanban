import { URLS } from "@/config/api-urls";

// Obtiene todos los usuarios
export function getUsuarios() {
     return fetch(URLS.LISTAR_USUARIOS, {
        headers: {
            'Authorization': "Token 9f3145aa21fbdee1094a6c80bbc0bd9e6ed08fbc"
        }
    }).then(
        (response) => {
            if (!response.ok) {
                throw new Error('Error al cargar los usuarios: ' + response.statusText);
            }
            return response.json()
        }
    )
}