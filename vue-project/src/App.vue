<template>
  <n-button class="my-buttom" v-on:click="()=>{
    showModel = !showModel
  }">Add Hero</n-button>
  <div>
    <div v-for="hero in heros" v-bind:key="hero.id">{{ hero.name }}</div>
  </div>

  <HeroModel v-if="showModel" v-on:close="()=>{
    showModel = false
  }"></HeroModel>
</template>


<script setup lang="ts">
import { NButton } from 'naive-ui'
import { ref, onMounted } from 'vue';
import HeroModel from './components/HeroModel.vue';

interface IHero{
  id: number
  name: string
  age?: number
  secret: string
}

const loading = ref<boolean>(false);
const error = ref<string>('');
const heros = ref<IHero[]>([]);
const showModel = ref<boolean>(false);
const fetchHeros=async()=>{
  try {
    loading.value = true;
    const res = await fetch("http://127.0.0.1:8000/heros/?offset=0&limit=100")
    if(!res.ok) throw new Error("Failed to fetch!")
    heros.value = await res.json()
  } catch (err: any) {
    error.value = err.message
  }finally{
    loading.value = false;
  }
}

onMounted(fetchHeros)
</script>

<style scoped>
.my-buttom {
  margin: 20px;
}
</style>