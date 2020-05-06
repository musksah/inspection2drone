<template>
  <card class="card" title="Editar Perfil">
    <div>
      <form @submit.prevent>
        <div class="row">
          <div class="col-md-5">
            <fg-input type="text"
                      label="Companía"
                      :disabled="true"
                      placeholder="Paper dashboard"
                      v-model="company">
            </fg-input>
          </div>
          <div class="col-md-3">

            <fg-input type="text"
                      label="Usuario"
                      placeholder="Username"
                      v-model="username">
            </fg-input>
          </div>
          <div class="col-md-4">
            <fg-input type="email"
                      label="Correo Electrónico"
                      placeholder="Email"
                      v-model="user.email">
            </fg-input>
          </div>
        </div>

        <div class="row">
          <div class="col-md-6">
            <fg-input type="text"
                      label="Nombres"
                      placeholder="First Name"
                      v-model="user.name">
            </fg-input>
          </div>
          <div class="col-md-6">
            <fg-input type="text"
                      label="Apellidos"
                      placeholder="Last Name"
                      v-model="user.lastname">
            </fg-input>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12">
            <fg-input type="text"
                      label="Dirección"
                      placeholder="Home Address"
                      v-model="user.address">
            </fg-input>
          </div>
        </div>
        <div class="text-center">
          <p-button type="info"
                    round
                    @click.native.prevent="updateProfile">
            Actualizar Perfil
          </p-button>
        </div>
        <div class="clearfix"></div>
      </form>
    </div>
  </card>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      user: {
        company: "",
        username: "",
        email: "",
        name: "",
        lastname: "",
        address: "",
      },
      username:this.$store.state.username,
      company:"DroneIAnalyzer"
    };
  },
  mounted() {
    this.getDataProfile();
  },
  methods: {
    updateProfile() {
      alert("Your data: " + JSON.stringify(this.user));
    },
    getDataProfile() {
      const axiosInstance = axios.create(this.$store.getters.getBaseInstanceAxios);
      axiosInstance({
        url: "/pilots/",
        method: "get",
        params: {}
      })
        .then(res => {
          console.log(res);
          // debugger
          this.user = res.data[0].fields
        })
        .catch(e => {});
    }
  }
};
</script>
<style>
</style>
