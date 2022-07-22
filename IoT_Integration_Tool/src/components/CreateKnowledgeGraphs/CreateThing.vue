<template>
<div>
    <w-drawer width="120em" class="newthing" v-model="$store.state.createThing" :[position]="true">
        <w-button @click="$store.state.createThing = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="humidity" bg-color="primary">Create New Thing</w-tag>
            <w-form @submit.prevent="sendThing">
                <w-input v-model="thingType" class="mb6" label="Thing Type" outline> </w-input>
                <w-textarea outline>Thing Description</w-textarea>
                <w-flex>
                    <w-input class="mb6" label="Event based target" outline> </w-input>
                    <w-input class="mb6" label="Target type" outline> </w-input>
                </w-flex>
                <w-flex>
                    <w-input class="mb6" label="Histroical Target" outline> </w-input>
                    <w-input class="mb6" label="Target type" outline> </w-input>
                </w-flex>
                <w-flex>
                    <w-button type="submit" class="ma1 grow" bg-color="primary">Click here to create new thing</w-button>
                </w-flex>
            </w-form>
        </w-flex>
    </w-drawer>
</div>
</template>

<script>
import store from "../../store/index";
import axios from "axios";
export default {
    data: () => ({
        thingType: null,
        thingDescription: null,
        eventBasedTarget: null,
        eventTargetType: null,
        historicalTargetType: null,
        historicalTarget: null,
    }),
    computed: {
        position() {
            return store.state.createThing || "right";
        },
    },

    methods: {
        async sendThing() {
            await axios
                .post("http://10.103.1.107:3000/updateknowledge", {
                    thingType:  this.thingType,
                    thingDescription: this.thingDescription,
                    eventBasedTarget: this.eventBasedTarget,
                    eventTargetType: this.eventTargetType,
                    historicalTargetType: this.historicalTargetType,
                    historicalTarget: this.historicalTarget
                })
                .then((response) => {
                    console.log(response);
                });
        },
    },
};
</script>

<style scoped>
.newthing {
    z-index: 2000060;
}
</style>
