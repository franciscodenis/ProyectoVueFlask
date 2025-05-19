<template>
  <div class="SolicitarServicio">
    <h1>Solicitar Servicio</h1>

    <!-- Selección de Institución -->
    <label for="institution">Seleccionar Institución:</label>
    <select v-model="selectedInstitution" id="institution" @change="loadServices">
      <option v-for="institution in institutions" :key="institution.id" :value="institution.id">
        {{ institution.name }}
      </option>
    </select>

    <!-- Formulario de Solicitud de Servicio -->
    <form @submit.prevent="submitForm">
      <label for="service" v-if="services && services.length > 0">Seleccionar Servicio:</label>
    <select v-model="selectedService" id="service" v-if="services && services.length > 0">
        <option v-for="service in services" :key="service.id" :value="service.id">
          {{ service.name }}
        </option>
      </select>

      <label for="title">Título del Trabajo:</label>
      <input v-model="title" id="title" type="text" />

      <label for="description">Descripción del Trabajo:</label>
      <textarea v-model="description" id="description" rows="4"></textarea>

      <label for="attachment">Adjuntar Archivos:</label>
      <input type="file" @change="handleFileChange" id="attachment" multiple />
      <div class="files-container" v-if="files.length > 0">
        <h3>Archivos Seleccionados</h3>
        <ul>
          <li v-for="(file, index) in files" :key="index">
            {{ file.file.name }} 
            <button class="delete-button" type="button" @click="removeFile(index)">X</button>
          </li>
        </ul>
      </div>

      <button type="submit">Enviar Solicitud</button>
    </form>
  </div>
</template>

<script>
import { apiService } from '../services/api';

export default {
  data() {
    return {
      selectedInstitution: null,
      selectedService: null,
      title: '',
      description: '',
      files: [],
      institutions: [],  // Lista de instituciones cargada desde la API
      services: []       // Lista de servicios cargada desde la API
    };
  },
  mounted() {
    // Llamada a la API para obtener la lista de instituciones
    apiService.get('api/consultas_instituciones')
    .then(response => {
      console.log('Datos de instituciones:', response.data.data);
      this.institutions = response.data.data;
    })
    .catch(error => {
      console.error('Error al cargar las instituciones', error);
    });
  },
  methods: {
    handleFileChange(event) {
      for (let i = 0; i < event.target.files.length; i++) {
        const uniqueName = `file_${Date.now()}_${i}`;
        this.files.push({
          name: uniqueName,
          file: event.target.files[i]
        });
      }
    },
    removeFile(index) {
      this.files.splice(index, 1);
    },
    loadServices() {
    // Llamada a la API para obtener la lista de servicios de la institución seleccionada
    if (this.selectedInstitution) {
      apiService.get(`api/services/institution/${this.selectedInstitution}`)
        .then(response => {
          const responseData = response.data;

          if (responseData && responseData.data && responseData.data.length > 0) {
            // Si hay datos en la respuesta, actualiza la lista de servicios
            this.services = responseData.data;
          } else {
            // Si no hay datos, muestra un mensaje o realiza alguna acción adecuada
            this.services = []; // Limpiar la lista de servicios
            console.warn('La respuesta de la API no contiene datos de servicios.');
          }
        })
        .catch(error => {
          console.error('Error al cargar los servicios', error);
          this.services = []; // Limpiar la lista de servicios en caso de error
        });
      } else {
        // Limpiar la lista de servicios si no se selecciona una institución
        this.services = [];
     }
    },
    submitForm() {
      // Validar que se haya seleccionado una institución y un servicio
      if (!this.selectedInstitution || !this.selectedService) {
        alert('Por favor, seleccione una institución y un servicio.');
        return;
      }

      // Enviar la solicitud a la API
      const formData = new FormData();
      formData.append('institution_id', this.selectedInstitution);
      formData.append('service_id', this.selectedService);
      formData.append('title', this.title);
      formData.append('description', this.description);

      if (this.files) {
        for (let i = 0; i < this.files.length; i++) {
          formData.append('files', this.files[i]);
        }
      }

      // Llamar a la API de solicitudes para crear una nueva solicitud
      apiService.post('/api/me/requests', formData).then(response => {
        if (response.status == 201 || response.status == 200) {
          console.log('Solicitud enviada con éxito', response.data);
          this.$router.push({name: 'DetallePedido', params: {id: response.data?.id}})
        }
      }).catch(error => {
        console.error('Error al enviar la solicitud', error);
      });

      // Limpiar el formulario después de enviar la solicitud
      this.selectedInstitution = null;
      this.selectedService = null;
      this.title = '';
      this.description = '';
      this.files = [];
    },
  },
};
</script>

<style scoped>
.SolicitarServicio {
  max-width: 800px;
  margin: 0 auto;
}

.form-container {
  border: 1px solid #ccc;
  padding: 20px;
  margin-top: 20px;
  border-radius: 5px;
}

label {
  display: block;
  margin-bottom: 5px;
}

select,
input,
textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.delete-button {
  background-color: #ff6b6b;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-left: 5px;
  padding: 5px 10px;
}

.delete-button:hover {
  background-color: #d9534f;
}

.files-container {
  margin-bottom: 20px;
}

</style>
