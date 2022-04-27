import * as mqtt from "mqtt"

export function readMQTT(path){
    let value 
    const host = 'ws://193.49.165.77:3128'
    const options = {
        clean: true,
        connectTimeout: 4000,     
    }
    const client  = mqtt.connect(host,options)
    client.subscribe(path, function() {
        //When a message arrives, print it to the console
        client.on('message', function(topic, message, packet) {
         // console.log("Received '" + message + "' on '" + topic + "'");
          console.log(message.toString())
          value = message.toString()
        });
    });

    return value
}