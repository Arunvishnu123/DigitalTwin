<template>
<div>
    <TabMenu class="navbar" :model="items" />
    <router-view />
</div>
</template>

<script>
import { ref } from 'vue';
export default {
    setup() {
           const items = ref([{
                    label: 'IFC to RDF Conversion',
                    icon: 'pi pi-fw pi-copy',
                    to: '/uploadfile'
                },
                {
                    label: 'ADD Knowledge',
                    icon: 'pi pi-fw pi-arrows-h',
                    to: '/addKnowledge'
                },
            ]);

            return { items }
        }
    
}
</script>

<style  scoped>

</style>