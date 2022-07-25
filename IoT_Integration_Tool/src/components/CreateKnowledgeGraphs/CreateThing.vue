<template>
<div>
    <w-drawer width="120em" class="newthing" v-model="$store.state.createThing" :[position]="true">
        <w-button @click="$store.state.createThing = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="humidity" bg-color="primary">Create New Thing</w-tag>
            <w-form @submit.prevent="sendThing">
              <w-divider class="ma6" color="white" />
                <w-input v-model="thingType" class="mb6" label="Thing Type" outline>
                </w-input>
                <w-divider class="ma6" color="white" />
                <w-flex>
                    <w-input v-model="eventBasedTarget" class="mb6" label="Event based target" outline> </w-input>
                    <w-input v-model="eventTargetType" class="mb6" label="Target type" outline> </w-input>
                    <w-input v-model="eventContentType" class="mb6" label="Content type" outline> </w-input>
                </w-flex>
                <w-textarea v-model="thingEventDescription" outline>Event based Sensor Description</w-textarea>
                <w-divider class="ma6" color="primary" />
                <w-flex>
                    <w-input v-model="historicalTarget" class="mb6" label="Histroical Target" outline> </w-input>
                    <w-input v-model="historicalTargetType" class="mb6" label="Target type" outline> </w-input>
                    <w-input v-model="historicalContentType" class="mb6" label="Content type" outline> </w-input>
                </w-flex>
                <w-textarea v-model="thingHistroicalDescription" outline>Historical based Sensor Description</w-textarea>
                <w-divider class="ma6" color="white" />
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
        thingEventDescription: null,
        eventBasedTarget: null,
        eventTargetType: null,
        historicalTargetType: null,
        historicalTarget: null,
        thingHistroicalDescription: null,
        eventContentType: null,
        historicalContentType: null,
    }),
    computed: {
        position() {
            return store.state.createThing || "right";
        },
    },

    methods: {
        async sendThing() {
            await axios
                .post("http://127.0.0.1:3000/updateknowledge", {
                    IfcClass:store.state.class,
                    IfcGuid:store.state.id,
                    thingType: this.thingType,
                    thingEventDescription: this.thingEventDescription,
                    eventBasedTarget: this.eventBasedTarget,
                    eventTargetType: this.eventTargetType,
                    historicalTargetType: this.historicalTargetType,
                    historicalTarget: this.historicalTarget,
                    thingHistroicalDescription: this.thingHistroicalDescription,
                    eventContentType: this.eventContentType,
                    historicalContentType: this.historicalContentType,
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
