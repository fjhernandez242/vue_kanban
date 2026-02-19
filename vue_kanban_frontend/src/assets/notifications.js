import Swal from "sweetalert2";

export function alertSuccess(mensaje) {
    Swal.fire({
        icon: "success",
        title: mensaje,
        showConfirmButton: false,
        timer: 1500
    });
}