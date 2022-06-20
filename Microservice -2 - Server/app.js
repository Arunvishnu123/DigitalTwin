let express = require('express')
const app = express()

let bodyParser = require('body-parser');
const cookieParser = require('cookie-parser')
let cors = require('cors')

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(cors());
app.use(cookieParser())

//api call
const getAPI = require("./router/get")

app.use('/' , getAPI)

// Create port
const port = process.env.PORT || 4000;
const server = app.listen(port, () => {
    console.log('Connected to port ' + port)
})
// Find 404
app.use((req, res, next) => {
    next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
    console.error(err.message);
    if (!err.statusCode) err.statusCode = 500;
    res.status(err.statusCode).send(err.message);
});

