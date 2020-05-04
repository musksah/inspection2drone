<template>
  <card class="card" title="Módulo de Carga de Fotografías">
    <div>
      <form @submit.prevent class="mt-2 mb-4">
        <div class="row">
          <div class="col-md-5">
            <!-- <select class="custom-select">
              <option selected>Compañía</option>
              <option value="Coca Cola">Coca Cola</option>
              <option value="Pepsi">Pepsi</option>
              <option value="Sprite">Sprite</option>
            </select>-->
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </div>
        </div>
        <div class="row">
          <!-- <div class="col-md-12">
            <input type="file" @change="processFile($event)" />
          </div>-->
          <div class="col-md-5">
            <b-form-file
              v-model="file"
              :state="Boolean(file)"
              placeholder="Escoja un archivo o suéltelo acá..."
              drop-placeholder="Drop file here..."
              accept="image/jpeg, image/gif"
              browse-text="buscar"
            ></b-form-file>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4">
            <b-button variant="primary">Registrar</b-button>
          </div>
        </div>
      </form>
    </div>
  </card>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      file: "",
      company: "",
      selected: null,
      options: [{ value: null, text: "seleccionar..." }],
      file: null
    };
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios;
  },
  mounted() {
    this.loadSelectCompany();
  },
  methods: {
    loadSelectCompany() {
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/companies/",
        method: "get",
        params: {}
      })
        .then(res => {
          console.log(res);
          res.data.forEach(item => {
            this.options.push({
              value: item.name,
              text: item.name
            });
          });
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "El usaurio no puedo ser creado",
            timer: 3000
          });
        });
    }
  }
};
</script>
<style>
</style>