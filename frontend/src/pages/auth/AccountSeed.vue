<template>
  <q-page class="docs-input row justify-center">

    <div class="col-xs-12 col-sm-6 col-md-4  col-auto q-pt-xl ">
      <p class="text-center ">
        In order to unlock your account, please enter your account seed below.
      </p>
     
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import { ref } from 'vue';

export default defineComponent({
  name: 'forgotpassword',

  data() {
    return {
      wordForm: {
        word0: '',
        word1: '',
        word2: '',
        word3: '',
        word4: '',
        word5: '',

        dense: ref(true),
      },
    };
  },

  methods:
  {
    sendWordRequest(payLoad: {
      word0: string;
      word1: string;
      word2: string;
      word3: string;
      word4: string;
      word5: string;
    }) {
      axios({
        method: 'get',
        url: '/auth/account-seed',
        data: payLoad,
      })
        .then((response) => {
          if (response.data.status == 200) {

            this.$router.push('/');
          }
        })
        .catch((error) => {
          if (error.response)  {
            if (error.response.status === 401) {
              this.$q.notify({
                type: 'negative',
                message: 'Error: Unauthorized',
                position: 'top',
              });
            }
             else if (error.response.status === 403) {
              this.$q.notify({
                type: 'negative',
                message: 'Error: Forbidden',
                position: 'top',
              });
            } else {
              this.$q.notify({
                type: 'negative',
                message: 'Error',
              });
            }
          }
        });
    },
    
  },
});
</script>


<style type="ts" scoped>
.center_text {
  text-align: center;
  display: inline-block;
}
</style>
