import express from "express"
import __dirname from "./utils.js"
import handlebars from "express-handlebars"
import userRouter from "./router/userRouter.js"
import menuRouter from "./router/menuRouter.js"

const port=8080
const app=express();

app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use('/',express.static(__dirname+"/public"))
//ROUTES
app.use("/",userRouter)
app.use('/menu',menuRouter)

//SET HANDLEBARS
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
