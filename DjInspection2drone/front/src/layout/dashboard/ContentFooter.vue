<template>
  <footer class="footer">
    <div class="container-fluid d-flex flex-wrap justify-content-between">
      <nav>
        <ul>
          <li>
            <router-link :to="{path:'/admin'}">Dashboard DroneIAnalyzer</router-link>
          </li>
        </ul>
      </nav>
      <div class="copyright d-flex flex-wrap">
        &copy; 2020 Modify
        <i class="fa fa-heart heart"></i> by
        <a href="https://github.com/musksah" target="_blank"> &nbsp; musksah.</a>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      
    }
  },
};
</script>
<style>
</style>
