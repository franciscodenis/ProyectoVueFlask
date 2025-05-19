<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/AuthStore';
// import { useCookies } from 'vue3-cookies';

const authStore = useAuthStore();
// const cookies = useCookies();

// if (cookies.cookies.isKey("csrf_access_token")) {
  authStore.fetchUser();
// }
</script>


<template>
  <div id="app">
    <nav>
      <RouterLink to="/" class="no-text-decoration">
        <div class="navbar-brand"> <!-- Cambiado a un enlace -->
          <img src="@/assets/logo.png" alt="Logo">
          <span class="brand-text">CIDEPINT</span>
        </div>
      </RouterLink>
      <div class="navbar-links">
        <RouterLink class="navbarButton" to="/BusquedaServicio">Busqueda de servicio</RouterLink>
        <RouterLink v-if="authStore.isLoggedIn" class="navbarButton" to="/ListadoPedidos">Listado Pedidos</RouterLink>
        <RouterLink class="navbarButton" to="/AnalisisDatos">Analisis de Datos</RouterLink>
        <RouterLink v-if="authStore.isLoggedIn" class="navbarButton" to="/Sesion">Perfil</RouterLink>
        <RouterLink v-if="!authStore.isLoggedIn" class="navbarButton" to="/Sesion">Login</RouterLink>
      </div>
    </nav>
    <div class="container">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
  background-color: #106cfc;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  color: #fff;
}

.navbar-brand {
  font-size: 1.5rem;
  display: flex;
  align-items: center;
}

.navbar-brand img {
  height: 40px;
  margin-right: 10px;
}

.navbar-links {
  display: flex;
  gap: 40px; /* Aumento el espacio entre los enlaces */
  margin-left: 30px; /* Ajusto el espacio a la izquierda */
  margin-right: 30px; /* Ajusto el espacio a la derecha */
}

.navbar-links a {
  color: #fff;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s;
}

.navbar-links a:hover {
  color: #ccc;
}

.container {
  margin-top: 80px;
  padding: 2rem;
  background-color: var(--color-background-soft);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.no-text-decoration {
  text-decoration: none;
}

@media (max-width: 767px) {
  nav {
    flex-direction: column;
    align-items: center;
  }

  .navbar-links {
    margin-top: 1rem;
    gap: 20px; /* Ajusto el espacio entre los enlaces en dispositivos pequeños */
  }

  .navbar-links a {
    margin: 0.5rem 0;
  }

  .container {
    margin-top: 150px; /* Ajusta la distancia desde la parte superior en pantallas pequeñas */
  }
}

.brand-text {
  font-size: 1.5rem;
  font-weight: bold;
  margin-left: 10px;
  color: white;
  text-decoration: none;
}
</style>