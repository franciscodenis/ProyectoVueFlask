<template>
    <div class="BusquedaServicio">
      <p>Busqueda de Servicio</p>
      <input type="text" ref="searchInputField">
      <select id="menu"  ref="selectInputField">
      <option v-for="types in listOfTypes" :key="types">{{types}}</option>
    </select>
    <button v-on:click="searchClick">Click aqui para iniciar la búsqueda</button>
    </div>
    <p></p>
    <table>
      <thead>
				<tr>
					<th> id </th>
					<th> Nombre </th>
					<th> Tipo de Servicio </th>
					<th> Descripción</th>
					<th> Habilitado </th>
					<th> Palabras Clave </th>
          <th> Link </th>
				</tr>
			</thead>
      <tr v-for="service in listOfServices" :key="service.id">
        <td >{{service.id}}</td>
        <td >{{service.name}}</td>
        <td >{{service.service_type.split('.')[1]}}</td>
        <td >{{service.description}}</td>
        <td >{{service.enabled ? "Sí" : "No"}}</td>
        <td >{{service.keywords}}</td>
        <td><RouterLink :to="{ name: 'VisualizarServicio', query: {s: service.id}}"
          custom v-slot="{ navigate }"><button @click="navigate" role="link">Ver</button></RouterLink></td>
      </tr>
    </table>
</template>

<script>
export default{

  data() {
    return {
      listOfTypes: [],
      listOfServices:[]
    }
  },
  created() {
    // watch the params of the route to fetch the data again
    this.$watch(
      () => this.$route.params,
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
      fetch(import.meta.env.VITE_API_SERVICE_TYPE_LINK, {
        method: "GET",
      })
        .then( response => {
          return response.json()})
        .then( data => {
          console.log(data["data"])
          this.listOfTypes = data["data"]
          return(data["data"])})
        .catch((err) => {
          console.error(err);
          console.log("Hubo un error en el fetch")
        });},

    searchClick() {
      console.log("click de busqueda");
      fetch(import.meta.env.VITE_API_SERVICE_SEARCH_LINK + new URLSearchParams({q: this.$refs.searchInputField.value, type: this.$refs.selectInputField.value, page:1, per_page: 10},
      ), {method: "GET"})
      .then( response => {
        return response.json()})
      .then( data => {
        console.log(data["data"])
        this.listOfServices = data["data"]
        return(data["data"])})
      .catch((err) => {
        console.error(err);
        console.log("Hubo un error en el fetch")});
      console.log("click de busqueda");
    }

}
}


</script>

<style scoped>

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

select {
  padding: 0.5em;
  font-size: 1em;
  border-radius: 0.25em;
  border: 1px solid #ccc;
}
/* General table styles */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

/* Header styles */
thead {
    background-color: #3498db;
    color: #fff;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

/* Alternating row colors for better readability */
tbody tr:nth-child(even) {
    background-color: #f2f2f2;
}

/* Hover effect on rows */
tbody tr:hover {
    background-color: #e0e0e0;
}

.link-ver {
  font-weight: bolder;
  /* text-decoration: none; */
  color: var(--color-text)
}

/* Responsive styles */
@media (max-width: 600px) {
    th, td {
        display: block;
        width: 100%;
        box-sizing: border-box;
    }

    /* Hide header on small screens */
    thead tr {
        display: none;
    }

    /* Display table row borders on small screens */
    tbody tr {
        border-bottom: 2px solid #ddd;
        margin-bottom: 8px;
    }
}

</style>
