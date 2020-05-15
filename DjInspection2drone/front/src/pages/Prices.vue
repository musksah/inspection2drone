<template>
  <div>
    <m-header></m-header>
    <!-- <div class="container">
      <h2 style="text-align:center">Precios Dronianalyzer</h2>
    <p style="text-align:center">Nuestros planes y precios están pensados para tu comodidad.</p>-->
    <!-- Contenedor -->
    <div class="pricing-wrapper clearfix" style="margin-top:9rem; margin-bottom:3rem;">
      <!-- Titulo -->
      <h1 class="pricing-table-title text-center" style="color:#454545;">
        Tabla de Precios DroneIAnalyzer
      </h1>

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
            <span>Fotografías / mes </span>
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
        <div class="table-buy">
          <p>
            $60
            <sup>/ mes</sup>
          </p>
		  <router-link class="pricing-action" :to="{name:'pay'}">Comprar</router-link>
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

      <div class="pricing-table">
        <h3 class="pricing-title" style="background: #58DA77; color:#454545;"> PLatino</h3>
        <div class="price">
          $200
          <sup>/ mes</sup>
        </div>
        <!-- Lista de Caracteristicas / Propiedades -->
        <ul class="table-list">
          <li>
            30 
            <span>Fotografías / mes </span>
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
        <div class="table-buy">
          <p>
            $200
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
	color: #FFF;
	margin-top: 15px;
	text-align: left;
	margin-bottom: 25px;
	text-shadow: 0 1px 1px rgba(0,0,0,0.4);
}

.pricing-table-title a {
	font-size: 0.6em;
}

.clearfix:after {
	content: '';
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
	font-family: 'Roboto', Arial, Helvetica, Sans-serif, Verdana;
  color: white;
	width: 960px;
	margin: 40px auto 0;
}

.pricing-table {
	margin: 0 10px;
	text-align: center;
	width: 300px;
	float: left;
	-webkit-box-shadow: 0 0 15px rgba(0,0,0,0.4);
	box-shadow: 0 0 15px rgba(0,0,0,0.4);
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
	color: #FFF;
	background: #e95846;
	padding: 20px 0;
	font-size: 2em;
	text-transform: uppercase;
	text-shadow: 0 1px 1px rgba(0,0,0,0.4);
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
	text-shadow: 0 1px 1px rgba(0,0,0,0.4);
}

.pricing-table .price sup {
	font-size: 0.4em;
	position: relative;
	left: 5px;
}

.table-list {
	background: #FFF;
	color: #403d3a;
}

.table-list li {
	font-size: 1.4em;
	font-weight: 700;
	padding: 12px 8px;
}

.table-list li:before {
	content: "\f00c";
	font-family: 'FontAwesome';
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
	color: #FFF;
	background: #e95846;
	font-size: 0.9em;
	padding: 5px 7px;
	display: inline-block;
	-webkit-border-radius: 38px;
	-moz-border-radius: 38px;
	border-radius: 38px;
}


.table-list li:nth-child(2n) {
	background: #F0F0F0;
}

.table-buy {
	background: #FFF;
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
	color: #FFF;
	background: #e95846;
	padding: 10px 16px;
	-webkit-border-radius: 2px;
	-moz-border-radius: 2px;
	border-radius: 2px;
	font-weight: 700;
	font-size: 1.4em;
	text-shadow: 0 1px 1px rgba(0,0,0,0.4);
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