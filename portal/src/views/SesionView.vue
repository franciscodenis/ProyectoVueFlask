<script setup>
import { useAuthStore } from '../stores/AuthStore';
import { ref } from 'vue';

const authStore = useAuthStore();

let error = ref(false);

let user = ref({
  email: null,
  password: null
});

async function login() {
  await authStore.login(user.value)
    .then(() => {
      error.value = false;
    })
    .catch(() => {
      error.value = true;
    });
}

function logout() {
  authStore.logout();
  user.value = {
    email: null,
    password: null
  };
}

async function google() {
  window.location.href = import.meta.env.VITE_ADMIN_APP_BASE_URL + "/auth/public-google-login"
}

</script>

<template>
  <div v-if="authStore.isLoggedIn" class="form">
    <h2 class="form-label">Usuario: {{ authStore.user?.username }}</h2>
    <h2 class="form-label">Mail: {{ authStore.user?.email }}</h2>
    <button type="button" @click="logout" class="form-submit">Cerrar sesión</button>
  </div>
  <div v-if="!authStore.isLoggedIn">
    <form class="form" @submit.prevent="login">
      <label for="#user.email" class="form-label">Email</label>
      <input type="email" v-model="user.email" placeholder="Email" class="form-input" id="email" required>
      <label for="#user.password" class="form-label">Password</label>
      <input type="password" autocomplete="on" v-model="user.password" placeholder="Password" id="password" class="form-input" required>
      <p v-if="error" class="error">Verifica los datos ingresados y vuelve a intentar.</p>
      <input type="submit" class="form-submit" value="Login">
    </form>
    <button type="button" @click="google">Usar Google</button>
  </div>
</template>

<style lang="css" scoped>
.login {
  padding: 2rem;
}
.title {
  text-align: center;
}
.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 20%;
  min-width: 350px;
  max-width: 100%;
  background: rgba(19, 35, 47, 0.9);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: white;
  margin-bottom: 0.5rem;
}
.form-label:first-of-type {
  margin-top: 0rem;
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: white;
}
.form-input:focus {
  outline: 0;
  border-color: #1ab188;
}
.form-submit {
  background: #1ab188;
  border: none;
  color: white;
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
}
.form-submit:hover {
  background: #0b9185;
}
.error {
  margin: 1rem 0 0;
  color: #ff4a96;
}
</style>