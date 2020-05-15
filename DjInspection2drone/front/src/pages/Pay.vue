<template>
  <div>
    <m-header></m-header>
    <b-container style="margin-top:10rem;">
        <form method="post" action="https://sandbox.checkout.payulatam.com/ppp-web-gateway-payu/">
          <input name="merchantId" type="hidden" value="508029" />
          <input name="accountId" type="hidden" value="512321" />
          <input name="description" type="hidden" value="Pago de Planes" />
          <input name="referenceCode" type="hidden" value="PAGO004" />
          <input name="amount" type="hidden" value="10000" />
          <input name="tax" type="hidden" value="0" />
          <input name="taxReturnBase" type="hidden" value="0" />
          <input name="currency" type="hidden" value="COP" />
          <input name="signature" type="hidden" value="a1cdf23e3072e62fe449060d2cf28fb9" />
          <input name="test" type="hidden" value="1" />
          <input name="buyerEmail" type="hidden" value="cliente1@drone.com" />
          <input name="responseUrl" type="hidden" value="http://localhost:8080/responsepay" />
          <input name="confirmationUrl" type="hidden" value="http://localhost:8080/confirmationpay" />
          <input name="Submit" type="submit" value="Enviar" />
        </form>
    </b-container>
    <div class="pricing-wrapper clearfix" style="margin-top:9rem; margin-bottom:3rem;">
      <!-- Titulo -->
      <h1 class="pricing-table-title text-center" style="color:#454545;">
        Tabla de Precios DroneIAnalyzer
      </h1>
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
            <span>Fotografías / mes </span>
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
        <div class="table-buy">
          <p>
            $100
            <sup>/ mes</sup>
          </p>
		  <router-link class="pricing-action" :to="{name:'pay'}">Comprar</router-link>
        </div>
      </div>
    </div>
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
<style lang="css">
</style>