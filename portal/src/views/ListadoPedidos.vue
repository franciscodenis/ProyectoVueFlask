<template>
  <div class="PedidoList">
    <h1>Listado de Pedidos</h1>

    <!-- Filtros y opciones de ordenamiento -->
    <div class="filters">
      <div class="filter-group">
        <label for="order">Ordenar por:</label>
        <select v-model="orderBy" @change="loadOrders">
          <option value="date-asc">Más Antigua Primero</option>
          <option value="date-desc">Más Reciente Primero</option>
          <option value="status">Estado</option>
        </select>
      </div>

      <!-- Agregar campos de fecha para filtrar por rango de fechas -->
      <div class="date-filters">
        <label for="start-date">Fecha Inicial:</label>
        <input type="date" v-model="startDate" @change="loadOrders" id="start-date">

        <label for="end-date">Fecha Final:</label>
        <input type="date" v-model="endDate" @change="loadOrders" id="end-date">
      </div>

      <div class="filter-group">
        <label for="filter">Filtrar por estado:</label>
        <select v-model="filterBy" @change="loadOrders">
          <option value="">Todos</option>
          <option value="IN_PROCESS">En Proceso</option>
          <option value="ACCEPTED">Aceptado</option>
          <option value="REJECTED">Rechazado</option>
          <option value="FINISHED">Finalizado</option>
          <option value="CANCELED">Cancelado</option>
        </select>
      </div>
    </div>

    <!-- Lista de Pedidos -->
    <ul class="order-list">
      <li v-for="order in orders" :key="order.id">
        <div class="order-info">
          <p><strong>Solicitud:</strong> {{ order.title }}</p>
          <p><strong>Fecha:</strong> {{ formatDate(order.created_at) }}</p>
          <p><strong>Estado:</strong> {{ formatStatus(order.status) }}</p>
        </div>
        <div class="order-actions">
          <div class="ver-detalles-button" @click="verDetalles(order.id)">
            Ver Detalles
          </div>
        </div>
      </li>
    </ul>

    <!-- Agregar sección de paginación -->
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">« Anterior</button>
      <span>Página {{ currentPage }} de {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Siguiente »</button>
    </div>
  </div>
</template>

<script>
import router from '../router';
import { apiService } from '../services/api';
import { useAuthStore } from '../stores/AuthStore';

export default {
  data() {
    return {
      orders: [],
      orderBy: 'date-asc',
      filterBy: '',
      startDate: null,
      endDate: null,
      currentPage: 1,
      totalPages: 1,
    };
  },
  mounted() {
    const authStore = useAuthStore();
    if (!authStore.isLoggedIn) {
      router.push("/");
    }
    // Cargar los pedidos al montar el componente
    this.loadOrders();
  },
  methods: {
    loadOrders() {
      // Construir el objeto de parámetros para la URL de la API
      const params = {
        page: this.currentPage,
      };

      // Agregar parámetros adicionales según las condiciones
      if (this.startDate) {
        params.start_date = this.startDate;
      }

      if (this.endDate) {
        params.end_date = this.endDate;
      }

      if (this.filterBy) {
        params.status  = this.filterBy;
      }

      if (this.orderBy === "date-asc" || this.orderBy === "date-desc" || this.orderBy === "status") {
        params.sort = this.orderBy;
      }
      console.log('Parámetros de la API:', params);
      // Realizar la llamada a la API con los parámetros
      apiService.get('api/me/requests', { params })
        .then(response => {
          console.log('Datos de pedidos:', response.data.data);
          this.orders = response.data.data;
          this.totalPages = response.data.total_pages;
          console.log('Total de páginas:', this.totalPages);
        })
        .catch(error => {
          console.error('Error al cargar los pedidos', error);
        });

    },

    verDetalles(orderId) {
      this.$router.push({ name: 'DetallePedido', params: { id: orderId } });
    },

    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        this.loadOrders();
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;
        this.loadOrders();
      }
    },

    // Función para formatear la fecha
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('es-ES', options);
    },

    // Función para formatear el estado
    formatStatus(status) {
      const statusMap = {
        'IN_PROCESS': 'En Proceso',
        'ACCEPTED': 'Aceptado',
        'REJECTED': 'Rechazado',
        'FINISHED': 'Finalizado',
        'CANCELED': 'Cancelado',
      };
      return statusMap[status] || status;
    },
  },
};
</script>

<style scoped>
.PedidoList {
  max-width: 1000px;
  margin: 0 auto;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 20px;
}

.filter-group {
  flex: 1;  /* Para que los elementos dentro de .filter-group se expandan ocupando el espacio disponible */
}

.date-filters {
  display: flex;
  gap: 10px;
}

.order-list {
  list-style: none;
  padding: 0;
}

.order-list li {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
}

.order-info {
  flex: 1;
}

.order-actions {
  flex-shrink: 0;
  text-align: right;
}

.ver-detalles-button {
  display: inline-block;
  padding: 8px 16px;
  background-color: #007BFF;
  color: #fff;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.ver-detalles-button:hover {
  background-color: #0056b3;
}

.pagination {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.pagination button {
  padding: 5px 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

</style>