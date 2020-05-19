<template>
  <div>
    <m-header></m-header>
    <!-- Contenedor -->
    <b-container>
      <div class="row" style="margin-top:5rem;margin-bottom:3rem;">
        <div class="col-md-12">
          <form @submit.stop.prevent="register">
            <h4>Información Personal</h4>
            <hr />
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputName">Nombres</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputName"
                  aria-describedby="emailHelp"
                  placeholder="Ingresar nombres"
                  v-model="form.first_name"
                />
                <!-- <small
                    id="emailHelp"
                    class="form-text text-muted"
                >We'll never share your email with anyone else.</small>-->
              </div>
              <div class="col-md-6">
                <label for="registerInputLastName">Apellidos</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputLastName"
                  placeholder="Ingresar apellidos"
                  v-model="form.last_name"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputEmail">Correo Electrónico</label>
                <input
                  type="email"
                  class="form-control"
                  id="registerInputEmail"
                  aria-describedby="emailHelp"
                  placeholder="Ingresar email"
                  v-model="form.email"
                />
              </div>
              <div class="col-md-6">
                <label for="registerInputUser">Usuario</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputUser"
                  placeholder="Ingresar usuario"
                  v-model="form.username"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputPassword">Contraseña</label>
                <input
                  type="password"
                  class="form-control"
                  id="registerInputPassword"
                  placeholder="Ingresar contraseña"
                  v-model="form.password"
                />
              </div>
              <div class="col-md-6">
                <label for="registerInputRePassword">Confirmar contraseña</label>
                <input
                  type="password"
                  class="form-control"
                  id="registerInputRePassword"
                  placeholder="Confirmar contraseña"
                  v-model="form.re_password"
                />
              </div>
            </div>
            <!-- <hr/> -->
            <h4>Información de la compañía</h4>
            <hr />
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputNit">Nit</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputNit"
                  placeholder="Ingresar nit"
                  v-model="form.company.nit"
                />
              </div>
              <div class="col-md-6">
                <label for="registerInputNameCompany">Nombre de la compañía</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputNameCompany"
                  placeholder="Ingresar nombre de compañía"
                  v-model="form.company.name"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputEmailCompany">Correo Electrónico Company</label>
                <input
                  type="email"
                  class="form-control"
                  id="registerInputEmailCompany"
                  placeholder="Ingresar correo compañía"
                  v-model="form.company.email"
                />
              </div>
              <div class="col-md-6">
                <label for="registerInputPhoneNumber">Número de Teléfono</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputPhoneNumber"
                  placeholder="Ingresar numero telefónico"
                  v-model="form.company.phone_number"
                />
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <label for="registerInputAddressCompany">Dirección</label>
                <input
                  type="text"
                  class="form-control"
                  id="registerInputAddressCompany"
                  placeholder="Ingresar dirección compañía"
                  v-model="form.company.address"
                />
              </div>
            </div>
            <h4>Elegir un plan</h4>
            <hr />
            <div class="pricing-wrapper clearfix" style="margin-bottom:3rem;">
              <b-form-group label="Radios using sub-components">
                <b-form-radio-group
                  id="radio-group-2"
                  v-model="form.plan"
                  name="radio-sub-component"
                >
                  <!-- Titulo -->
                  <div class="pricing-table">
                    <h3 class="pricing-title" style="background: #D8D8D8; color:#454545;">Plata</h3>
                    <div class="price">
                      $60
                      <sup>/ mes</sup>
                    </div>
                    <!-- Lista de Caracteristicas / Propiedades -->
                    <ul class="table-list">
                      <li>
                        15
                        <span>Fotografías / mes</span>
                      </li>
                      <li>
                        3
                        <span>Inspecciones / mes</span>
                      </li>
                      <li>
                        8
                        <span>análisis con IA / mes</span>
                      </li>
                      <li>
                        1
                        <span class="unlimited">Usuario Full</span>
                      </li>
                    </ul>
                    <!-- Contratar / Comprar -->
                    <div class="table-buy" style="text-align:center;margin-bottom:1rem;">
                      <div class="custom-control custom-radio custom-control-inline">
                        <b-form-radio value="1" class="label-prices">Seleccionar</b-form-radio>
                        <!-- <input
                          type="radio"
                          id="radioPlan3"
                          name="radioPlan"
                          class="custom-control-input"
                        />
                        <label
                          class="custom-control-label label-prices"
                          for="radioPlan3"
                        >Seleccionar</label>-->
                      </div>
                    </div>
                  </div>
                  <div class="pricing-table">
                    <h3 class="pricing-title" style="background: #E3D83D; color:#454545;">Oro</h3>
                    <div class="price">
                      $100
                      <sup>/ mes</sup>
                    </div>
                    <!-- Lista de Caracteristicas / Propiedades -->
                    <ul class="table-list">
                      <li>
                        20
                        <span>Fotografías / mes</span>
                      </li>
                      <li>
                        4
                        <span>Inspecciones / mes</span>
                      </li>
                      <li>
                        10
                        <span>análisis con IA / mes</span>
                      </li>
                      <li>
                        2
                        <span class="unlimited">Usuarios Full</span>
                      </li>
                    </ul>
                    <!-- Contratar / Comprar -->
                    <div class="table-buy" style="text-align:center;margin-bottom:1rem;">
                      <b-form-radio value="2" class="label-prices">Seleccionar</b-form-radio>
                      <!-- <input
                          type="radio"
                          id="radioPlan2"
                          name="radioPlan"
                          class="custom-control-input"
                      />-->
                      <!-- <label
                          class="custom-control-label label-prices"
                          for="radioPlan2"
                      >Seleccionar</label>-->
                    </div>
                  </div>
                  <div class="pricing-table">
                    <h3 class="pricing-title" style="background: #58DA77; color:#454545;">PLatino</h3>
                    <div class="price">
                      $200
                      <sup>/ mes</sup>
                    </div>
                    <!-- Lista de Caracteristicas / Propiedades -->
                    <ul class="table-list">
                      <li>
                        30
                        <span>Fotografías / mes</span>
                      </li>
                      <li>
                        4
                        <span>Inspecciones / mes</span>
                      </li>
                      <li>
                        15
                        <span>análisis con IA / mes</span>
                      </li>
                      <li>
                        4
                        <span class="unlimited">Usuarios Full</span>
                      </li>
                    </ul>
                    <!-- Contratar / Comprar -->
                    <div class="table-buy" style="text-align:center;margin-bottom:1rem;">
                      <div class="custom-control custom-radio custom-control-inline">
                        <b-form-radio value="3" class="label-prices">Seleccionar</b-form-radio>
                        <!-- <input
                          type="radio"
                          id="radioPlan1"
                          name="radioPlan"
                          class="custom-control-input"
                          v-model="form.plan"
                        />
                        <label
                          class="custom-control-label label-prices"
                          for="radioPlan1"
                        >Seleccionar</label>-->
                      </div>
                    </div>
                  </div>
                </b-form-radio-group>
              </b-form-group>
            </div>
            <div class="row">
              <div class="col-md-12 text-center">
                <input type="submit" value="Registrar y Pasar al Pago" class="btn btn-primary" />
              </div>
            </div>
          </form>
        </div>
      </div>
    </b-container>
    <starter-footer></starter-footer>
  </div>
