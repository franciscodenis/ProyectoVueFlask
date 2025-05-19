<template>
    <div class="PedidoDetalles">
      <h2>Detalles del Pedido</h2>
  
      <div v-if="pedido">
        <p><strong>Solicitud:</strong> {{ pedido.title }}</p>
        <p><strong>Descripción:</strong> {{ pedido.description }}</p>
        <p><strong>Fecha:</strong> {{ formatDate(pedido.created_at) }}</p>
        <p><strong>Estado:</strong> {{ formatStatus(pedido.status) }}</p>
      </div>
  
      <div v-if="notas.length">
        <h3>Notas</h3>
        <ul>
          <li v-for="nota in notas" :key="nota.id">
            <strong>{{ nota.username }}:</strong> {{ nota.content }}
          </li>
        </ul>
      </div>
  
      <form @submit.prevent="agregarNota">
        <label>Nueva Nota:</label>
        <textarea v-model="nuevaNota" required></textarea>
        <button type="submit">Agregar Nota</button>
      </form>
    </div>
  </template>
  
  <script>
  import { apiService } from '../services/api';
  
  export default {
    data() {
      return {
        pedido: null,
        notas: [],
        nuevaNota: '',
      };
    },
    mounted() {
      const pedidoId = this.$route.params.id;
  
      Promise.all([
        apiService.get(`/api/me/requests/${pedidoId}`),
        apiService.get(`/api/me/requests/${pedidoId}/notes`),
      ])
        .then(([pedidoResponse, notasResponse]) => {
          this.pedido = pedidoResponse.data;
          this.notas = notasResponse.data;
        })
        .catch(error => {
          console.error('Error al cargar los detalles del pedido', error);
        });
    },
    methods: {
      formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('es-ES', options);
      },
  
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
  
      agregarNota() {
        if (this.nuevaNota) {
          const pedidoId = this.$route.params.id;
          apiService
            .post(`/api/me/requests/${pedidoId}/notes`, { content: this.nuevaNota })
            .then(response => {
              this.notas.push(response.data);
              this.nuevaNota = '';
            })
            .catch(error => {
              console.error('Error al agregar la nota', error);
            });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .PedidoDetalles {
    margin: 20px;
  }
  
  .PedidoDetalles h2 {
    color: #333;
  }
  
  .PedidoDetalles div {
    margin-bottom: 20px;
  }
  
  .PedidoDetalles p {
    margin: 5px 0;
  }
  
  .PedidoDetalles ul {
    list-style-type: none;
    padding: 0;
  }
  
  .PedidoDetalles li {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    background-color: var(--color-background-muted);
  }
  
  .PedidoDetalles form {
    margin-top: 20px;
  }
  
  .PedidoDetalles label {
    display: block;
    margin-bottom: 5px;
  }
  
  .PedidoDetalles textarea {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }
  
  .PedidoDetalles button {
    background-color: #4caf50;
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
  }
  
  .PedidoDetalles button:hover {
    background-color: #45a049;
  }
  </style>