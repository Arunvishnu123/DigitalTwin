<template>
<div class="form-demo">
    <div class="flex justify-content-center">
        <div class="card">
            <form @submit.prevent="test" class="p-fluid form ">
                <div class="field">
                    <div >
                        <InputText id="name" placeholder="Enter the IFC element Link" />
                    </div>
                </div>
                <div class="field">
                    <Editor v-model="value" editorStyle="height: 320px">
                        <template #toolbar>
                            <span class="ql-formats">
                               <label> Enter the Sparql Query to Update the Knowledge Graph</label>
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
export default {
    data() {
        return {
            name: "",
            email: "",
        };
    },

};
</script>

<style  scoped>
.form{
margin-top: 10px;
}
</style>
