<template>
  <div class="todo">
    <div class="uk-container" v-if="!connection_state">
      <div class="spinner" uk-spinner="ratio: 3">
      </div>
    </div>
    <div class="uk-container" v-else>
      <h1>Todo-List</h1>
      <div class="uk-grid">
        <div class="uk-card uk-card-default uk-card-body uk-width-1-3@m" v-for="todo_list in todo_lists[0]">
          <h3 class="uk-card-title">{{ todo_list.list_name }}</h3>
          <ul class="uk-list">
            <li v-for="task in todo_list.tasks" >
              <span v-if=" task.done === 'false' ">{{ task.task_name }}</span>
              <span v-else="task.done === 'true' "> <s>{{ task.task_name }}</s></span>
            </li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  computed: {
    connection_state() {
      return this.$store.state.connection.isConnected
    },
    todo_lists(){
      return this.$store.state.todo.todo_list
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spinner {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%)
}
</style>
