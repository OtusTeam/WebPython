<script setup>
import { ref } from 'vue'

const name = ref('OTUS')
const count = ref(0)

const buttonIsBig = ref(false)
const buttonText = ref('Click me!')

const newTodoText = ref('')

function handleReset() {
  count.value = 0
  buttonIsBig.value = !buttonIsBig.value
  // buttonText.value = `Prev high ${count.value}`
}

let todoIds = 1

const todos = ref([
  {id: todoIds++, text: 'Todo 1'},
  {id: todoIds++, text: 'Todo 2'},
  {id: todoIds++, text: 'Todo 3'},
])

function addTodo() {
  todos.value.push({id: todoIds++, text: newTodoText.value})
  newTodoText.value = ''
}

function handleDeleteTodo(todo) {
  todos.value = todos.value.filter(t => t.id !== todo.id)
}


</script>

<template>

  <h2>Todo list</h2>

  <div v-if="todos.length">
    Your todos:
  </div>
  <div v-else>
    No todos, create a new one:
  </div>

  <ul v-if="todos.length">
    <li
      v-for="todo in todos"
      :key="todo.id"
    >
      {{ todo.text }}
      <input
        type="button"
        value="x"
        @click="handleDeleteTodo(todo)"
      >
    </li>
  </ul>

  <div>
    <form @submit.prevent="addTodo">
      <input type="text" v-model="newTodoText">
      <input type="submit" value="Add">
    </form>
    <div v-if="newTodoText.length">
      Your input: <span>{{ newTodoText }}</span>
    </div>
  </div>


  <br>
  <hr>
  <br>

  <h2>Hello {{ name }}!</h2>

  <h3>How many times can you click?</h3>
  <h4>Clicked <span>{{ count }}</span> times!</h4>
  <div>
    <input
      v-on:click="count++"
      :class="{'big-font': buttonIsBig}"
      type="button"
      :value="buttonText"
    >
    <br>
    <button @click="handleReset">
      Reset
    </button>
  </div>
</template>

<style>
.big-font {
  font-size: 25px;
}
</style>
