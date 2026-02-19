<template>
    <div id="viewTablero">
        <div class="row pt-3">
            <div class="col-xl-10">
                <h1 class="text-black">Tablero</h1>
            </div>
            <div class="col-xl-2">
                <!-- Se referencia la vista del modal -->
                <agregarTrabajo
                    :editar-id="idEdit"
                    :visible="mostrarModal"
                    @cerrar-modal="cerrarModal"
                    @trabajo-agregado="listarTrabajos" />
                <!-- Button trigger modal -->
                <button type="button" class="btn" id="btnAgregar" @click="editarTarjeta(null)">
                    <span>Agregar tarea</span>
                </button>
            </div>
        </div>
        <div class="container text-center">
            <div class="row">
                <!-------------------------------------------------------------- Evaluación -->
                <div class="col-xl-3">
                    <div class="p-3 drop-zone" id="recepcion" @drop="onDrop($event, 1)" @dragover.prevent @dragenter.prevent>
                        <div class="position-relative">
                            <span class="p-2">
                                Recepción
                            </span>
                            <span class="position-absolute top-5 translate-middle badge rounded-pill bg-danger">{{ cantRecepciones }}</span>
                        </div>
                        <div v-for="trabajo in listOne" class="card mt-2 drag-el" draggable="true"
                            @dragstart="startDrag($event, trabajo)">
                            <div class="card-header">
                                <div class="row">
                                    <div class="col-xl-8">
                                        <h5 class="card-title text-start"
                                            data-bs-toggle="tooltip" data-bs-placement="top" title="Copiar guía ">
                                            {{ trabajo.guia }}
                                            <i class="bi bi-copy" id="icon_copy" @click="copyData(trabajo.guia)"></i>
                                        </h5>
                                    </div>
                                    <div class="col-xl-4 text-end">
                                        <div class="btn-group-vertical">
                                            <button type="button" class="btn btn-outline-success" id="icon_edit"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Editar tarjeta"
                                                @click="editarTarjeta(trabajo.id)">
                                                <i class="bi bi-pencil-fill"></i>
                                            </button>
                                            <button type="button" class="btn btn-outline-success" id="icon_viewImage"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Ver imagen">
                                                <i class="bi bi-image"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Fecha de recepción:</small>
                                    <small class="text-end">{{ formatFecha(trabajo.fecha_recepcion) }}</small>
                                </div>
                                <div class="mt-2 d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Descripción:</small>
                                    <p class="card-text">{{ trabajo.desc }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-------------------------------------------------------------- Revisión -->
                <div class="col-xl-3">
                    <div class="p-3 drop-zone" id="revision" @drop="onDrop($event, 2)" @dragover.prevent @dragenter.prevent>
                        <div class="position-relative">
                            <span class="p-2">
                                Revisión
                            </span>
                            <span class="position-absolute top-3 translate-middle badge rounded-pill bg-danger">{{ cantRevision }}</span>
                        </div>
                        <div v-for="trabajo in listTwo" class="card mt-2 drag-el" draggable="true"
                            @dragstart="startDrag($event, trabajo)">
                           <div class="card-header">
                                <div class="row">
                                    <div class="col-xl-8">
                                        <h5 class="card-title text-start"
                                            data-bs-toggle="tooltip" data-bs-placement="top" title="Copiar guía ">
                                            {{ trabajo.guia }}
                                            <i class="bi bi-copy" id="icon_copy" @click="copyData(trabajo.guia)"></i>
                                        </h5>
                                    </div>
                                    <div class="col-xl-4 text-end">
                                        <div class="btn-group-vertical">
                                            <button type="button" class="btn btn-outline-success" id="icon_edit"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Editar tarjeta">
                                                <i class="bi bi-pencil-fill"></i>
                                            </button>
                                            <button type="button" class="btn btn-outline-success" id="icon_viewImage"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Ver imagen">
                                                <i class="bi bi-image"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Fecha de recepción:</small>
                                    <small class="text-end">{{ formatFecha(trabajo.fecha_recepcion) }}</small>
                                </div>
                                <div class="mt-2 d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Descripción:</small>
                                    <p class="card-text">{{ trabajo.desc }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-------------------------------------------------------------- Reparacion -->
                <div class="col-xl-3">
                    <div class="p-3 drop-zone" id="reparacion" @drop="onDrop($event, 3)" @dragover.prevent @dragenter.prevent>
                        <div class="position-relative">
                            <span class="p-2">
                                Reparación
                            </span>
                            <span class="position-absolute top-3 translate-middle badge rounded-pill bg-danger">{{ cantReparacion }}</span>
                        </div>
                        <div v-for="trabajo in listTree" class="card mt-2 drag-el" draggable="true"
                            @dragstart="startDrag($event, trabajo)">
                           <div class="card-header">
                                <div class="row">
                                    <div class="col-xl-8">
                                        <h5 class="card-title text-start"
                                            data-bs-toggle="tooltip" data-bs-placement="top" title="Copiar guía ">
                                            {{ trabajo.guia }}
                                            <i class="bi bi-copy" id="icon_copy" @click="copyData(trabajo.guia)"></i>
                                        </h5>
                                    </div>
                                    <div class="col-xl-4 text-end">
                                        <div class="btn-group-vertical">
                                            <button type="button" class="btn btn-outline-success" id="icon_edit"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Editar tarjeta">
                                                <i class="bi bi-pencil-fill"></i>
                                            </button>
                                            <button type="button" class="btn btn-outline-success" id="icon_viewImage"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Ver imagen">
                                                <i class="bi bi-image"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Fecha de recepción:</small>
                                    <small class="text-end">{{ formatFecha(trabajo.fecha_recepcion) }}</small>
                                </div>
                                <div class="mt-2 d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Descripción:</small>
                                    <p class="card-text">{{ trabajo.desc }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-------------------------------------------------------------- Entregado -->
                <div class="col-xl-3">
                    <div class="p-3 drop-zone" id="entregado" @drop="onDrop($event, 4)" @dragover.prevent @dragenter.prevent>
                        <div class="position-relative">
                            <span class="p-2">
                                Entregado
                            </span>
                            <span class="position-absolute top-3 translate-middle badge rounded-pill bg-danger">{{ cantEntregado }}</span>
                        </div>
                        <div v-for="trabajo in listFour" class="card mt-2 drag-el" draggable="true"
                            @dragstart="startDrag($event, trabajo)">
                           <div class="card-header">
                                <div class="row">
                                    <div class="col-xl-8">
                                        <h5 class="card-title text-start"
                                            data-bs-toggle="tooltip" data-bs-placement="top" title="Copiar guía ">
                                            {{ trabajo.guia }}
                                            <i class="bi bi-copy" id="icon_copy" @click="copyData(trabajo.guia)"></i>
                                        </h5>
                                    </div>
                                    <div class="col-xl-4 text-end">
                                        <div class="btn-group-vertical">
                                            <button type="button" class="btn btn-outline-success" id="icon_edit"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Editar tarjeta">
                                                <i class="bi bi-pencil-fill"></i>
                                            </button>
                                            <button type="button" class="btn btn-outline-success" id="icon_viewImage"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Ver imagen">
                                                <i class="bi bi-image"></i>
                                            </button>
                                            <button type="button" class="btn btn-outline-success" id="icon_archiving"
                                                data-bs-toggle="tooltip" data-bs-placement="top" title="Archivar"
                                                @mouseenter="isHovering = true" @mouseleave="isHovering = false">
                                                <div v-if="isHovering">
                                                    <i class="bi bi-folder2-open"></i>
                                                </div>
                                                <div v-else>
                                                    <i class="bi bi-folder"></i>
                                                </div>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card-body">
                                <div class="d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Fecha de recepción:</small>
                                    <small class="text-end">{{ formatFecha(trabajo.fecha_recepcion) }}</small>
                                </div>
                                <div class="mt-2 d-grid gap-2" id="card_fecha_carga">
                                    <small class="text-start fw-bold">Descripción:</small>
                                    <p class="card-text">{{ trabajo.desc }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
// Se importa el modal
import agregarTrabajo from './agregarTrabajo.vue'
// Importa servicio API Django Rest Framework
import { getListarTablero, SetterPosicionTablero } from '../services/tablero-services.js'
// Función para formateo de fecha
import { formatFecha } from '@/assets/dateFormatter';

// Declaración de variables
// Bandera para cambio de icono Carpeta abierta
const isHovering = ref(false);
// Cantidad de recepciones
const cantRecepciones = ref(0);
// Cantidad de revisiones
const cantRevision = ref(0);
// Cantidad de reparaciones
const cantReparacion = ref(0);
// Cantidad de entregados
const cantEntregado = ref(0);
// Info para edición
const idEdit = ref(null);
const mostrarModal = ref(false);
// API tablero
const tableroApi = ref([])

const listarTrabajos = async () => {
    cerrarModal();
    getListarTablero().then(
            (data) => {
                tableroApi.value = data.trabajos;
            }
    ).catch(error => {
        console.error("Error al obtener los datos:", error);
        // Manejo de errores (mostrar mensaje al usuario)
    });
};
onMounted(listarTrabajos);

const listOne = computed(() => {
        const recepcion = tableroApi.value.filter((trabajo) => trabajo.lista === 1)
        cantRecepciones.value = recepcion.length
        return recepcion
    });

const listTwo = computed(() => {
        const revision = tableroApi.value.filter((trabajo) => trabajo.lista === 2)
        cantRevision.value = revision.length
        return revision
    });
const listTree = computed(() => {
        const reparacion = tableroApi.value.filter((trabajo) => trabajo.lista === 3)
        cantReparacion.value = reparacion.length
        return reparacion
    });
const listFour = computed(() => {
        const entregado = tableroApi.value.filter((trabajo) => trabajo.lista === 4)
        cantEntregado.value = entregado.length
        return entregado
    });

// Métodos
const startDrag = (evt, trabajo) => {
    evt.dataTransfer.dropEffect = 'move';
    evt.dataTransfer.effectAllowed = 'move';
    // Guardamos el ID del ítem que se está arrastrando
    evt.dataTransfer.setData('itemID', trabajo.id);
};

const onDrop = (evt, listId) => {
    // 1. Obtener el ID del ítem arrastrado
    const itemID = evt.dataTransfer.getData('itemID');
    // 2. Buscar el ítem en el arreglo reactivo 'tableroApi'
    const trabajo = tableroApi.value.find((trabajo) => trabajo.id == itemID);
    // 3. Modificar el estado: mover el ítem a la nueva lista

    if (trabajo) {
        // Cambia el número de lista en la vista
        trabajo.lista = listId;
        // Realiza el cambio de lista en la base de datos
        const cambio = ref({ "guia": trabajo.guia, "posicion": listId })
        SetterPosicionTablero(cambio.value);
    }
    // Al modificar trabajo.list, Vue actualiza automáticamente listOne y listTwo
};

// Inicializar rutas
// import { useRouter } from 'vue-router';
// const router = useRouter();
// const goToTablero = () => {
//     router.push('/usuarios');
// };

const copyData = (dato) => {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(dato).select();
    document.execCommand("copy");
    $temp.remove();
}

function editarTarjeta(id) {
    idEdit.value = id;
    mostrarModal.value = true;
}

function cerrarModal() {
    mostrarModal.value = false;
    idEdit.value = null;
}
</script>

<style scoped>

#viewTablero {
    padding-top: 3rem;
    padding-inline: 1rem;
}

#icon_copy {
    font-size: 13px;
    cursor: pointer;
}

#recepcion span,
#revision span,
#reparacion span,
#entregado span {
    color: #fff;
}

#btnAgregar {
    background-color: #40749eda;
    color: white;
    transform: scale3d(1, 1, 1);
    transition: all 0.7s;
}

#btnAgregar:hover {
    transform: scale3d(1.1, 1.1, 1.1);
    transition: all 0.7s;
}

.drop-zone {
    background-color: #40749ead;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 10px;
}

.drag-el {
    background-color: #fff;
    margin-bottom: 10px;
    padding: 5px;
}

#card_fecha_carga {
    background-color: #d3d1d159;
    padding-inline: 2px;
    border-radius: 10px;
}

#icon_edit,
#icon_viewImage,
#icon_archiving {
    color: rgb(29, 131, 25);
    border: none;
    transition: all 0.3s;
}

#icon_edit:hover,
#icon_viewImage:hover,
#icon_archiving:hover {
    color: rgb(253, 253, 253);
    transition: all 0.2s;
}

#icon_viewImage:hover,
#icon_edit:hover,
#icon_archiving:hover {
    border-radius: 6px;
    transition: all 0.7s;
    rotate: -15deg;
}
</style>