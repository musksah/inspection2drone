<template>
  <div>
    <m-header></m-header>
    <starter-content></starter-content>
    <starter-footer></starter-footer>
  </div>
</template>

<script>
import StarterHeader from "@/layout/website/StarterHeader";
import StarterFooter from "@/layout/website/StarterFooter";
import StarterContent from "@/layout/website/StarterContent";
export default {
  components: {
    "m-header": StarterHeader,
    // "m-content":
    StarterFooter,
    StarterContent
  }
};
</script>