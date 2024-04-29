import express from "express"
import __dirname from './utils.js'
console.log(__dirname)
import handlebars from 'express-handlebars'

import menuRouter from "./router/menuRouter.js"
import userRouter from './/router/userRouter.js'

const port=8084
const app=express();
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use('/',express.static(__dirname+"/public"));
app.use('/',userRouter)
app.use('/menu',menuRouter)

//SET HANDLEABRS
app.engine('handlebars',handlebars.engine());
app.set('view engine',"handlebars");
app.set('views',__dirname+'/views');

app.listen(port,()=>{
    console.log(`app listening on port ${port}`)
}).on("error", function (err) {
    process.once("SIGUSR2", function () {
      process.kill(process.pid, "SIGUSR2");
    });
    process.on("SIGINT", function () {
      // this is only called on ctrl+c, not restart
      process.kill(process.pid, "SIGINT");
    });
  });

