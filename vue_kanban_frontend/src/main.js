import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// Bootstrap js
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
// Bootstrap Css
import 'bootstrap/dist/css/bootstrap.min.css';
// Bootstrap icons
import '../node_modules/bootstrap-icons/font/bootstrap-icons.min.css';

const app = createApp(App)

app.use(router)

app.mount('#app')

