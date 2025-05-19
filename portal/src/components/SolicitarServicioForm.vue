<template>
  <div v-if="authStore.isLoggedIn" class="card solicitar-servicio-form">
    <h2 class="form-heading">Solicitar Servicio</h2>

    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="title" class="form-label">Título del Trabajo:</label>
        <input v-model="title" id="title" type="text" class="form-input" />
      </div>

      <div class="form-group">
        <label for="description" class="form-label">Descripción del Trabajo:</label>
        <textarea v-model="description" id="description" rows="4" class="form-input"></textarea>
      </div>

      <div class="form-group">
        <button type="submit" class="submit-button">Enviar Solicitud</button>
      </div>
    </form>
  </div>
  <div v-else class="login-container">
    <p class="login-message">Debes iniciar sesión para solicitar un servicio.</p>
    <router-link to="/Sesion" class="login-link">Ir a la página de inicio de sesión</router-link>
  </div>
</template>

<script>
import { apiService } from '../services/api';
import { useAuthStore } from '../stores/AuthStore';

export default {
  props: {
    serviceId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      title: '',
      description: '',
    };
  },
  methods: {
    submitForm() {
      // Validar que se haya recibido la ID del servicio
      if (!this.serviceId) {
        console.error('No se ha proporcionado la ID del servicio.');
        return;
      }

      // Validar que se haya ingresado el título y la descripción
      if (!this.title.trim() || !this.description.trim()) {
        alert('Por favor, complete tanto el título como la descripción antes de enviar la solicitud.');
        return;
      }

      // Enviar la solicitud a la API
      const formData = new FormData();
      formData.append('service_id', this.serviceId);
      formData.append('title', this.title);
      formData.append('description', this.description);

      // Llamar a la API de solicitudes para crear una nueva solicitud
      apiService.post('/api/me/requests/', formData).then(response => {
        console.log('Solicitud enviada con éxito', response.data);
        this.$router.push({name: "DetallePedido", params: { id: response?.data?.id }})
      }).catch(error => {
        console.error('Error al enviar la solicitud', error);
      });

      // Limpiar el formulario después de enviar la solicitud
      this.title = '';
      this.description = '';
    }
  },
  setup() {
    const authStore = useAuthStore();
    return {
      authStore,
    };
  },
};
</script>

<style scoped>
.solicitar-servicio-form {
  background-color: #ecf0f1;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.form-heading {
  color: #2c3e50;
  font-size: 1.5em;
  font-weight: bold;
  text-align: center;
  margin-bottom: 10px;
}

.form-group {
  margin-bottom: 15px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 5px;
}

.submit-button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  margin: 0 auto; /* Centrar el botón */
}

.submit-button:hover {
  background-color: #45a049;
}

.login-message {
  color: black; /* Color rojo, puedes ajustar según tu preferencia */
  font-size: 1.7em;
  text-align: center;
}

.login-link {
  color: #3498db; /* Color azul, puedes ajustar según tu preferencia */
  text-decoration: none;
  font-weight: bold;
  margin-top: 10px;
  display: inline-block;
}
</style>