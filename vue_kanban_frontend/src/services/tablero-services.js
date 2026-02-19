import { URLS } from "@/config/api-urls";

// Lista todos los trabajos
export function getListarTablero() {
    return fetch(URLS.LISTAR_TRABAJOS, {
        headers: {
            'Authorization': "Token 9f3145aa21fbdee1094a6c80bbc0bd9e6ed08fbc"
        }
    }).then(
        (response) => {
            if (!response.ok) {
                throw new Error('Error al cargar los trabajos: ' + response.statusText);
            }
            return response.json()
        }
    )
}

// Obtiene el trabajo por ID
export function getTrabajoID(id) {
    return fetch(URLS.CARGAR_TRABAJOID, {
        method: 'POST',
        body: JSON.stringify({
            "id": id,
        }),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Token 9f3145aa21fbdee1094a6c80bbc0bd9e6ed08fbc"
        }
    }).then(
        (response) => {
            if (!response.ok) {
                throw new Error('Error al cargar los trabajo: ' + response.statusText);
            }
            return response.json()
        }
    )
}
// Cambia la posición de lista del trabajo
export function SetterPosicionTablero(params) {
    return fetch(URLS.CAMBIAR_POSICION, {
        method: 'POST',
        body: JSON.stringify({
            "guia": params.guia,
            "posicion": params.posicion
        }),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Token 9f3145aa21fbdee1094a6c80bbc0bd9e6ed08fbc"
        }
    }).then(
        (response) => {
            if (!response.ok) {
                // Mejora: Es útil incluir el body de error si es posible
                return response.json().then(errorData => {
                    throw new Error(`Error ${response.status}: ${JSON.stringify(errorData)}`);
                });
            }
            return response.json();
        }
    )
}

// Servicio para cargar nuevo trabajo
export function CargarTrabajo(params) {

    const formData = new FormData();
    formData.append("guia", params.guia);
    formData.append("recibio", params.recibio);
    formData.append("lista", params.lista);
    formData.append("desc", params.desc);
    formData.append("estado", params.estado);
    formData.append("cliente", params.cliente);
    formData.append("imagen", params.imagen);

    return fetch(URLS.CARGAR_TRABAJO, {
        method: 'POST',
        body: formData,
        headers: {
            // 'Content-Type': 'application/json',
            'Authorization': "Token 9f3145aa21fbdee1094a6c80bbc0bd9e6ed08fbc"
        }
    }).then(
        (response) => {
            if (!response.ok) {
                // Mejora: Es útil incluir el body de error si es posible
                return response.json().then(errorData => {
                    throw new Error(`Error ${response.status}: ${JSON.stringify(errorData)}`);
                });
            }
            return response.json();
        }
    )

}