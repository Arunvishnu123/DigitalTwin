<template>
<div>
    <w-drawer width="120em" class="newemployee" v-model="$store.state.createEmployee" :[position]="true">
        <w-button @click="$store.state.createEmployee = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="humidity" bg-color="primary">Add Employee</w-tag>
            <w-form @submit.prevent="sendemployee">
                <w-divider class="ma6" color="white" />
                <w-input v-model="firstName" class="mb6" label="Employee First Name" outline>
                </w-input>
                <w-input v-model="lastName" class="mb6" label="Employee Second Name" outline></w-input>

                <w-input v-model="emailID" class="mb6" label="Employee Email ID " outline>
                </w-input>
                <w-input v-model="employeeTitle" class="mb6" label="Employee Title" outline>
                </w-input>
                <w-input v-model="employeeImage" class="mb6" label="Employee Image Link" outline>
                </w-input>
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
        firstName: null,
        lastName: null,
        emailID: null,
        employeeTitle: null,
        employeeImage: null

    }),
    computed: {
        position() {
            return store.state.createEmployee || "right";
        },
    },

    methods: {
        async sendemployee() {

            await axios
                .post("http://127.0.0.1:3000/addEmployee", {
                    firstName: this.firstName,
                    lastName: this.lastName,
                    emailID: this.emailID,
                    employeeTitle: this.employeeTitle,
                    employeeImage: this.employeeImage,
                     IfcClass: store.state.thingifcClass,
                    IfcGuid: store.state.thingIfcId,
                })
                .then((response) => {
                    console.log(response);
                });
        },
    },
};
</script>

<style scoped>
.newemployee {
    z-index: 2000061;
}
</style>
