<template>
  <card class="card" title="Módulo de Carga de Fotografías">
    <div>
      <form @submit.prevent="saveImage" class="mt-2 mb-4">
        <div class="row">
          <div class="col-md-5">
            <!-- <select class="custom-select">
              <option selected>Compañía</option>
              <option value="Coca Cola">Coca Cola</option>
              <option value="Pepsi">Pepsi</option>
              <option value="Sprite">Sprite</option>
            </select>-->
            <!-- <b-form-select v-model="form.company_id" :options="options"></b-form-select> -->
            <label for="">Inspección</label>
            <b-form-select v-model="form.inspection_id" :options="options_inspection"></b-form-select>
            <label for="" class="mt-2">Drone</label>
            <b-form-select v-model="form.drone_id" :options="options_drone"></b-form-select>
          </div>
        </div>
        <div class="row mt-1">
          <!-- <div class="col-md-12">
            <input type="file" @change="processFile($event)" />
          </div>-->
          <div class="col-md-5">
            <b-form-file
              v-model="form.file"
              :state="Boolean(form.file)"
              placeholder="Escoja un archivo o suéltelo acá..."
              drop-placeholder="Drop file here..."
              accept="image/jpeg, image/gif"
              browse-text="buscar"
              @change="handleFileUpload"
              ref="file"
            ></b-form-file>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4">
            <b-button type="submit" variant="primary">Registrar</b-button>
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
      company: "",
      selected: null,
      options: [{ value: null, text: "seleccionar..." }],
      options_inspection: [{ value: null, text: "seleccionar..." },{ value: 1, text: "06/04/20" }],
      options_drone: [{ value: null, text: "seleccionar..." },,{ value: 1, text: "Mavic Phantom 4 RTK" }],
      form: {
        drone_id: null,
        inspection_id: null,
        file: null
      }
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
            text: "El usuario no puedo ser creado",
            timer: 3000
          });
        });
    },
    saveImage() {
      let formData = new FormData();
      formData.append('file', this.form.file);
      // formData.append('company_id', this.form.company_id);
      formData.append('drone_id',this.form.drone_id);
      formData.append('inspection_id',this.form.inspection_id);
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/images/",
        method: "post",
        data: formData,
        headers: {'Content-Type': 'multipart/form-data'}
      })
        .then(res => {
          console.log(res);
          swal({
            type: "success",
            icon: "success",
            title: "Proceso completado",
            text: "La imagen fue cargada exitosamente",
            timer: 3000
          });
          this.resetForm();
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "El usuario no puedo ser creado",
            timer: 3000
          });
        });
    },
    resetForm(){
      this.form.drone_id = null;
      this.form.inspection_id = null;
      this.form.file = null;
    },
    handleFileUpload(event) {
      this.form.file = event.target.files[0]
    }
  }
};
</script>
<style>
</style>