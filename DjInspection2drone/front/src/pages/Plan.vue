<template>
  <div>
    <div class="row">
      <div class="col-md-12">
        <ag-grid-vue
          style="width: auto; height: 300px;"
          class="ag-theme-balham"
          :columnDefs="columnDefs"
          :rowData="rowData"
          pagination="true"
        ></ag-grid-vue>
      </div>
    </div>
    <b-button v-b-modal.modal-form-plan>Registrar Plan</b-button>
    <b-modal id="modal-form-plan" title="Registrar Plan">
      <b-form @submit.prevent="Register" @reset="onReset" v-if="show">
        <b-form-group id="input-group-1" label="Nombre:" label-for="input-1">
          <b-form-input id="input-1" v-model="form.name" required placeholder="Ingresar nombre"></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Precio:" label-for="input-2">
          <b-form-input id="input-2" v-model="form.price" required placeholder="Ingresar Precio"></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Número Fotos:" label-for="input-3">
          <b-form-input
            type="number"
            id="input-3"
            v-model="form.photos_number"
            required
            placeholder="Ingresar número de fotos"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-4" label="Número de Usuarios:" label-for="input-4">
          <b-form-input
            type="number"
            id="input-4"
            v-model="form.user_number"
            required
            placeholder="Ingresar número de Usuarios"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-5" label="Número de Análisis:" label-for="input-5">
          <b-form-input
            type="number"
            id="input-5"
            v-model="form.analysis_number"
            required
            placeholder="Ingresar número de análisis"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-6" label="Duración en meses:" label-for="input-6">
          <b-form-input
            type="number"
            id="input-6"
            v-model="form.term_months_number"
            required
            placeholder="Ingresar duracion en meses"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-7" label="Número de Inspecciones:" label-for="input-7">
          <b-form-input
            type="number"
            id="input-7"
            v-model="form.inspection_number"
            required
            placeholder="Ingresar número de inspecciones"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Registrar</b-button>
        <b-button type="reset" variant="danger">Resetear</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-balham.css";
import { AgGridVue } from "ag-grid-vue";
import jwt_decode from "jwt-decode";
export default {
  data() {
    return {
      columnDefs: [],
      rowData: [],
      form: {
        name: "",
        price: "",
        photos_number: "",
        user_number: "",
        analysis_number: "",
        term_months_number: "",
        inspection_number: ""
      },
      show: true,
      loading: false,
      base_instance_axios:{}
    };
  },
  components: {
    AgGridVue
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios
  },
  mounted() {
    this.getList();
  },
  methods: {
    Register(evt) {
      this.loading = true;
      axios
        .post("http://127.0.0.1:8000/api/v1.0/plans/", this.form)
        .then(response => {
          swal("Plan creado exitosamente!", "", "success");
          this.$bvModal.hide("modal-form-plan");
        })
        .catch(err => {
          swal("El libro no ha sido creado!", "", "error");
        });
      this.getList();
    },
    onReset(evt) {
      // Reset our form values
      this.form.name = "";
      this.form.price = "";
      this.form.photos_number = "";
      this.form.user_number = "";
      this.form.analysis_number = "";
      this.form.term_months_number = "";
      this.form.inspection_number = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    getList() {
      this.columnDefs = [];
      this.rowData = [];
      
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/plans/",
        method: "get",
        params: {}
      }).then(res => {
          res.data.forEach(item => {
            Object.keys(item).forEach(key => {
              this.columnDefs.push({ headerName: key, field: key });
            });
            this.rowData.push({
              id: item.id,
              name: item.name,
              price: item.price,
              photos_number: item.photos_number,
              user_number: item.user_number,
              analysis_number: item.analysis_number,
              term_months_number: item.term_months_number,
              inspection_number: item.inspection_number
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