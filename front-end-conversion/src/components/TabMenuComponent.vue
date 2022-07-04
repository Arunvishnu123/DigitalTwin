<template>
<div>
    <TabMenu class="navbar" :model="items" />
    <router-view />
</div>
</template>

<script>
import {
    ref
} from 'vue';
export default {
    setup() {
        const items = ref([{
                label: 'Home',
                icon: 'pi pi-fw pi-home',
                to: '/'
            }, {
                label: 'IFC to RDF Conversion',
                icon: 'pi pi-fw pi-copy',
                to: '/uploadfile'
            },
            {
                label: 'ADD Knowledge',
                icon: 'pi pi-fw pi-arrows-h',
                to: '/addKnowledge'
            },

            {
                label: 'Update Knowledge',
                icon: 'pi pi-fw pi-sort-amount-up-alt',
                to: '/updateknowledge'
            },

              {
                label: 'Visualise Knowledge Graphs',
                icon: 'pi pi-fw pi-sliders-v',
                to: '/visualizeGraph'
            },
        ]);

        return {
            items
        }
    }

}
</script>

<style  scoped>

</style>
