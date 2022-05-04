

import $rdf from "rdflib"

export function readRoomData()
{

var store = $rdf.graph()

const data = store.sym('https://territoire.emse.fr/kg/emse/fayol/4ET/421');
const profile = data.doc()

const fetcher = new $rdf.Fetcher(store);

fetcher.load(profile).then(response => {
    const roomCapacity = new $rdf.Namespace("https://territoire.emse.fr/kg/ontology/");
    let roomCapcityNo = store.any(data, roomCapacity("roomCapacity"));
    console.log(roomCapcityNo.value)
    const rdfComment = new $rdf.Namespace("http://www.w3.org/2000/01/rdf-schema#")
    let rdfCommentData = store.any(data, rdfComment("comment"));

    console.log(rdfCommentData.value)
}, err => {
    console.log("Load failed" + err);
});

}
