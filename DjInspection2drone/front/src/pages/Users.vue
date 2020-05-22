<template>
  <div>
    <div class="row">
      <div class="col-md-12">
        <ag-grid-vue
          style="width: auto; height: 300px;"
          class="ag-theme-balham"
          :columnDefs="columnDefs"
          :rowData="rowData"
          :context="context"
          pagination="true"
        ></ag-grid-vue>
      </div>
    </div>
    <b-button v-b-modal.modal-1>Registrar Usuario</b-button>
    <b-modal id="modal-1" title="Registrar Usuario">
      <b-form @submit.prevent="onSubmit" @reset="register" v-if="show">
        <b-form-group id="first_name-group" label="Nombre:" label-for="first_name">
          <b-form-input
            id="first_name"
            v-model="form.first_name"
            type="text"
            required
            placeholder="Ingresar nombre"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="last_name-group" label="Apellido:" label-for="last_name">
          <b-form-input
            id="last_name"
            v-model="form.last_name"
            type="text"
            required
            placeholder="Ingresar apellido"
          ></b-form-input>
        </b-form-group>
        <b-form-group id="input-group-1" label="Email address:" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="password-group"
          label="Contraseña:"
          label-for="password"
          description="La contraseña debe tener mínimo 8 dígitos."
        >
          <b-form-input
            id="input-1"
            v-model="form.password"
            type="password"
            required
            placeholder="Ingresar contraseña"
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="company_id-group"
          label="Compañía:"
          label-for="company_id"
        >
          <b-form-select v-model="form.company_id" :options="options_company"></b-form-select>
        </b-form-group>
        <b-button class="mr-2" type="submit" variant="primary">Registrar</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-balham.css";
import { AgGridVue } from "ag-grid-vue";
export default {
  data() {
    return {
      columnDefs: [],
      rowData: [],
      form: {
        first_name:"",
        last_name:"",
        email: "",
        password: "",
        company_id:null,
      },
      frameworkComponents: null,
      context: null,
      show: true,
      options_company: [{ value: null, text: "seleccionar..." }],
    };
  },
  components: {
    AgGridVue
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios;
    this.context = { componentParent: this };
  },
  mounted() {
    this.getList();
    this.getCompanies();
  },
  methods: {
    register(evt) {
      alert(JSON.stringify(this.form));
      // const axiosInstance = axios.create(this.base_instance_axios);
      // axiosInstance({
      //   url: "/users/list/",
      //   method: "get",
      //   params: {}
      // })
      //   .then(res => {
      //   })
      //   .catch(e => {
      //     this.loading = false;
      //     swal({
      //       type: "error",
      //       icon: "error",
      //       title: "Error",
      //       text: "El usaurio no puedo ser creado",
      //       timer: 3000
      //     });
      //   });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
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
        url: "/users/list/",
        method: "get",
        params: {}
      })
        .then(res => {
          let fields_excluded = [
            "password",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "user_permissions"
          ];
          // console.log(res);
          // debugger
          res.data.forEach(item => {
            Object.keys(item).forEach(key => {
              if (!fields_excluded.includes(key)) {
                this.columnDefs.push({ headerName: key, field: key });
              }
            });
            this.rowData.push({
              id: item.id,
              username: item.username,
              is_superuser: item.is_superuser,
              first_name: item.first_name,
              last_name: item.last_name,
              email: item.email,
              company: item.company
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
    },
    getCompanies() {
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/companies/",
        method: "get",
        params: {}
      })
        .then(res => {
          let fields_excluded = [
            "password",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "user_permissions"
          ];
          console.log(res);
          res.data.forEach(item => {
            this.options_company.push({ value: item.id, text: item.name });
          });
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "No se pudieron traer las compañías",
            timer: 3000
          });
        });
    }
  }
};
</script>