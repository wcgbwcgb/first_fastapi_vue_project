<template>
  <div class="myCard">
    <n-card embedded :bordered="true" >
      <n-space vertical>
        <h2>Add Heros</h2>
        <n-input v-model:value="name" type="text" placeholder="name" />
        <n-input v-model:value="age" type="text" placeholder="age(optional)" />
        <n-input
          v-model:value="secretName"
          type="text"
          placeholder="secret name"
        />
        <n-button type="primary" class="my-buttom" v-on:click="save">Create</n-button>
        <n-button type="error" class="my-buttom" v-on:click="emits('close')">Cancel</n-button>
      </n-space>
    </n-card>
  </div>

</template>

<script setup lang="ts">
import { NInput, NButton, NCard, NSpace } from 'naive-ui'
import { ref } from 'vue';

const age = ref<string>('')
const name = ref<string>('')
const secretName = ref<string>('')
const emits = defineEmits(["close"]);

const save = async () => {
  const payload={
    name: name.value,
    age: age.value,
    secret_name: secretName.value,
  }
  try {
    let response;
    response = await fetch("http://127.0.0.1:8000/heros", {
    method: "POST",
    headers: {'Content-Type': "application/json"},
    body: JSON.stringify(payload)
  })
  if(!response.ok) throw new Error("Failed to save")
  const result = await response.json();
  console.log(result)
  } catch (err: any) {
    console.log(err);
  }
}

</script>

<style scoped>
.myCard {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
  width: 800px;
}

</style>
