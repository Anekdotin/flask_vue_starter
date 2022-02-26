<template>
  <q-layout view="hHh lpR fFf">

    <q-header
      reveal
      elevated
      class="bg-primary text-white"
    >
      <q-toolbar>
        <q-toolbar-title>
               <router-link to="/">Clearnet Market</router-link>
   
        </q-toolbar-title>
        <div v-if="user">
          <q-btn
            class="q-ma-sm"
            color="secondary"
            label="Logout"
            @click.prevent
            @click="logout()"

          />

        </div>
        <div v-if="!user">
          <q-btn
            href="/login"
            class="q-ma-sm"
            color="None"
            label="Sign In"
          />
          <q-btn
            href="/register"
            class="q-ma-sm"
            color="secondary"
            label="Register"
          />
        </div>
      </q-toolbar>

    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { mapGetters } from 'vuex';
export default defineComponent({
  name: 'MainLayout',

  computed: {
    ...mapGetters(['user']),
  },

  methods: {
    logout() {
      localStorage.clear();
      this.$store.dispatch('user', null);
      this.$q.notify({
        type: 'negative',
        message: 'You are now logged out.',
        badgeStyle: 'opacity: 0',
        position: 'top',
      });
  
      
    },
  },
});
</script>

