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
    <b-button v-b-modal.modal-form-users>Registrar Usuario</b-button>
    <b-modal id="modal-form-users" size="lg" ok-disabled="true" title="Registrar Usuario">
      <b-form @submit.prevent="register" @reset="onReset" v-if="show">
        <div class="row">
          <div class="col-md-6">
            <b-form-group id="first_name-group" label="Nombre:" label-for="first_name" style="margin-bottom:0;">
              <b-form-input
                id="first_name"
                v-model="form.first_name"
                type="text"
                required
                placeholder="Ingresar nombre"
              ></b-form-input>
            </b-form-group>
          </div>
          <div class="col-md-6">
            <b-form-group id="last_name-group" label="Apellido:" label-for="last_name" style="margin-bottom:0;">
              <b-form-input
                id="last_name"
                v-model="form.last_name"
                type="text"
                required
                placeholder="Ingresar apellido"
              ></b-form-input>
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <b-form-group id="email-group" label="Email address:" label-for="email" style="margin-bottom:0;">
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                required
                placeholder="Enter email"
              ></b-form-input>
            </b-form-group>
          </div>
          <div class="col-md-6">
            <b-form-group id="username-group" label="Usuario:" label-for="username" style="margin-bottom:0;">
              <b-form-input
                id="username"
                v-model="form.username"
                type="text"
                required
                placeholder="Ingresar usuario"
              ></b-form-input>
            </b-form-group>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <b-form-group id="password-group" label="Contraseña:" label-for="password" style="margin-bottom:0;">
              <b-form-input
                id="input-1"
                v-model="form.password"
                type="password"
                required
                placeholder="Ingresar contraseña"
              ></b-form-input>
            </b-form-group>
          </div>
          <div class="col-md-6">
            <b-form-group id="company_id-group" label="Compañía:" label-for="company_id" style="margin-bottom:0;">
              <b-form-select v-model="form.company_id" :options="options_company"></b-form-select>
            </b-form-group>
          </div>
        </div>
        <div class="row mb-2">
          <div class="col-md-6">
            <b-form-group id="profile_id-group" label="Perfil:" label-for="profile_id">
              <b-form-select v-model="form.profile_id" :options="options_profile"></b-form-select>
            </b-form-group>
          </div>
        </div>
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
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        company_id: null,
        profile_id: null
      },
      frameworkComponents: null,
      context: null,
      show: true,
      options_company: [{ value: null, text: "seleccionar..." }],
      options_profile: [
        { value: null, text: "seleccionar..." },
        { value: 1, text: "Administrador" },
        { value: 2, text: "Operador" },
        { value: 3, text: "Cliente" }
      ]
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
      const axiosInstance = axios.create(this.base_instance_axios);
      axiosInstance({
        url: "/users/list/",
        method: "POST",
        params: this.form
      })
        .then(res => {
          console.log(res);
          swal({
            type: "success",
            icon: "success",
            title: "Proceso Completado",
            text: "El usuario ha sido creado correctamente",
            timer: 3000
          });
          this.getList();
          this.$bvModal.hide('modal-form-users');
        })
        .catch(e => {
          this.loading = false;
          swal({
            type: "error",
            icon: "error",
            title: "Error",
            text: "El usuario no pudo ser creado",
            timer: 3000
          });
        });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.first_name = "";
      this.form.last_name = "";
      this.form.email = "";
      this.form.password = "";
      this.form.company_id = null;
      this.form.profile_id = null;
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