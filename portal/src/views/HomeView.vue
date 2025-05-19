<template>
  <main>
    <div class="main-container">
      <!-- Sección de ¿Quiénes somos? -->
      <section class="about-us-section">
        <h1 class="section-title">¿Quiénes somos?</h1>
        <p class="section-description">CIDEPINT es un portal que facilita la búsqueda de servicios ofrecidos por diversas instituciones. Nuestra misión es proporcionar una plataforma intuitiva para que puedas realizar solicitudes y consultar el estado de tus servicios de manera eficiente.</p>
      </section>

      <!-- Sección de Funcionalidades -->
      <section class="features-section">
        <section class="feature-section">
          <h2>Realizar Búsqueda de Servicios</h2>
          <p>Encuentra los servicios que necesitas de manera rápida y sencilla. Utiliza nuestra herramienta de búsqueda para filtrar y encontrar la información que buscas.</p>
        </section>

        <section class="feature-section">
          <h2>Servicios Prestados</h2>
          <p>Explora la variedad de servicios ofrecidos por las instituciones asociadas. Obtén detalles sobre cada servicio y accede a la información relevante para realizar tus solicitudes.</p>
        </section>

        <section class="feature-section">
          <h2>Iniciar Solicitud de Servicio</h2>
          <p>¿Listo para solicitar un servicio? Inicia el proceso de solicitud fácilmente a través de nuestro portal. Sigue los pasos indicados y realiza tu solicitud en pocos minutos.</p>
        </section>
      </section>

      <!-- Sección de Información de Contacto -->
      <section class="contact-section">
        <h2>Información de Contacto</h2>

        <div v-if="contactInfo">
          <p><strong>Teléfono:</strong> {{ contactInfo.phone_number }}</p>
          <p><strong>Email:</strong> {{ contactInfo.email }}</p>
          <p><strong>Dirección:</strong> {{ contactInfo.address }}</p>
        </div>
        <p v-else>Cargando información de contacto...</p>
      </section>
    </div>
  </main>
</template>

<script>
import { ref, onMounted } from 'vue';
import { apiService } from '../services/api';

export default {
  setup() {
    const contactInfo = ref(null);

    onMounted(() => {
      // Llama a la API Flask para obtener la información de contacto
      apiService.get('/api/contact_info')
        .then(response => {
          console.log('Información de contacto cargada', response.data);
          contactInfo.value = response.data;
        })
        .catch(error => {
          console.error('Error al cargar la información de contacto', error);
        });
    });

    return {
      contactInfo,
    };
  },
};
</script>
<style scoped>
.main-container {
  display: flex;
  flex-direction: column; /* Cambiado a columna en pantallas más pequeñas */
  margin: 0 auto; /* Añadido para centrar el contenido */
  max-width: 1200px; /* Ajusta según sea necesario */
}

.about-us-section,
.features-section,
.contact-section {
  width: 100%; /* Cambiado a 100% en pantallas más pequeñas */
  padding: 20px; /* Añadido espacio de relleno */
  border: 1px solid #ccc; /* Agregado borde */
  margin-bottom: 20px; /* Añadido margen inferior */
  box-sizing: border-box; /* Asegura que el borde y el relleno no afecten el tamaño total */
}

.section-title {
  font-size: 2.1rem;
  font-weight: bold;
  font-family: sans-serif;
}

.section-description {
  font-size: 1.3rem;
  /* color: #333232; */
  line-height: 1.6;
  text-align: justify;
}

.feature-section {
  margin-bottom: 20px;
}

.contact-section h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.contact-info {
  font-size: 1.2rem;
  color: #555;
  line-height: 1.6;
}
</style>