<script setup>
let level = 0;
let topics = ["HTML", "CSS", "JS", "Vue.js"];
const mem = {
    [Symbol("怡珍")]:"物件型別練習",
};
const nen = Object.getOwnPropertySymbols(mem).map(item=>mem[item]);
console.log(nen)
const me = new Set(["hghg","adad"]);

me.add("yuy");
console.log(me.size);

const binm = (x,y) => x + y;
</script>
<template>
    <nav>基本的導覽列</nav>
    <main>基本的主內容</main>
    <div v-if="level === 3">大神會員</div>
    <div v-else-if="level === 2">高級會員</div>
    <div v-else-if="level === 1">中階會員</div>
    <div v-else>入門會員
        <div>入門資料</div>
        <ul>
            <li v-for="(name, index) in topics">{{ index }} - {{ name }}</li>
        </ul>
    </div>
</template>
<style scoped>
main {
    background-color: #fff;
}
</style>