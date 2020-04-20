<template>
  <div>
    <m-header></m-header>
    <main class="login-form" style="margin-top:7rem !important; margin-bottom:2rem !important;">
      <div class="cotainer">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <div class="card" style="background-color:#E2E2E2;">
              <div class="card-header pb-3" style="font-weight:700;background-color: #353E76;color:white;">Iniciar Sesión</div>
              <div class="card-body">
                <form action method class="mt-3">
                  <div class="form-group row">
                    <label
                      for="email_address"
                      class="col-md-4 col-form-label text-md-right" style="color:#66615B;"
                    >Correo Electrónico</label>
                    <div class="col-md-6">
                      <input
                        type="text"
                        id="email_address"
                        class="form-control"
                        name="email-address"
                        required
                        autofocus
                      />
                    </div>
                  </div>

                  <div class="form-group row">
                    <label for="password" class="col-md-4 col-form-label text-md-right" style="color:#66615B;">Contraseña</label>
                    <div class="col-md-6">
                      <input
                        type="password"
                        id="password"
                        class="form-control"
                        name="password"
                        required
                      />
                    </div>
                  </div>
<!-- 
                  <div class="form-group row">
                    <div class="col-md-6 offset-md-4">
                      <div class="checkbox">
                        <label>
                          <input type="checkbox" name="remember"/> Remember Me
                        </label>
                      </div>
                    </div>
                  </div> -->

                  <div class="col-md-6 offset-md-4 mb-3">
                    <button type="submit" class="btn btn-primary">Ingresar</button>
                    <a href="#" class="btn btn-link">Olvidó su contraseña?</a>
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
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
export default {
  components: {
    "m-header": StarterHeader,
    StarterFooter
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