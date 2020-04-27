<template>
  <card class="card" title="Módulo de Carga de Fotografías">
    <div>
      <form @submit.prevent class="mt-2 mb-4">
        <div class="row">
          <div class="col-md-4">
            <select class="custom-select">
              <option selected>Compañía</option>
              <option value="Coca Cola">Coca Cola</option>
              <option value="Pepsi">Pepsi</option>
              <option value="Sprite">Sprite</option>
            </select>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <input type="file" @change="processFile($event)" />
          </div>
        </div>
      </form>
    </div>
  </card>
</template>
<script>
export default {
  data() {
    return {
      file: "",
      company: ""
    };
  },
  methods: {
    processFile(event) {
      this.someData = event.target.files[0];
    }
  }
};
</script>
<style>
</style>