<template>
     <Transition name="fade-slide">
        <div v-if="props.visible" class="modal" id="trabajoModal" tabindex="-1" aria-labelledby="trabajoModalLabel"
            style="display: block;" aria-modal="true" role="dialog">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="trabajoModalLabel">Carga tarea</h1>
                        <button type="button" class="btn-close" @click="handleClose()" aria-label="Close"></button>
                    </div>
                    <div class="modal-body d-flex">
                        <div class="card h-100">
                            <div class="card-body">
                                <form @submit.prevent="nuevoTrabajo" class="row g-3 needs-validation" novalidate>
                                    <div class="col-md-6">
                                        <label for="presupuesto" class="form-label">Presupuesto</label>
                                        <input type="text" class="form-control limpiarCampo" name="presupuesto" id="presupuesto"
                                            v-model="v_presupuesto" v-bind:disabled="modificar" required>
                                        <div class="invalid-feedback">
                                        Por favor indique el presupuesto de referencia!
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="recibio" class="form-label">¿Quién recibio?</label>
                                        <select class="form-select" id="recibio" v-model="v_recibio" required>
                                            <option v-for="usuarios in usuariosApi" :value="usuarios.id">
                                                {{ usuarios.first_name }} {{ usuarios.last_name }}
                                            </option>
                                        </select>
                                        <div class="invalid-feedback">
                                        Por favor indique quien recibio el producto.
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="cliente" class="form-label">Referencia del cliente</label>
                                        <input type="text" class="form-control limpiarCampo" id="cliente" v-model="v_cliente" required>
                                        <div class="invalid-feedback">
                                        Por favor ingrese la referencia del cliente.
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="estado" class="form-label">Estado</label>
                                        <select class="form-select" id="estado" v-model="v_estado" required>
                                            <option v-for="estado in opcion_estado" :value="estado.value" >
                                                {{ estado.text }}
                                            </option>
                                        </select>
                                        <div class="invalid-feedback">
                                        Por favor indique el estado.
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="desc" class="form-label">Descripción</label>
                                        <textarea class="form-control limpiarCampo" id="desc" v-model="v_desc" required></textarea>
                                        <div class="invalid-feedback">
                                        Por favor agergue una descripción.
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="img_ref" class="form-label">Imagen</label>
                                        <input type="file" id="img_ref" class="form-control limpiarCampo" ref="archivoInput">
                                    </div>
                                    <div class="col-md-7"></div>
                                    <div class="col-md-5 d-flex btn-group">
                                        <button type="submit" class="btn btn-success" :disabled="enviando">
                                            {{ enviando ? 'Cargando...' : textoBoton }}
                                        </button>
                                        <button type="button" class="btn btn-secondary ms-2" @click="handleClose()">Cerrar</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="card h-100">
                            <div class="card-headr">
                                <span>Imagen</span>
                            </div>
                            <div class="card-body">
                                <img src="/src/img/fondo2.jpg" alt="" id="imgEdit">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Transition>
</template>


<script setup>
import { readonly, ref, watch } from 'vue';
import { getUsuarios } from '@/services/usuarios-services';
import { CargarTrabajo, getTrabajoID } from '@/services/tablero-services';
import { alertSuccess } from '@/assets/notifications';
import Swal from 'sweetalert2';

// Declaración Variables
const v_presupuesto = defineModel('presupuesto');
const v_recibio = defineModel('recibio');
const v_cliente = defineModel('cliente');
const v_desc = defineModel('desc');
const v_estado = ref(1);
// Variable para imagen
const archivoInput = ref(null);
// Bandera para diseño de botón
const enviando = ref(false);
// Variable para texto de botón
const textoBoton = ref('Cargar tarea');
// bandera para identificación de edición
const modificar = ref(false);
// Define Props
const props = defineProps({
    editarId: {
        type: [Number, String, null],
        default: null
    }, visible: {
        type: Boolean,
        default: false
    }
});
// Define emits
const emit = defineEmits(['cerrar-modal', 'trabajo-agregado']);
// Variable reactiva par ID dentro del modal
const idLocal = ref(null);

