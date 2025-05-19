<template>
  <div class="container">
  <div class="card">
    <h2 class="custom-heading">{{ serviceInfo.name }}</h2>
    <p><span class="label">id: </span>{{ serviceInfo.id }}</p>
    <p><span class="label">Descripcion: </span>{{ serviceInfo.description }}</p>
    <p><span class="label">Habilitado:</span> {{ serviceInfo.enabled }}</p>
    <p><span class="label">Palabras Clave:</span> <span class="keywords">{{ serviceInfo.keywords }}</span></p>
    <p><span class="label">Service Type:</span> <span class="service-type">{{ serviceInfo.service_type }}</span></p>
  </div>

  <div class="map">
    <ol-map :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" style="height: 400px">
      <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />

      <ol-tile-layer>
        <ol-source-osm />
      </ol-tile-layer>

      <ol-vector-layer>
        <ol-source-vector>
          <ol-feature>
            <ol-geom-point :coordinates="coordinate"></ol-geom-point>
            <ol-style>
              <ol-style-circle :radius="radius">
                <ol-style-fill :color="fillColor"></ol-style-fill>
                <ol-style-stroke :color="strokeColor" :width="strokeWidth"></ol-style-stroke>
              </ol-style-circle>
            </ol-style>
          </ol-feature>
        </ol-source-vector>
      </ol-vector-layer>
    </ol-map>
  </div>
  <div class="card">
    <h2 class="custom-heading">{{ institutionInfo.name }}</h2>
    <p><span class="label">id: </span>{{ institutionInfo.id }}</p>
    <p><span class="label">Dirección: </span>{{ institutionInfo.address }}</p>
    <p><span class="label">Web:</span> {{ institutionInfo.web }}</p>
    <p><span class="label">Horario:</span> <span class="keywords">{{ institutionInfo.opening_hours }}</span></p>
    <p><span class="label">Contacto:</span> <span class="service-type">{{ institutionInfo.contact }}</span></p>
  </div>

  <!-- Usar el componente SolicitarServicioForm -->
  <SolicitarServicioForm
      :serviceId="serviceInfo?.id || NaN"
    />
  </div>
</template>

<script>
import { ref, inject } from 'vue';
import SolicitarServicioForm from "@/components/SolicitarServicioForm.vue";

export default {

  components: {
    SolicitarServicioForm,
  },
  data() {
    return {
      serviceID: this.$route.query.s,
      serviceInfo: {},
      institutionInfo: {}
    }
  },
  created() {
    // watch the params of the route to fetch the data again
    this.$watch(
      () => this.$route.query,
      () => {
        this.fetchData()
      },
      // fetch the data when the view is created and the data is
      // already being observed
      { immediate: true }
    )
  },
  methods: {
    fetchData() {
      fetch(import.meta.env.VITE_API_SERVICE_INFO + this.serviceID, {
        method: "GET",
      })
        .then(response => {
          if (!response.ok) {
            console.error("No se encontró el servicio.");
            this.$router.push({name: "home"});
          }
          return response.json()
        })
        .then(data => {
          this.serviceInfo = data
          return (data)
        })
        .then(service => {
          // aca comienza la busqueda de la institución del servicio
          fetch(import.meta.env.VITE_API_INSTITUTION_INFO + this.serviceInfo.institution_id, {
            method: "GET",
          })
            .then(response => {
              return response.json()
            })
            .then(data => {
              this.institutionInfo = data
              let strings_array = this.institutionInfo.location.split(",")
              this.coordinate = [Number(strings_array[0]), Number(strings_array[1])]
              return (data)
            })

          return service
        })
        .catch((err) => {
          console.error(err);
          console.log("Hubo un error en el fetch");
        });
    },
  },
  setup() {
    const center = ref([-58.37723,-34.61315 ]);
    const projection = ref('EPSG:4326');
    const zoom = ref(8);
    const rotation = ref(0);

    const format = inject('ol-format');
    const geoJson = new format.GeoJSON();
    const radius = ref(5);
    const strokeWidth = ref(5);
    const strokeColor = ref("red");
    const fillColor = ref("white");
    const coordinate = ref([-58.37723,-34.61315]);

    return {
      center,
      projection,
      zoom,
      rotation,
      geoJson,
      radius,
      strokeWidth,
      strokeColor,
      fillColor,
      coordinate
    };
  },
}
</script>


<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #2c3e50;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
}

.container {
  max-width: 90%; /* Cambiado de 1200px a 100% */
  margin: 0 auto; /* Center the container */
  display: flex;
  flex-wrap: wrap;
}

.card {
  background-color: #ecf0f1;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%; /* Cambiado de 300px a 100% */
  text-align: left;
  margin: 10px; /* Espacio entre las tarjetas */
}

.card h2 {
  color: #2c3e50;
  font-size: 1.5em;
  margin-bottom: 10px;
}

.card p {
  color: #34495e;
  font-size: 1em;
  margin: 0 0 10px;
}

.label {
  font-weight: bold;
  color: #3498db;
}

.keywords {
  color: #e74c3c;
}

.service-type {
  color: #27ae60;
}

.map {
  width: 100%;
  border: 2px solid #ccc;
}

.custom-heading {
  color: #2c3e50;
  font-size: 2em;
  font-weight: bold;
  text-align: center;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
}
</style>
