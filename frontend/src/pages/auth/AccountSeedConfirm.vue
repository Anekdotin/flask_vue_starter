<template>
  <q-page class="docs-input row justify-center">

    <div class="col-xs-12 col-sm-6 col-md-4  col-auto q-pt-xl ">
      <p class="text-center ">
        In order to unlock your account, please enter your account seed below.
      </p>
      <q-form
        class="q-px-sm q-pt-xl"
        method="POST"
        @submit="onSubmit"
      >
        <div class="q-gutter-md  q-pa-lg formlayout">
          <div class="row">
            <div class="col-xs-12 text-center text-h4">
              Unlock Account
            </div>
          </div>
          <q-input
            outlined
            v-model="wordForm.word0"
            label="Word 1"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <q-input
            outlined
            v-model="wordForm.word1"
            label="Word 2"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <q-input
            outlined
            v-model="wordForm.word2"
            label="Word 3"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <q-input
            outlined
            v-model="wordForm.word3"
            label="Word 4"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <q-input
            outlined
            v-model="wordForm.word4"
            label="Word 5"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <q-input
            outlined
            v-model="wordForm.word5"
            label="Word 6"
            autocomplete="off"
            :dense="wordForm.dense"
          />
          <div class="q-pa-md doc-container">
            <div class="row justify-end">
              <q-btn
                class="full-width"
                type="submit"
                color="secondary"
                label="Register"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-xs-12 text-center q-mb-md">
              Want to Register? <router-link to="/register">Register</router-link>
            </div>

            <div class="col-xs-12 text-center ">
              Login Here <router-link to="/login">Login</router-link>
            </div>
          </div>
        </div>
      </q-form>
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
        method: 'post',
        url: '/auth/accountseedconfirm',
        data: payLoad,
      })
        .then((response) => {
          if (response.data.status == "success") {

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
            }else if (error.response.status === 409) {
              this.$q.notify({
                type: 'negative',
                message: 'Error: Seed does not match',
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
    onSubmit() {
      const payLoad = {
        word0: this.wordForm.word0,
        word1: this.wordForm.word1,
        word2: this.wordForm.word2,
        word3: this.wordForm.word3,
        word4: this.wordForm.word4,
        word5: this.wordForm.word5,
      };
      this.sendWordRequest(payLoad);
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