</template>
<script>
import axios from "axios";
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
export default {
  components: {
    "m-header": StarterHeader,
    StarterFooter
  },
  data() {
    return {
      form: {
        plan: "",
        first_name: "",
        last_name: "",
        username: "",
        company: {
          nit: "",
          name: "",
          email: "",
          phone_number: "",
          address: ""
        }
      }
    };
  },
  methods: {
    register(evt) {
      // this.loading = true;
      const axiosInstance = axios.create(this.$store.getters.getBaseInstanceAxios);
      axiosInstance({
        url: "/user/new-customer/",
        method: "post",
        data: this.form
      })
        .then(res => {
          console.log(res);
          swal({
            type: "success",
            icon: "success",
            title: "Usuario Creado",
            text: "El usuario fue creado exitosamente!",
            timer: 3000
          });
          this.$router.push("/pay");
          // let fields_excluded = [
          //   "password",
          //   "is_superuser",
          //   "last_login",
          //   "is_staff",
          //   "is_active",
          //   "user_permissions"
          // ];
          // console.log(res);
          // debugger
          // res.data.forEach(item => {
          //   Object.keys(item).forEach(key => {
          //     if (!fields_excluded.includes(key)) {
          //       this.columnDefs.push({ headerName: key, field: key });
          //     }
          //   });
          //   this.rowData.push({
          //     id: item.id,
          //     username: item.username,
          //     is_superuser: item.is_superuser,
          //     first_name: item.first_name,
          //     last_name: item.last_name,
          //     email: item.email,
          //     company: item.company
          //   });
          // });
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
<style lang="css">
* {
  margin: 0;
  padding: 0;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.pricing-wrapper ul {
  list-style-type: none;
}

.pricing-wrapper a {
  color: #e95846;
  text-decoration: none;
}

.pricing-table-title {
  text-transform: uppercase;
  font-weight: 700;
  font-size: 2.6em;
  color: #fff;
  margin-top: 15px;
  text-align: left;
  margin-bottom: 25px;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);
}

.pricing-table-title a {
  font-size: 0.6em;
}

.clearfix:after {
  content: "";
  display: block;
  height: 0;
  width: 0;
  clear: both;
}
/** ========================
 * Contenedor
 ============================*/
.pricing-wrapper {
  font-size: 62.5%;
  font-family: "Roboto", Arial, Helvetica, Sans-serif, Verdana;
  color: white;
  width: 960px;
  margin: 40px auto 0;
}

.pricing-table {
  margin: 0 10px;
  text-align: center;
  width: 300px;
  float: left;
  -webkit-box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.4);
  -webkit-transition: all 0.25s ease;
  -o-transition: all 0.25s ease;
  transition: all 0.25s ease;
}

.pricing-table:hover {
  -webkit-transform: scale(1.06);
  -ms-transform: scale(1.06);
  -o-transform: scale(1.06);
  transform: scale(1.06);
}

.pricing-title {
  color: #fff;
  background: #e95846;
  padding: 20px 0;
  font-size: 2em;
  text-transform: uppercase;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);
}

.pricing-table.recommended .pricing-title {
  background: #2db3cb;
}

.pricing-table.recommended .pricing-action {
  background: #2db3cb;
}

.pricing-table .price {
  background: #403e3d;
  font-size: 3.4em;
  font-weight: 700;
  padding: 20px 0;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);
}

.pricing-table .price sup {
  font-size: 0.4em;
  position: relative;
  left: 5px;
}

.table-list {
  background: #fff;
  color: #403d3a;
}

.table-list li {
  font-size: 1.4em;
  font-weight: 700;
  padding: 12px 8px;
}

.table-list li:before {
  content: "\f00c";
  font-family: "FontAwesome";
  color: #3fab91;
  display: inline-block;
  position: relative;
  right: 5px;
  font-size: 16px;
}

.table-list li span {
  font-weight: 400;
}

.table-list li span.unlimited {
  color: #fff;
  background: #e95846;
  font-size: 0.9em;
  padding: 5px 7px;
  display: inline-block;
  -webkit-border-radius: 38px;
  -moz-border-radius: 38px;
  border-radius: 38px;
}

.table-list li:nth-child(2n) {
  background: #f0f0f0;
}

.table-buy {
  background: #fff;
  padding: 15px;
  text-align: left;
  overflow: hidden;
}

.table-buy p {
  float: left;
  color: #37353a;
  font-weight: 700;
  font-size: 2.4em;
}

.table-buy p sup {
  font-size: 0.5em;
  position: relative;
  left: 5px;
}

.table-buy .pricing-action {
  float: right;
  color: #fff;
  background: #e95846;
  padding: 10px 16px;
  -webkit-border-radius: 2px;
  -moz-border-radius: 2px;
  border-radius: 2px;
  font-weight: 700;
  font-size: 1.4em;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.4);
  -webkit-transition: all 0.25s ease;
  -o-transition: all 0.25s ease;
  transition: all 0.25s ease;
}

.table-buy .pricing-action:hover {
  background: #cf4f3e;
}

.recommended .table-buy .pricing-action:hover {
  background: #228799;
}

.label-prices {
  color: #37353a;
  font-weight: 700;
  font-size: 2.4em;
  line-height: 1.4em;
  -webkit-font-smoothing: antialiased;
  font-family: "Muli", "Helvetica", Arial, sans-serif;
  margin-top: 0;
  cursor: pointer;
  margin-bottom: 1rem !important;
}

/** ================
 * Responsive
 ===================*/
@media only screen and (min-width: 768px) and (max-width: 959px) {
  .pricing-wrapper {
    width: 768px;
  }

  .pricing-table {
    width: 236px;
  }

  .table-list li {
    font-size: 1.3em;
  }
}

@media only screen and (max-width: 767px) {
  .pricing-wrapper {
    width: 420px;
  }

  .pricing-table {
    display: block;
    float: none;
    margin: 0 0 20px 0;
    width: 100%;
  }
}

@media only screen and (max-width: 479px) {
  .pricing-wrapper {
    width: 300px;
  }
}
</style>