// API usuarios
const usuariosApi = ref([])
getUsuarios().then(
        (data) => {
            usuariosApi.value = data.usuarios;
        }
).catch(error => {
    console.error("Error al obtener los datos:", error);
    // Manejo de errores (mostrar mensaje al usuario)
});

function trabajoByID(newId) {
    getTrabajoID(newId).then(
        (response) => {
            console.log(response.trabajo);
            v_presupuesto.value = response.trabajo.guia
            v_recibio.value = response.trabajo.recibio
            v_cliente.value = response.trabajo.cliente
            v_desc.value = response.trabajo.desc
            v_estado.value = response.trabajo.lista
            // Cambia texto de botón
            textoBoton.value = 'Editar tarea';
            modificar.value = true;
        }
    );
}
// 4. Observador (watcher) para reaccionar cuando el ID o la visibilidad cambian
watch(
    () => props.editarId,
    (newId) => {
        if (newId) {
            // Lógica para cargar los datos del trabajo con este ID
            idLocal.value = newId;
            trabajoByID(newId);
        } else {
            // Modo agregar: limpiar o preparar el formulario
            idLocal.value = null;
        }
    },
    { immediate: true } // Ejecutar inmediatamente la primera vez
);

// Función para cerrar el modal y notificar al padre
function handleClose() {
    cerrarmodal();
    emit('cerrar-modal');
}

const opcion_estado = ref([
  { text: 'Recepción', value: 1 },
  { text: 'Revisión', value: 2 },
  { text: 'Reparación', value: 3 },
  { text: 'Entregado', value: 4 }
])

// Define un Emit
// Carga de trabajo
async function nuevoTrabajo() {
    // Cambia estado de boton a Enviando...
    enviando.value = true
    // Captura datos
    const trabajo = {
        "guia": v_presupuesto.value,
        "recibio": v_recibio.value,
        "lista": v_estado.value,
        "desc": v_desc.value,
        "estado": v_estado.value,
        "cliente": v_cliente.value,
        "imagen": archivoInput.value.files[0]
    }

    CargarTrabajo(trabajo).then(
        (response) => {
            if (response.error) {
                Swal.fire({
                    title: "¡Duplicado!",
                    text: response.error,
                    icon: 'info',
                    showCancelButton: true,
                    confirmButtonText: 'Editar información'
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Cambia estado de boton a Enviando...
                        enviando.value = false
                    }
                    if (result.dismiss) {
                        const $modal = $('#trabajoModal');
                        $modal.on('hidden.bs.modal', function () {
                            const backdrop = document.querySelector('.modal-backdrop');
                            if (backdrop) {
                                // Elimina el elemento del DOM
                                backdrop.remove();
                            }
                        });
                        cerrarmodal();
                        enviando.value = false
                        emit('trabajo-agregado');
                    }
                });
            } else {
                cerrarmodal();
                enviando.value = false
                alertSuccess("¡Trabajo cargado!");
                // Se envia el emit
                emit('trabajo-agregado');
            }
        }
    );
};

// Función para limpiar campos
function cerrarmodal() {
    // const $modal = $('#trabajoModal');
    // $modal.modal('hide');
    // Limpia los campos input}
    v_presupuesto.value = '';
    v_recibio.value = '';
    v_cliente.value = '';
    v_desc.value = '';
    v_estado.value = '';
    // Limpia campos de FILE
    const imagenseleccionada = archivoInput.value;
    imagenseleccionada.value = '';

}
</script>

<style scoped>
.modal-content {
    background-color: #eeeeee;
}

.modal {
    background: rgba(0, 0, 0, 0.5);
}
.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
}

/* 1. Estado inicial del elemento al entrar (antes de que 'visible' sea true)
      o estado final al salir (cuando 'visible' pasa a ser false) */
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
}

/* 2. Estado de la transición. Define la duración y la función de temporización. */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.5s ease;
}

/* 3. Estado final al entrar (cuando la transición de entrada termina)
      o estado inicial al salir (antes de que 'visible' pase a ser false) */
.fade-slide-enter-to,
.fade-slide-leave-from {
  opacity: 1;
}

/* Puedes aplicar efectos de transformación al contenido dentro del modal */
.modal-body {
    transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.fade-slide-enter-from .modal-body {
    transform: translateY(-50px);
}

#imgEdit {
    width: 100%;
}
</style>