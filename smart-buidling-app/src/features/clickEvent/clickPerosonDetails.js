import store from "../../store/index"


export function clickPersonData() {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == "1Qfe3f5n95yfrQ8nllTWu9") {
            console.log("id clicked");
            store.state.person.name = "Arun R S"
            store.state.person.postion = "Research Intern"
            store.state.person.emailID = "arunvishnu40@gmail.com"
            store.state.person.imageLink = "src/assets/67491341.jfif"
            store.state.tablepersonDialog = true
        }
        if (pickResult.entity.id == "1Qfe3f5n95yfrQ8nllTWu8") {
            store.state.person.name = "Mouloud IFERROUDJENE"
            store.state.person.postion = "Doctorant"
            store.state.person.emailID = "mouloud.iferroudjene@emse.fr"
            store.state.person.imageLink = "src/assets/mouloud.jpeg"
            store.state.tablepersonDialog = true
        }
        if (pickResult.entity.id == "1Qfe3f5n95yfrQ8nllTWzq") {
            store.state.person.name = "Alaa Daoud "
            store.state.person.postion = "Maitre Assistant Associé"
            store.state.person.emailID = "alaa.daoud@emse.fr"
            store.state.person.imageLink = "src/assets/1596111570528.jfif"
            store.state.tablepersonDialog = true
        }
        if (pickResult.entity.id == "1Qfe3f5n95yfrQ8nllTWx6") {
            store.state.person.name = "	HOUNAS Zehor Thilleli"
            store.state.person.postion = "Doctorant"
            store.state.person.emailID = "zehor-thilleli.hounas@edf.fr"
            store.state.person.imageLink = "src/assets/plain.jpg"
            store.state.tablepersonDialog = true
        }
    })
}