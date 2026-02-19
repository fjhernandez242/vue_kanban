// Url base
export const API_BASE_URL = 'http://localhost:8000';
// Urls endpoint
export const URLS = {
    // Url para listar todos los trabajos
    LISTAR_TRABAJOS: `${API_BASE_URL}/tablero/trabajos`,
    // Url para cambiar número lista de un trabajo
    CAMBIAR_POSICION: `${API_BASE_URL}/tablero/posicion`,
    // Obtiene todos los usuarios
    LISTAR_USUARIOS: `${API_BASE_URL}/usuarios/getAll`,
    // Cargar nuevo trabajo
    CARGAR_TRABAJO: `${API_BASE_URL}/tablero/cargar`,
    // Carga trabajo por ID
    CARGAR_TRABAJOID: `${API_BASE_URL}/tablero/trabajo_id`,
};