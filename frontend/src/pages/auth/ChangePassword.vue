<template>
  <q-page class="docs-input row justify-center">

    <div class="col-xs-12 col-sm-6 col-md-4  col-auto q-pt-xl ">
      <p class="text-center ">
        If your account has been unlocked, you can change your password
      </p>
      <q-form
        class="q-px-sm q-pt-xl"
        method="POST"
        @submit="onSubmit"
      >
        <div class="q-gutter-md  q-pa-lg formlayout">
          <div class="row">
            <div class="col-xs-12 text-center text-h4">
              Enter New Password
            </div>
          </div>
          <q-input
            outlined
            v-model="ChangePasswordForm.password"
            label="Word 1"
            autocomplete="off"
            :dense="ChangePasswordForm.dense"
          />
          <q-input
            outlined
            v-model="ChangePasswordForm.password_confirm"
            label="Word 2"
            autocomplete="off"
            :dense="ChangePasswordForm.dense"
          />

          <div class="q-pa-md doc-container">
            <div class="row justify-end">
              <q-btn
                class="full-width"
                type="submit"
                color="secondary"
                label="Change Password"
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
  name: 'changepassword',

  data() {
    return {
      ChangePasswordForm: {
        password: '',
        password_confirm: '',

        dense: ref(true),
      },
    };
  },

  methods: {
    sendWordRequest(payLoad: { password: string; password_confirm: string }) {
      axios({
        method: 'post',
        url: '/auth/change-password',
        data: payLoad,
      })
        .then((response) => {
          if (response.data.status == 'success') {
            this.$q.notify({
              type: 'positive',
              message: 'Password Has been changed',
              position: 'top',
            });
            this.$router.push('/login');
          }
        })
        .catch((error) => {
          if (error.response) {
            if (error.response.status === 401) {
              this.$q.notify({
                type: 'negative',
                message: 'Error: Unauthorized',
                position: 'top',
              });
            } else if (error.response.status === 403) {
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
      console.log('Submitted');
      const payLoad = {
        password: this.ChangePasswordForm.password,
        password_confirm: this.ChangePasswordForm.password_confirm,
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
