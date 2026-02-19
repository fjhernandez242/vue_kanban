export function formatFecha(isoString) {
  if (!isoString) return 'N/A';

  const date = new Date(isoString);

  // Opciones de formato (hora local en español de México)
  const options = {
    year: 'numeric',
    month: 'short', // 'Oct'
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true, // Formato AM/PM
  };

  // Usar Intl.DateTimeFormat para un formato legible y localizado
  return new Intl.DateTimeFormat('es-MX', options).format(date);
}