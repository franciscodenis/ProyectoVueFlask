<template>
  <div>
    <div class="button-container">
      <button @click="toggleChart('statusPieChart')" class="chart-button">Cantidad de solicitudes por estado</button>
      <button @click="toggleChart('topServicesChart')" class="chart-button">Servicio más utilizados</button>
      <button @click="toggleChart('topInstitutionsChart')" class="chart-button">Institucion con mejor Tiempo de Resolución</button>
    </div>

    <div class="charts-container">
      <status-pie-chart class="chart" v-if="visibleCharts.statusPieChart"></status-pie-chart>
      <top-services-chart class="chart" v-if="visibleCharts.topServicesChart"></top-services-chart>
      <top-institutions-chart class="chart" v-if="visibleCharts.topInstitutionsChart"></top-institutions-chart>
    </div>
  </div>
</template>

<script>
import StatusPieChart from '@/components/_StatusPieChart.vue';
import TopServicesChart from '@/components/_TopServicesChart.vue';
import TopInstitutionsChart from '@/components/_TopInstitutionsChart.vue';

export default {
  components: {
    StatusPieChart,
    TopServicesChart,
    TopInstitutionsChart,
  },
  data() {
    return {
      visibleCharts: {
        statusPieChart: false,
        topServicesChart: false,
        topInstitutionsChart: false,
      },
    };
  },
  methods: {
    toggleChart(chart) {
      this.visibleCharts = {
        statusPieChart: chart === 'statusPieChart',
        topServicesChart: chart === 'topServicesChart',
        topInstitutionsChart: chart === 'topInstitutionsChart',
      };
    },
  },
};
</script>

<style scoped>
.button-container {
  display: flex;
  justify-content: space-around;
  margin: 1rem;
}

.chart-button {
  padding: 10px;
  background-color: #ddd;
  color: #555;
  border: 1px solid #555;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.chart-button:hover {
  background-color: #ccc;
}

.chart {
  flex: 1;
  margin: 1rem;
  max-width: 700px; /* Ajusta el ancho máximo de las gráficas según tus necesidades */
}

/* Estilo para dispositivos más pequeños (ajusta según tus necesidades) */
@media screen and (max-width: 768px) {
  .chart {
    flex: 1 0 100%;
  }
}
</style>