<template>

  <div v-if="user">
    Welcome {{user.user_name}}
    </div>
   <div v-if="!user">Login</div>
  
</template>

<script lang="ts">
import { mapGetters } from 'vuex';
import { defineComponent } from 'vue';
import axios from 'axios';
import { useQuasar } from 'quasar';

export default defineComponent({
  name: 'Home',
 
  setup() {
    const $q = useQuasar();
  },
  mytoken(){

    },
  data() {
    return {
      token: null
    };
  },
  computed: {
    ...mapGetters(['user'])
  },
  
   methods: {
  
  },
});

</script>


<style type="ts" scoped>
</style>