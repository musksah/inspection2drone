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
          :frameworkComponents="frameworkComponents"
          pagination="true"
        ></ag-grid-vue>
      </div>
    </div>
    <b-button v-b-modal.modal-1>Registrar Usuario</b-button>
    <b-modal id="modal-1" title="Registrar Usuario">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Email address:"
          label-for="input-1"
          description="We'll never share your email with anyone else."
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
          <b-form-input id="input-2" v-model="form.name" required placeholder="Enter name"></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Food:" label-for="input-3">
          <b-form-select id="input-3" v-model="form.food" required></b-form-select>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
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
        email: "",
        name: "",
        food: null,
        checked: []
      },
      frameworkComponents:null,
      context:null,
      show: true
    };
  },
  components: {
    AgGridVue
  },
  beforeMount() {
    this.base_instance_axios = this.$store.getters.getBaseInstanceAxios
    this.context = { componentParent: this };
    this.frameworkComponents = {
      squareRenderer: SquareRenderer,
      cubeRenderer: CubeRenderer,
      paramsRenderer: ParamsRenderer,
      currencyRenderer: CurrencyRenderer,
      childMessageRenderer: ChildMessageRenderer,
    };
    
  },
  mounted() {
    this.getList();
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
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
          let fields_excluded = ['password','is_superuser','last_login','is_staff','is_active','user_permissions']
          // console.log(res);
          // debugger
          res.data.forEach(item => {
            Object.keys(item).forEach(key => {
              if(!fields_excluded.includes(key)){
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
              company: item.company,
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