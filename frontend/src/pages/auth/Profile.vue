<template>


  <div class="col-xs-12 text-center q-mb-md">

    <h3 v-if="user">

      {{user.user_name}}
    </h3>

    <h3 v-if="user">
   
      </h3>
    {{user.user_id}}

    
  </div>
</template>

<script lang="ts">
import { mapGetters } from 'vuex';
import { defineComponent } from 'vue';


export default defineComponent({
  name: 'Home',


  computed: {
    ...mapGetters(['user'])

  }

});

</script>


<style type="ts" scoped>
</style>