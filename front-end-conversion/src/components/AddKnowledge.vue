<template>
<div class="form-demo">
    <div class="flex justify-content-center">
        <div class="card">
            <form @submit.prevent="sendSparqlQuery" class="p-fluid form">
                <div class="field">
                    <div>
                        <InputText v-model="restLink" id="name" placeholder="Enter the IFC element Link" />
                    </div>
                </div>
                <div class="field">
                    <Editor v-model="sparqlInsertQuery" editorStyle="height: 320px">
                        <template #toolbar>
                            <span class="ql-formats">
                                <label> Enter the Sparql Query to add new Knowledge</label>
                            </span>
                        </template>
                    </Editor>
                </div>
                <Button type="submit" label="Submit" class="mt-2" />
            </form>
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            restLink: null,
            sparqlInsertQuery: null,
        };
    },

    methods: {
     sendSparqlQuery() {
             axios
                .post("http://127.0.0.1:3000/updateknowledge", {
                    restLink: this.restLink,
                    sparqlQuery: this.sparqlInsertQuery,
                })
                .then((response) => {
                    console.log(response);
                });
        },
    },
};
</script>

<style scoped>
.form {
    margin-top: 10px;
}
</style>
