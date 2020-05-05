<template>
  <div>
    <m-header></m-header>
    <main class="login-form" style="margin-top:7rem !important; margin-bottom:2rem !important;">
      <div class="cotainer">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <div class="card" style="background-color:#E2E2E2;">
              <div
                class="card-header pb-3"
                style="font-weight:700;background-color: #353E76;color:white;"
              >Registrarse</div>
              <div class="card-body">
                <v-layout row fill-height justify-center align-center v-if="loading" style="display:flex;justify-content:center;">
                    <v-progress-circular :size="50" color="primary" indeterminate />
                </v-layout>
                <form action method class="mt-3" @submit.prevent="Register">
                  <div class="form-group row">
                    <label
                      for="username"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Usuario</label>
                    <div class="col-md-6">
                      <input
                        type="text"
                        id="username"
                        class="form-control"
                        name="username"
                        required
                        autofocus
                        v-model="register.username"
                      />
                    </div>
                  </div>
                  <div class="form-group row">
                    <label
                      for="email"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Correo Electrónico</label>
                    <div class="col-md-6">
                      <input
                        type="text"
                        id="email"
                        class="form-control"
                        name="email"
                        required
                        autofocus
                        v-model="register.email"
                      />
                    </div>
                  </div>
                  <div class="form-group row">
                    <label
                      for="password"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Contraseña</label>
                    <div class="col-md-6">
                      <input
                        type="password"
                        id="password"
                        class="form-control"
                        name="password"
                        required
                        v-model="register.pwd"
                      />
                    </div>
                  </div>
                  <div class="form-group row">
                    <label
                      for="re_password"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Confirmar contraseña</label>
                    <div class="col-md-6">
                      <input
                        type="password"
                        id="re_password"
                        class="form-control"
                        name="re_password"
                        required
                        v-model="register.re_pwd"
                      />
                    </div>
                    <div v-if="register.pwd != register.re_pwd" class="col-md-6 offset-md-4 mb-2">
                      <span style="color:#C62020;font-weight:700;">Las contraseñas deben coincidir</span>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label
                      for="company_id"
                      class="col-md-4 col-form-label text-md-right"
                      style="color:#66615B;"
                    >Companía</label>
                    <div class="col-md-6">
                      <b-form-select v-model="register.company_id" :options="options"></b-form-select>
                    </div>
                  </div>
                  <div class="col-md-6 offset-md-4 mb-3">
                    <button type="submit" class="btn btn-primary">Registrarse</button>
                  </div>
                  <div class="col-md-6 offset-md-4 mb-4">
                    <router-link to="/login">¿Ya tienes una cuenta?</router-link>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    <starter-footer></starter-footer>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
export default {
  data() {
    return {
      register: {},
      loading: false,
      options: [{ value: null, text: "seleccionar..." },{ value:1, text: "SuperConstructora S.A.S" }],
    };
  },
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  methods: {
    Register() {
      // checking if the input is valid
      this.loading = true;
      axios
        .post("http://127.0.0.1:8000/api/v1.0/user/new/", this.register)
        .then(res => {
          console.log(res);
          swal({
            type: "success",
            icon: "success",
            title: "Proceso Completado",
            text: res.response,
            timer: 3000
          });
          this.$router.push("/login");
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
.my-form {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.my-form .row {
  margin-left: 0;
  margin-right: 0;
}

.login-form {
  padding-top: 1.5rem;
  padding-bottom: 1.5rem;
}

.login-form .row {
  margin-left: 0;
  margin-right: 0;
}
</style>