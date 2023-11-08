import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { IonIcon } from '@ionic/vue';
import './assets/estilos/style.css';
import store from './stores/store';

const app = createApp(App);

app.component('IonIcon', IonIcon);

app.use(router);

app.use(store);

app.mount('#app');

